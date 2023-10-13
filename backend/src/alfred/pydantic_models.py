from typing import List, Optional

from pydantic import BaseModel


class Recommendation(BaseModel):
    user_id: str
    topic_id: str
    thumbnail_url: Optional[str]
    note: str
    url: str


class Topic(BaseModel):
    user_id: str
    topic_id: str
    text: str
    urls: List[str]


class RSSPost(BaseModel):
    thumbnail: Optional[str]
    url: str
    title: str
    description: Optional[str]
    timestamp: str
