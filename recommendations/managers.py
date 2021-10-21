import os
import json
from datetime import datetime

from auto_markup.model import get_result_tag_and_spheres_for_title_preview_fulltext
from . schemas import TheNewsIn, TheNewsOut
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_recommendations(user_id: int):
    # здесь будет произведён расчёт рекоммендаций согласно выбранному алгоритму
    history = pd.read_excel(os.path.join(BASE_DIR, "dataset_news_1.xlsx"))
    history = history[history.user_id == user_id]
    print(history)
    new_recommendations = [{"id": 345, "title": "first recommendation", "date": datetime.today()}, ]
    return new_recommendations
