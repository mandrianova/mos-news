from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class NewsItem(BaseModel):
    id: int
    title: str
    date: datetime


class RecommendationAndHistoryOut(BaseModel):
    recommendation_items: Optional[List[NewsItem]]
    histort_items: Optional[List[NewsItem]]
