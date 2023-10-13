from datetime import datetime
from typing import List

import feedparser

from alfred.pydantic_models import Article


def get_rss_posts(url: str) -> List[Article]:
    feed = feedparser.parse(url)
    quadruplets = []

    for entry in feed.entries:
        title = entry.title if "title" in entry else None
        description = entry.summary if "summary" in entry else None
        link = entry.link if "link" in entry else None
        thumbnail = None
        if "media_thumbnail" in entry and len(entry.media_thumbnail) > 0:
            thumbnail = entry.media_thumbnail[0]["url"]
        elif "enclosures" in entry and len(entry.enclosures) > 0:
            thumbnail = entry.enclosures[0].href

        # Extract the timestamp
        timestamp = None
        if hasattr(entry, "published_parsed"):
            timestamp = datetime(*entry.published_parsed[:6]).isoformat()

        quadruplet = Article(
            thumbnail=thumbnail,
            url=link,
            title=title,
            description=description,
            timestamp=timestamp,
        )

        quadruplets.append(quadruplet)

    return quadruplets


def print_rss_stats(quadruplets: List[Article]) -> None:
    if quadruplets:
        latest_post = max(quadruplets, key=lambda x: x.timestamp)  # type:ignore
        print("\nLatest post:\n")
        print(f"Title:\n{latest_post.title}")
        print(f"URL:\n{latest_post.url}")
        print(f"Timestamp:\n{latest_post.timestamp}")
        print(f"Thumbnail:\n{latest_post.thumbnail}")
        print(f"Description:\n{latest_post.description}")

        number_of_articles = len(quadruplets)
        print(f"\nNumber of articles: {number_of_articles}")
