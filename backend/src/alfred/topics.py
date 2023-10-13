from typing import List

from google.cloud import firestore

from alfred.pydantic_models import Topic

db = firestore.Client(database="alfred")


def save_topic(topic: Topic):
    topics_ref = db.collection("topics")

    # You can use `topic_id` as the document ID
    topic_doc_ref = topics_ref.document(topic.topic_id)

    # Save the topic to Firestore
    topic_doc_ref.set(topic.dict())


def get_topics(user_id: str) -> List[Topic]:
    topics_ref = db.collection("topics")

    # Query topics for a specific user
    queried_topics = topics_ref.where("user_id", "==", user_id).stream()

    # Convert the queried data to a list of Topic models
    return [Topic(**doc.to_dict()) for doc in queried_topics]
