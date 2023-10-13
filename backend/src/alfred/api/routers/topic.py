# Importing necessary modules from FastAPI and SQLAlchemy
from fastapi import APIRouter, Body, Depends, HTTPException, Query, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from alfred.pydantic_models import Topic
from alfred.topics import get_topics, save_topic

router = APIRouter()


@router.get("/")
async def healthcheck():
    return {"status": "healthy"}


class TopicPayload(BaseModel):
    text: str
    user_id: str
    urls: list[str]


@router.post(
    "/save-topic", status_code=201, response_model=None
)  # No response body, so set response_model to None
async def save_topic_route(topic_payload: TopicPayload = Body(...)):
    topic = Topic.new(
        text=topic_payload.text, user_id=topic_payload.user_id, urls=topic_payload.urls
    )
    save_topic(topic)
    return {}


@router.get("/get-topics")
async def get_topics_route(user_id: str = Query(...)):
    try:
        topics = get_topics(user_id)
        json_topics = [topic.dict() for topic in topics]
        return JSONResponse(content={"topics": json_topics}, status_code=200)

    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid topic")
