from typing import List

from alfred.pydantic_models import Topic


# TODO: actually query the database
def get_topics(user_id: str) -> List[Topic]:
    """
    Get the list of topics the user ins interested in, including the given URLs
    """
    return [
        Topic(
            user_id=user_id,
            topic_id="1",
            text="I want the latest news around reinforcment learning",
            urls=[
                "https://blog.google/technology/ai/rss/",
                "https://openai.com/blog/rss.xml",
            ],
        ),
        Topic(
            user_id=user_id,
            topic_id="2",
            text="I want to learn about recent developments in the Donetsk region of Ukraine / Russian war",
            urls=["https://www.theguardian.com/europe/rss"],
        ),
    ]
