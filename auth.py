import requests
import urllib
import json
import base64
import os
from tokens import client_id, client_secret_id, manual_code
#urls

AUTH_URL = "https://accounts.spotify.com/authorize"
REDIRECT_URL = "https://tarandeep.ca"
TOKEN_URL = "https://accounts.spotify.com/api/token"

# scope - https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope = "playlist-modify-private playlist-read-private playlist-modify-public"

# dictionaries - for POST request

headers = {}
data = {}

auth_header = base64.urlsafe_b64encode(
    (client_id + ':' + client_secret_id).encode())

decode_auth_header = auth_header.decode("ascii")

##FOR USER
#auth link
auth_link = f"{AUTH_URL}?client_id={client_id}&response_type=code&redirect_uri={urllib.parse.quote_plus(REDIRECT_URL)}&scope={urllib.parse.quote_plus(scope)}"
print(auth_link)  #code has to be retrived manually in current state

headers['Authorization'] = f"Basic {decode_auth_header}"
data['grant_type'] = "authorization_code"
data['code'] = manual_code  #manual input from auth_link
data['json'] = True
data['redirect_uri'] = REDIRECT_URL

r = requests.post(url=TOKEN_URL, headers=headers, data=data)

# ##FOR PUBLIC
# #post request
# headers['Authorization'] = f"Basic {decode_auth_header}"
# data['grant_type'] = "client_credentials"
# data['json'] = True
# data['scope'] = scope

# r = requests.post(url=TOKEN_URL, headers=headers, data=data)

print(json.dumps(r.json(), indent=2))

auth_token = r.json()['access_token']
refresh_token = r.json()['refresh_token']

print(auth_token)
print(refresh_token)