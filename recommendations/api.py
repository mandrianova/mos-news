import os
from fastapi import APIRouter
from .schemas import RecommendationAndHistoryOut, NewsItem
from .managers import get_history, get_recommendations

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

recommendations = APIRouter(prefix='/recommendations', tags=["recommendations"])


@recommendations.get("/{user_id}", response_model=RecommendationAndHistoryOut, summary="Get recommendation and history")
def generate_recommendations(user_id: int):
    """
    Generate an recommendations item with all the information:

    **recommendations** - prediction of news views for a given user
    - **id**: user id
    - **title**: title of the text
    - **date**: date publication

    **history** - news viewing history for this user
    - **id**: user id
    - **title**: title of the text
    - **date**: date publication
    """
    recommendations_items = get_recommendations(user_id)
    history_items = get_history(user_id)
    return RecommendationAndHistoryOut(
        recommendation_items=[NewsItem(**news_item) for news_item in recommendations_items],
        histort_items=[NewsItem(**history_item) for history_item in history_items]
    )
