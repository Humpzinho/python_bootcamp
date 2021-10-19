import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import json

with open("Day 46 - Spotify Playlist with Musical Time Machine\\private_data.json") as file:
    data = json.load(file)

client_id = data["client_id"]
client_secret = data["client_secret"]

date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
data = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date_input}")
print("Data has been received.")
data = data.text

soup = BeautifulSoup(data, "html.parser")
titles = soup.find_all("span", class_="chart-element__information__song text--truncate color--primary")
artists = soup.find_all("span", class_="chart-element__information__artist text--truncate color--secondary")
print("Data has been scraped.")

titles = [title.getText() for title in titles]
artists = [artist.getText() for artist in artists]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="Day 46 - Spotify Playlist with Musical Time Machine\\private_data.txt"))
print("Connected to Spotify.")

uri_list = []
user_id = sp.current_user()["id"]

year = date_input.split('-')[0]

for song, artist in zip(titles, artists):
    data = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = data["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except Exception as e:
        print(f"{song} from {artist} doesn't exist in Spotify. Skipping...\n")
    else:
        print(f"{song} from {artist} has been added.\n")

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)

print(playlist_id)
print(uri_list)

sp.playlist_add_items(playlist_id=playlist_id["id"], items=uri_list, position=None)