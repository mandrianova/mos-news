import os
import json
from datetime import datetime
from time import perf_counter
from . models import TheNewsIn, TheNewsOut, Recommendation
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_personal_history(user_id: int):
    main_start = perf_counter()
    with open(os.path.join(BASE_DIR, 'data', 'dataset_with_titles.json'), 'r') as file:
        history = json.load(file)
    personal_history_news = [i for i in history if i['user_id'] == user_id]
    finish = perf_counter()
    print(f"takes {finish - main_start} seconds in total to get personal news")
    return [dict(filter(lambda x: x[0] != 'user_id', i.items())) for i in personal_history_news]
    

def get_markups(body: TheNewsIn):
    # здесь будет произведена генерация разметки согласно выбранному алгоритму
    with open(os.path.join(BASE_DIR, "data", "news.json"), "r") as file:
        data = json.load(file)
    result = data[0]
    return result


def get_recommendations(user_id: int):
    # здесь будет произведён расчёт рекоммендаций согласно выбранному алгоритму
    personal_history_news = get_personal_history(user_id)
    new_recommendations = [{"id": 345, "title": "first recommendation", "date": datetime.now().strftime('%Y-%m-%d %H:%M'), }]
    return new_recommendations, personal_history_news

