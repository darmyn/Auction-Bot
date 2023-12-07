import os
import requests
from dotenv import load_dotenv
from util import parsingUtil
import config

if __name__ == "__main__":
    load_dotenv()
    TARGET_DOMAIN = "kotnauction.com"
    TARGET_PAGE = "auction"
    TARGET_URL = f"https://{TARGET_DOMAIN}/{TARGET_PAGE}"
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    HTML_CONTENT = requests.get(TARGET_URL).content

    print(USERNAME)
    print(PASSWORD)

    # Example usage
    category_to_fetch = config.TARGET_CATEGORIES[0]
    category_element = parsingUtil.get_element_for_category(HTML_CONTENT, category_to_fetch)

    print(category_to_fetch)
    print(category_element)

    if category_element:
        print(f"Category: {category_to_fetch.name}")
        print(f"Element Text: {category_element.text}")
        print(f"Element Href: {category_element['href']}")
    else:
        print(f"No element found for category: {category_to_fetch.name}")

