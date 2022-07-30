import requests
import json
import base64
import os
from tokens import client_id, client_secret_id
#urls

REDIRECT_URL = "https://tarandeep.ca"
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"

# scope - https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope = "playlist-modify-private playlist-read-private playlist-modify-public"

# dictionaries - for POST request

headers = {}
data = {}

##functions

# auth_code = requests.get(
#     AUTH_URL,
#     {
#         'client_id': client_id,
#         'response_type': 'code',  #from spotify docs
#         'redirect_url': REDIRECT_URL,
#         'scope': scope,
#     })

# print(auth_code.url)

auth_header = base64.urlsafe_b64encode(
    (client_id + ':' + client_secret_id).encode())

decode_auth_header = auth_header.decode("ascii")

headers['Authorization'] = f"Basic {decode_auth_header}"
data['grant_type'] = "client_credentials"
data['json'] = True
data['scope'] = scope

r = requests.post(url=TOKEN_URL, headers=headers, data=data)

#print(json.dumps(r.json(), indent=2))
