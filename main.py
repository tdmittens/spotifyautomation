import json
import requests
from tokens import client_id, client_secret_id, user_id
from auth import auth_token


class LikedSongs:

    def __init__(self) -> None:
        self.user_id = user_id
        self.auth_token = auth_token

    def get_playlist(self):
        playlist_id = "2KQsKqJPdzB5dd13yOD0dE"
        query = f"https://api.spotify.com/v1/playlists/{playlist_id}"
        r = requests.get(query,
                         headers={
                             'Content-Type': "application/json",
                             'Authorization': f"Bearer {self.auth_token}",
                         })
        r_json = r.json()
        print(r_json)

    def get_saved(self):
        query = f"https://api.spotify.com/v1/me/playlists"
        r = requests.get(query,
                         headers={
                             'Content-Type': "application/json",
                             'Authorization': f"Bearer {self.auth_token}",
                         })
        r_json = r.json()
        print(r_json)


test = LikedSongs()
test.get_saved()