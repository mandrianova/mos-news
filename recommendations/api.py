import os
from fastapi import APIRouter
from .schemas import RecommendationAndHistoryOut, NewsItem
from .managers import get_history, get_recommendations

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

recommendations = APIRouter(prefix='/recommendations', tags=["recommendations"])


@recommendations.get("/{user_id}", response_model=RecommendationAndHistoryOut, summary="Get recommendation and history")
def generate_recommendations(user_id: int):
    """
    Generate recommendations with for selected user with the following structure:

    **recommendations** - prediction of news which might interest a given user
    - **id**: user id
    - **title**: news title
    - **date**: str representation of date of publication

    **history** - news history for selected user
    - **id**: user id
    - **title**: news title
    - **date**: str representation of date of publication
    """
    history_items = get_history(user_id)
    new_user = True if history_items == [] else False
    recommendations_items = get_recommendations(user_id, new_user = new_user)
    return RecommendationAndHistoryOut(
        recommendations=[NewsItem(**news_item) for news_item in recommendations_items],
        history=[NewsItem(**history_item) for history_item in history_items]
    )
