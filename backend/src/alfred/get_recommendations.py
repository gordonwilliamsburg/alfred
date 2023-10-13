import os
import tempfile
from typing import List, Optional

import numpy as np
from langchain.embeddings.openai import OpenAIEmbeddings

from alfred.palm import recommend_post_with_palm
from alfred.pydantic_models import Article, Recommendation, Topic


def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)


def top_k_similar(embeddings, target_embedding, k=1):
    similarities = [
        (i, cosine_similarity(target_embedding, emb))
        for i, emb in enumerate(embeddings)
    ]
    sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
    return [idx for idx, similarity in sorted_similarities[:k]]


# TODO: actually implement using similarity metrics
def filter_using_similarity(
    topic: Topic, feed: List[Article], top_k=7
) -> List[Article]:
    embed_func = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
    article_embeddings = embed_func.embed_documents([article.title for article in feed])
    topic_embedding = embed_func.embed_query(topic.text)

    indexes = top_k_similar(article_embeddings, topic_embedding, k=top_k)
    filtered_articles = [feed[idx] for idx in indexes]
    return filtered_articles


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
