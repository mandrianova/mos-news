from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from auto_markup.api import auto_markup
from recommendations.api import recommendations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(recommendations)
app.include_router(auto_markup)
