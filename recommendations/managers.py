import os
import json

from recommendations.cold_rec import get_cold_recommendations
from recommendations.rec import retrain_recommend_model, generate_recommendations

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_to_cold_start_rating = os.path.join(BASE_DIR, 'data', 'cold_start_rating.json')


def get_history(user_id: int):
    with open('data/history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)
        try:
            personal_history = sorted(history[str(user_id)], key=lambda i: i['date'], reverse=True)
        except:
            personal_history = []
    return personal_history


def update_recommendations_model():
    retrain_recommend_model()


def get_recommendations_handler(user_id: int):
    recommendations = generate_recommendations(user_id)
    return recommendations


def get_cold_recommendations_handler():
    cold_recommendations = get_cold_recommendations()
    return cold_recommendations
