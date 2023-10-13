import requests
from apify import Actor
from bs4 import BeautifulSoup


async def main():
    async with Actor:
        input = await Actor.get_input()
        response = requests.get(input["url"])
        soup = BeautifulSoup(response.content, "html.parser")
        await Actor.push_data({"url": input["url"], "title": soup.title.string})
