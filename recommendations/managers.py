import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_history(user_id: int):
    # здесь будет произведён расчёт рекоммендаций согласно выбранному алгоритму
    with open('data/history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)
    return history[str(user_id)]


def get_recommendations(user_id: int):
    recommendations = []
    return recommendations


def update_recommendation_model():
    pass
