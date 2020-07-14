import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pprint import pprint

url = "https://www.webscraper.io/test-sites/tables"

r = requests.get(url)

soup = bs(r.text, "html.parser")
soup_table = soup.find("table")

headers = soup_table.find_all("th")
rows = soup_table.tbody.find_all("tr")

# print(rows[2].text)

table = [[header.text for header in headers]]


for row in rows:
    temp_row = []
    for td in row.find_all("td"):
        temp_row.append(td.string)
    table.append(temp_row)

pprint(table)

# pandas
df = pd.read_html(str(soup_table), index_col="#")[0]

print(df)
