from bs4 import BeautifulSoup
import requests
from os import environ
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

load_dotenv()
YOUR_APP_CLIENT_ID = environ["YOUR_APP_CLIENT_ID"]
YOUR_APP_CLIENT_SECRET = environ["YOUR_APP_CLIENT_SECRET"]
YOUR_APP_REDIRECT_URI = environ["YOUR_APP_REDIRECT_URI"]
user_library_read = environ["user_library_read"]


date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

dated_url = f"https://www.billboard.com/charts/hot-100/{date_input}/"

response = requests.get(dated_url)
webpage_html = response.text

soup = BeautifulSoup(webpage_html, "html.parser")

song_titles = soup.select("li ul li h3")
song_title_list = [song.getText().strip("\n\t") for song in song_titles]
song_artists= soup.select("li ul li[class~=o-chart-results-list__item] span[class~=c-label]")
song_artists_list = [artist.getText().strip("\n\t") for artist in song_artists if artist.getText().strip("\n\t").isdigit() == False and artist.getText().strip("\n\t") != "-" ]

song_dict = {}
for i in range(len(song_title_list)):
  song_dict[i] = {"song_title": song_title_list[i], "song_artist": song_artists_list[i]}

with open("song_dict.json", "w") as f:
  json.dump(song_dict, f, indent=4)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID, client_secret=YOUR_APP_CLIENT_SECRET, redirect_uri=YOUR_APP_REDIRECT_URI, scope="playlist-modify-private, user-read-private, user-modify-playback-state, playlist-modify-public,  user-follow-modify, user-library-modify", show_dialog=True, cache_path="token.txt"))

song_uri_list = []
for i in range(len(song_dict)):
  try:
    sp_search_term = f'{song_dict[i]["song_title"]} {song_dict[i]["song_artist"]}'
    sp_search_result = sp.search(sp_search_term)
    song_uri = sp_search_result["tracks"]["items"][0]["id"]
    print(i, sp_search_term, song_uri)
    song_uri_list.append(song_uri)
  except:
    sp_search_term = f'{song_dict[i]["song_title"]}'
    sp_search_result = sp.search(sp_search_term)
    song_uri = sp_search_result["tracks"]["items"][0]["id"]
    print(i, sp_search_term, song_uri)
    song_uri_list.append(song_uri)

with open("song_uri_list.txt", "w") as f:
  for uri in song_uri_list:
    f.write(f"{uri}\n")

# Create playlist
userid = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=userid, name=f"{date_input} Billboard 100")

# Add Songs to Playlist
add_songs_to_pl = sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri_list)
