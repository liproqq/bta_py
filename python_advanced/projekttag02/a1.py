import requests
import json
from pathlib import Path
import base64

path = Path(__file__).parent

api_cred = {}

api_endpoint = "https://api.twitter.com/1.1/followers/ids.json"

with open(path / "authentication.json") as auth:
    api_cred = json.load(auth)

# key_secret = f""""{api_cred['api-key']}:
#                   {api_cred['api-secret']}""".encode("ascii")
# b64_key_secret = base64.b64encode(key_secret).decode("ascii")

headers = {'Authorization': f"Bearer {api_cred['bearer-token']}"}


query = input("Bitte Twitter handle eingeben(ohne @): ")
params = {"screen_name": query}

r = requests.get(api_endpoint, headers=headers, params=params)
response = r.json()

print(f"{query} hat {len(response['ids'])} follower auf Twitter")
