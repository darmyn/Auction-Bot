from bs4 import BeautifulSoup

def get_element_for_category(html_content, category):
  soup = BeautifulSoup(html_content, "html.parser")

  # Find the corresponding <a> tag based on the category value
  selector = f"a[href*='all?category={category.value}']"
  category_element = soup.select_one(selector)

  return category_element