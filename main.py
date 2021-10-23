from concurrent.futures.process import ProcessPoolExecutor
import asyncio
from enum import Enum
from http import HTTPStatus
from typing import Dict
from uuid import UUID
from starlette.background import BackgroundTasks
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from auto_markup.api import auto_markup
from auto_markup.model import update_auto_markup_model
from auto_markup.schemas import Job
from recommendations.api import recommendations
from recommendations.managers import update_recommendation_model

app = FastAPI()

jobs: Dict[UUID, Job] = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(recommendations)
app.include_router(auto_markup)


@app.on_event("startup")
async def startup_event():
    app.state.executor = ProcessPoolExecutor()


@app.on_event("shutdown")
async def on_shutdown():
    app.state.executor.shutdown()


@app.get("/status/{uid}", tags=["task"])
async def status_task(uid: UUID):
    """
    Check status task for id

    **Input**
    - **uid**: unique task number

    **Output**
    - **uid**: unique task number
    - **status**: execution status
    - **exception**: if status failed return Error
    """
    return jobs[uid]


class ModelName(Enum):
    auto_markup = 'auto_markup'
    recommendations = 'recommendations'


@app.post("/update_models", status_code=HTTPStatus.ACCEPTED, tags=["task"])
async def update_model(model_name: ModelName, background_tasks: BackgroundTasks):
    """
    Updating the model to choose in the background

    **Input**
    - **model_name**: auto_markup or recommendations

    **Output**
    - **uid**: unique task number by which you can track its execution in status_task func
    - **status**: execution status
    - **exception**: exception status
    """
    new_task = Job()
    jobs[new_task.uid] = new_task
    if model_name == ModelName.auto_markup:
        func = update_auto_markup_model
    elif model_name == ModelName.recommendations:
        func = update_recommendation_model
    else:
        raise HTTPException(status_code=400, detail="Error start task, check logs")
    background_tasks.add_task(start_update_task_handler, func, new_task.uid)
    return new_task


async def start_update_task_handler(func, uid: UUID) -> None:
    """Run task"""
    try:
        await run_in_process(func)
        jobs[uid].status = "complete"
    except Exception as ex:
        jobs[uid].status = "failed"
        jobs[uid].exception = f'{ex}'


async def run_in_process(func, *args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(app.state.executor, func, *args)
