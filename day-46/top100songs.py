import requests
from bs4 import BeautifulSoup

date = input("What year would you like to travel to? (YYYY-MM-DD) ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
siteInfo = BeautifulSoup(response.text, "html.parser")

songs = siteInfo.findAll("h3", class_="c-title", id="title-of-a-story")
songTitles = []
for song in songs:
  songTitle = song.getText().strip("\n")
  songTitle = songTitle.replace('\r', '').replace('\n', '').replace('\t', "")
  if(songTitle != "Songwriter(s):" and songTitle != "Producer(s):" and songTitle != "Imprint/Promotion Label:"):
    songTitles.append(songTitle)

print(songTitles)
