from flask import Flask
import requests
from flask_restful import Resource, Api
from pprint import pprint
from pathlib import Path

path = Path(__file__).parent

app = Flask(__name__)
api = Api(app)


class Koor(Resource):
    def get(self, query):
        self.query = query
        self.plz = query.isdecimal()
        self.lat, self.lon = 0, 0
        if self.plz:
            self.get_coor(query)
        return (self.lat, self.lon), 200

    def get_coor(self, plz):
        r = requests.get(f"""https://public.opendatasoft.com/
                             api/records/1.0/search/?dataset=postleitzahlen-deutschland
                             &q={plz}&facet=note&facet=plz""")
        data = r.json()
        self.lat, self.lon = data['records'][0]['geometry']['coordinates']

        coor = (self.lat, self.lon)
        return coor


class Weather(Resource):
    def get(self, query):
        query = query
        coor = True if query.isdecimal() else False
        api_endpoint_weather = "http://api.openweathermap.org/data/2.5/weather"
        params = {"lang": "de", "units": "metric",
                  "appid": "f58428116698109cd066f2c91bdc0670"}
        if coor:
            params["zip"] = f"{query},DE"
        else:
            params["q"] = query
        r = requests.get(api_endpoint_weather, params=params)
        data = r.json()

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]

        result = f"""Query: {query} \t Temp: {temp} \t Gefühlt: {feels_like} \t
                     Beschreibung: {description}\n"""
        with open(path / "log.txt", "a") as file:
            file.write(result)
        return result, 200

    # def get_coor(self, plz):
    #     r = requests.get(f"""https://public.opendatasoft.com/
        #                      api/records/1.0/search/?dataset=postleitzahlen-deutschland
        #                      &q={plz}&facet=note&facet=plz""")
        # data = r.json()
    #     self.lat, self.lon = data['records'][0]['geometry']['coordinates']

    #     coor = (self.lat, self.lon)
    #     return coor


api.add_resource(Koor, "/koor/<string:query>")
api.add_resource(Weather, "/weather/<string:query>")

if __name__ == "__main__":
    app.run(debug=True)
