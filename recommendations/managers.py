import os
import json
from .models import combine_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_history(user_id: int):
    with open('data/history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)
        try:
            personal_history = sorted(history[str(user_id)], key=lambda i: i['date'], reverse=True)
        except:
            personal_history = []
    return personal_history


def get_recommendations(user_id: int, new_user: bool):
    if new_user:
        recommendations = update_general_rating()
    else:
        recommendations = []
    return recommendations


def update_recommendation_model():
    pass


def update_general_rating():
    combine_data()
