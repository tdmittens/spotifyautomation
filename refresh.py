import base64
import requests
from tokens import refresh_code, client_id, client_secret_id

TOKEN_URL = "https://accounts.spotify.com/api/token"

headers = {}
data = {}

auth_header = base64.urlsafe_b64encode(
    (client_id + ':' + client_secret_id).encode())

decode_auth_header = auth_header.decode("ascii")

headers['Authorization'] = "Basic " + decode_auth_header
data['grant_type'] = "refresh_token"
data['refresh_token'] = refresh_code  #manual input from auth_link

r = requests.post(url=TOKEN_URL, headers=headers, data=data)

#print(r.json())

auth_token = r.json()['access_token']