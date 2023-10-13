from typing import List, Optional

from alfred.palm import recommend_post_with_palm
from alfred.pydantic_models import Article, Recommendation, Topic


# TODO: actually implement using similarity metrics
def filter_using_similarity(
    topic: Topic, feed: List[Article], top_k=3
) -> List[Article]:
    return feed[:top_k]


def filter_using_palm(
    topic: Topic, feed: List[Article], top_k=3
) -> List[Recommendation]:
    recommendations = []
    for feed_post in feed:
        worth_it, why = recommend_post_with_palm(topic, feed_post)
        if worth_it:
            recommendations.append(
                Recommendation(
                    user_id=topic.user_id,
                    topic_id=topic.topic_id,
                    thumbnail_url=feed_post.thumbnail,
                    note=why,
                    url=feed_post.url,
                )
            )
    return recommendations[:top_k]


def recommend(topic: Topic, feed: List[Article]) -> List[Recommendation]:
    feed = filter_using_similarity(topic, feed)
    recommendations = filter_using_palm(topic, feed)
    return recommendations  # type : ignore
