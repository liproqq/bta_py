import requests
from pprint import pprint

api_key = "f58428116698109cd066f2c91bdc0670"
api_endpoint = "https://api.openweathermap.org/data/2.5/weather?"
city = "Berlin"
p = {"q": city, "appid": api_key, "units": "metric"}

r = requests.get(api_endpoint, params=p)

berlin = r.json()

print(berlin["weather"][0]["description"])
print(berlin["wind"]["speed"])
