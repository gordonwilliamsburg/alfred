import json
from typing import Tuple

from langchain.chat_models import ChatVertexAI

from alfred.json_utils import clean_json_string
from alfred.pydantic_models import Article, Topic


def recommend_post_with_palm(topic: Topic, feed_post: Article) -> Tuple[bool, str]:
    output = ask_text(
        f"""
        I will give you a user description of a topic he wishes to follow and a news article content.
        Your task is to output just a JSON object with two keys:
        - 'article-content' – a repetition of the article content to remind you of the context.
        - 'article-reasoning' - a very detailed reasoning on the article contents.
        You should create a meaningful (alwauys with the user's topic description in mind) reasoning on why the user should AND should not be recommended this article.
        Both negative and positive reasoning should be equally detailed, and always with the user topic in mind.
        Lastly you should make the bridge to the user description, culminating in either a recommendation or not.
        If you don't have enough information about the article, you must explicitly state that you don't have enough information.
        - 'worth_it' - a boolean value indicating whether the user should be recommended this article
        You should only return true when you have absolute confidence that the user will be interested in the article.

        User Topic Description:
        - {topic.text}

        Article Title: {feed_post.title}
        Article Description: {feed_post.description}

        Now go!
    """.replace(
            "    ", ""
        ),
        model="codechat-bison",
    )
    output = clean_json_string(output)
    output = json.loads(output)

    print(f"Topic: {topic.text}")
    print(f"Post: {feed_post.description}")
    print(output)
    return output["worth_it"], output["article-reasoning"]  # type: ignore


def ask_text(text: str, model="chat-bison", max_output_tokens=1000) -> str:
    print(f"Asking Text: \n{text}")
    chat = ChatVertexAI(
        model_name=model, max_output_tokens=max_output_tokens, temperature=0, top_k=20
    )
    return chat.predict(text)
