from typing import List

from alfred.config import apify_client
from alfred.pydantic_models import BaseResult


def search_google(query: str) -> List[BaseResult]:
    # Prepare the Actor input
    run_input = {
        "queries": query,
        "maxPagesPerQuery": 1,
        "resultsPerPage": 10,
        "mobileResults": False,
        "languageCode": "",
        "maxConcurrency": 10,
        "saveHtml": False,
        "saveHtmlToKeyValueStore": False,
        "includeUnfilteredResults": False,
        "customDataFunction": """async ({ input, $, request, response, html }) => {
    return {
        pageTitle: $('title').text(),
    };
    };""",
    }

    # Run the Actor and wait for it to finish
    run = apify_client.actor("apify/google-search-scraper").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    for item in apify_client.dataset(run["defaultDatasetId"]).iterate_items():
        # print(item)
        """
        These are example queries that might be relevant to the user query, consists of title and url
        example related_query:
        {'title': 'Best food in nyc', 'url': 'https://www.google.com/search?sca_esv=573110829&q=Best+food+in+nyc&sa=X&ved=2ahUKEwjq-ZPwu_KBAxXkEFkFHQNvDhwQ1QJ6BAhVEAE'}
        """
        # related_queries_data = item.get("relatedQueries", [])
        # for related_query in related_queries_data:
        #    print(related_query)
        """
        These are the results related to the user query, consisting of title, url, description, date
        example organic_result:
        {'title': '20 Iconic Dishes to Try in New York City', 'url': 'https://ny.eater.com/maps/new-york-city-iconic-dishes-restaurants', 'displayedUrl': 'https://ny.eater.com › maps › new-york-city-iconic-dishe...', 'description': "Where to find NYC's most iconic dishes: pastrami on rye at Katz's Deli, banana pudding at Magnolia Bakery, spicy cumin lamb noodles at Xi'an\xa0...", 'date': '2022-12-20T12:00:00.000Z', 'emphasizedKeywords': ["NYC's"], 'siteLinks': [], 'productInfo': {}, 'type': 'organic', 'position': 1}
        """
        organic_results = item.get("organicResults", [])
        results = [
            BaseResult(
                url=organic_result["url"],
                title=organic_result["title"],
                description=organic_result["description"],
                position=organic_result["position"],
                emphasizedKeywords=organic_result["emphasizedKeywords"],
            )
            for organic_result in organic_results
        ]

    return results


print(search_google("Food in new york for upscale high end trendy fusion kitchen"))
