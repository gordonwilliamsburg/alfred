import uuid
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

    @classmethod
    def new(cls, text: str, user_id: str, urls: List[str]):
        return cls(
            topic_id=str(uuid.uuid4()),
            user_id=user_id,
            text=text,
            urls=urls,
        )


# the result coming from google search
class Article(BaseModel):
    url: str
    title: str
    description: Optional[str]
    timestamp: Optional[str]
    position: Optional[int]  # the ranked position
    emphasizedKeywords: Optional[List[str]]  # list of emphasized keywords
    thumbnail: Optional[str]
