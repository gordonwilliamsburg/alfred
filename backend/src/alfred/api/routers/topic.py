# Importing necessary modules from FastAPI and SQLAlchemy
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse

from alfred.pydantic_models import Topic
from alfred.topics import get_topics, save_topic

router = APIRouter()


@router.get("/")
async def healthcheck():
    return {"status": "healthy"}


@router.post("/save-topic")
async def save_topic_route(
    request: Request,
):
    body = await request.json()
    try:
        topic = Topic.new(text=body["text"], user_id=body["user_id"], urls=body["urls"])
        save_topic(topic)
        return JSONResponse(content={}, status_code=201)

    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid topic")


@router.get("/get-topics")
async def get_topics_route(request: Request):
    body = await request.json()
    try:
        user_id = body["user_id"]
        topics = get_topics(user_id)
        json_topics = [topic.dict() for topic in topics]
        return JSONResponse(content={"topics": json_topics}, status_code=200)

    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid topic")
