import os
import json
from fastapi import APIRouter
from .schemas import TheNewsOut
from .managers import get_recommendations

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

recommendations = APIRouter(prefix='/recommendations', tags=["recommendations"])


@recommendations.get("/")
def read_root():
    return {"Hello": "World"}


# TODO: поразмышлять на тему роутов / подчеркивание или слэш
@recommendations.get("/history_news/{id}", response_model=TheNewsOut, tags=["history"])
def show_history(id: int):
    """test route to get history news from news.json accessed by index"""
    with open(os.path.join(BASE_DIR, "news.json"), "r") as file:
        data = json.load(file)
    response = data[id]
    return response


@recommendations.post("/{user_id}")
def generate_recommendations(user_id: int):
    recommendations = get_recommendations(user_id)
    return {"recommendations": recommendations}


@recommendations.post("/news/create", response_model=TheNewsOut)
def create_new_item(item: TheNewsOut):
    item_dict = item.dict()
    return item_dict
