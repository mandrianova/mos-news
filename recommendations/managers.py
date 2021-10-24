import os
import json
from .models import combine_data, generate_cold_start_rating

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
    pass


def get_recommendations(user_id: int, new_user: bool):
    if new_user == True:
        if os.path.isfile(path_to_cold_start_rating):
            with open(path_to_cold_start_rating, 'r') as file:
                recommendations = json.load(file)[:20]
            print(recommendations)
        else:
            recommendations = generate_cold_start_rating()
    else:
        recommendations = []
    return recommendations