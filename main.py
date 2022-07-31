import json
import requests
from tokens import client_id, client_secret_id, user_id
from refresh import auth_token


class LikedSongs:

    def __init__(self) -> None:
        self.user_id = user_id
        self.auth_token = auth_token

    # def get_playlist(self):
    #     playlist_id = "2KQsKqJPdzB5dd13yOD0dE"
    #     query = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    #     r = requests.get(query,
    #                      headers={
    #                          'Content-Type': "application/json",
    #                          'Authorization': f"Bearer {self.auth_token}",
    #                      })
    #     r_json = r.json()
    #     print(r_json)

    def get_saved(self):
        query = f"https://api.spotify.com/v1/me/tracks"
        r = requests.get(query,
                         headers={
                             'Content-Type': "application/json",
                             'Authorization': f"Bearer {self.auth_token}",
                         })
        r_json = r.json()
        print(r_json)

    def get_top_items(self):
        limit = 100
        time_range = "short_term"
        query = f"https://api.spotify.com/v1/me/top/tracks?limit={limit}&time_range={time_range}&offset=0"

        r = requests.get(query,
                         headers={
                             'Content-Type': "application/json",
                             'Authorization': f"Bearer {self.auth_token}",
                         })
        r_json = r.json()
        print(r_json)

    def get_user(self):
        query = f"https://api.spotify.com/v1/me/"

        r = requests.get(query,
                         headers={
                             'Content-Type': "application/json",
                             'Authorization': f"Bearer {self.auth_token}",
                         })
        r_json = r.json()
        print(r_json)


test = LikedSongs()
test.get_saved()