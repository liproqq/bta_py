from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    users = [
            {'name': 'Nico', 'age': 55, 'occupation': 'PR'},
            {'name': 'Melly', 'age': 42, 'occupation': 'Dev'},
            {'name': 'Erna', 'age': 60, 'occupation': None}]

    def get(self, name):
        if name.lower() == "all":
            return Users.users

        for user in Users.users:
            return ((user, 201) if name.lower() == user["name"].lower()
                    else (f"404: {name} not found"), 404)

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")

        args = parser.parse_args()

        if name.lower() == "all":
            return "not allowed", 403

        for user in Users.users:
            if name.lower() == user["name"].lower():
                return f"user {name} already exists", 403

        user = {
            "name": name.capitalize(),
            "age": int(args["age"]),
            "occupation": args["occupation"]
        }

        Users.users.append(user)

        print(Users.users)

        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")

        args = parser.parse_args()

        if name.lower() == "all":
            return "not allowed", 403
        for user in Users.users:
            if name.lower() == user["name"].lower():
                user["age"] = int(args["age"])
                user["occupation"] = args["occupation"]
                return user

            return f"user {name} does not exist", 404

    def delete():
        for index, user in enumerate(Users.users):
            if name.lower() == user["name"].lower():
                return Users.users.pop(index), 200


api.add_resource(Users, "/users/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
