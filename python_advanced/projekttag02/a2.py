from flask import Flask
import requests
from flask_restful import Resource, Api, reqparse
from pprint import pprint

app = Flask(__name__)
api = Api(app)

api_endpoint = "http://api.openweathermap.org/data/2.5/onecall"


class Koor(Resource):
    def get(self, query):
        self.query = query
        self.plz = query.isdecimal()
        self.lat, self.lon = 0, 0
        if self.plz:
            self.get_coor(query)
        return (self.lat, self.lon), 200

    def get_coor(self, plz):
        r = requests.get(f"https://public.opendatasoft.com/api/records/1.0/search/?dataset=postleitzahlen-deutschland&q={plz}&facet=note&facet=plz")
        data = r.json()
        self.lat, self.lon = data['records'][0]['geometry']['coordinates']

        coor = (self.lat, self.lon)
        return coor


api.add_resource(Koor, "/koor/<string:query>")

if __name__ == "__main__":
    app.run(debug=True)
