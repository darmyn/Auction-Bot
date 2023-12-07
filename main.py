import os
import requests
import openpyxl
import config
from util import parsingUtil

TARGET_DOMAIN = "kotnauction.com"
TARGET_PAGE = "auction"
TARGET_URL = f"https://{TARGET_DOMAIN}/{TARGET_PAGE}"
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HTML_CONTENT = requests.get(TARGET_URL).content

category_to_fetch = config.TARGET_CATEGORIES[0]
category_element = parsingUtil.get_element_for_category(HTML_CONTENT, category_to_fetch)

if category_element:
    print(f"Category: {category_to_fetch.name}")
    print(f"Element Text: {category_element.text}")
    print(f"Element Href: {category_element['href']}")
else:
    print(f"No element found for category: {category_to_fetch.name}")
