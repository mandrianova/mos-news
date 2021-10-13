import os
import json
from datetime import datetime
from . models import TheNewsIn, TheNewsOut
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_markups(body: TheNewsIn):
    # здесь будет произведена генерация разметки согласно выбранному алгоритму
    with open(os.path.join(BASE_DIR, "news.json"), "r") as file:
        data = json.load(file)
    print(data[:3])
    result = data[0]
    return result


def get_recommendations(user_id: int):
    # здесь будет произведён расчёт рекоммендаций согласно выбранному алгоритму
    history = pd.read_excel(os.path.join(BASE_DIR, "dataset_news_1.xlsx"))
    history = history[history.user_id == user_id]
    print(history)
    new_recommendations = [{"id": 345, "title": "first recommendation", "date": datetime.today()}, ]
    return new_recommendations
