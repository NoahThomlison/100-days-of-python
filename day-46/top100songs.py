import requests
from bs4 import BeautifulSoup

date = input("What year would you like to travel to? YYYY-MM-DD ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
siteInfo = BeautifulSoup(response.text, "html.parser")

songs = siteInfo.findAll(class_="c-title__link")
print(songs)
for song in songs:
  print(song)
