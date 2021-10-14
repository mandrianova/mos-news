import os
import json

from fastapi import FastAPI
from starlette import status
from starlette.responses import Response

from . models import TheNewsIn, TheNewsOut, Recommendation
from . managers import get_markups, get_recommendations


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/history_news/{id}", response_model=TheNewsOut, tags=["history"])
def show_history(id: int):
    """test route to get history news from news.json accessed by index"""
    with open(os.path.join(BASE_DIR, "news.json"), "r") as file:
        data = json.load(file)
    response = data[id]
    return response


@app.post("/markups", tags=["mark_ups"])
def generate_markups(body: TheNewsIn):
    result = get_markups(body)
    return {"result": TheNewsOut(**result)}


@app.post("/recommendations/{user_id}", tags=["recommendations"])
def generate_recommendations(user_id: int):
    recommendations = get_recommendations(user_id)
    return {"recommendations": recommendations}


@app.post("/news/create", response_model=TheNewsOut)
def create_new_item(item: TheNewsOut):
    item_dict = item.dict()
    return item_dict
