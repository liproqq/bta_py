import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = "https://webscraper.io/test-sites/e-commerce/allinone"

r = requests.get(url)

page = bs(r.text, "html.parser")

titles = page.find_all("a", class_="title")
prices = page.find_all("h4", class_="price")
descriptions = page.find_all("p", class_="description")

captions_dict = [
                 {"title": title.text,
                  "price": price.text,
                  "description": description.text}
                 for (title, price, description)
                 in zip(titles, prices, descriptions)
                 ]

pprint(captions_dict)
