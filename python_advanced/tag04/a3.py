import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
from time import time

start = time()

base_url = "https://webscraper.io/"
start_url = "test-sites/e-commerce/allinone"

r = requests.get(base_url + start_url)

page = bs(r.text, "html.parser")

titles = []

links = page.find_all("a", class_="category-link")


for link in links:
    category_page = bs(requests.get(base_url + link["href"]).text,
                       "html.parser")

    subcategory_links = category_page.find_all("a", class_="subcategory-link")
    for link in subcategory_links:
        subcategory_page = bs(requests.get(base_url + link["href"]).text,
                              "html.parser")
        subcat_links = subcategory_page.find_all("a", class_="title")
        for link in subcat_links:
            item_page = bs(requests.get(base_url + link["href"]).text,
                           "html.parser")
            title = item_page.find_all("h4")[1]

            titles.append(title.text)
        # titles.extend([subcat_link.text for subcat_link in subcat_links])


pprint(titles)
print(len(titles))

print(time()-start)
