from typing import List, Optional

from alfred.palm import recommend_post_with_palm
from alfred.pydantic_models import Recommendation, RSSPost, Topic


# TODO: actually implement using similarity metrics
def filter_using_similarity(
    topic: Topic, rss_feed: List[RSSPost], top_k=3
) -> List[RSSPost]:
    return rss_feed[:top_k]


def filter_using_palm(
    topic: Topic, rss_feed: List[RSSPost], top_k=3
) -> List[Recommendation]:
    recommendations = []
    for rss_post in rss_feed:
        worth_it, why = recommend_post_with_palm(topic, rss_post)
        if worth_it:
            recommendations.append(
                Recommendation(
                    user_id=topic.user_id,
                    topic_id=topic.topic_id,
                    thumbnail_url=rss_post.thumbnail,
                    note=why,
                    url=rss_post.url,
                )
            )
    return recommendations[:top_k]


def recommend(topic: Topic, rss_feed: List[RSSPost]) -> List[Recommendation]:
    rss_feed = filter_using_similarity(topic, rss_feed)
    recommendations = filter_using_palm(topic, rss_feed)
    return recommendations
