# Importing necessary modules from FastAPI and SQLAlchemy
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from alfred.get_recommendations import recommend
from alfred.get_topics import get_topics
from alfred.pydantic_models import Recommendation
from alfred.rss import get_rss_posts

router = APIRouter()


@router.get("/get-curation", response_model=List[Recommendation])
async def get_curation(user_id: str):
    topics = get_topics(user_id)

    recommendations = []
    for topic in topics:
        rss_feed = []
        for url in topic.urls:
            rss_feed.extend(get_rss_posts(url=url))
        recommendations.extend(recommend(topic=topic, rss_feed=rss_feed))
    return recommendations
