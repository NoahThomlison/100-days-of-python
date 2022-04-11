import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
siteInfo = BeautifulSoup(response.text, "html.parser")

titles = siteInfo.find(class_="gallery").findAll(class_="title")
greatestMovies = ""
for title in titles[::-1]:
  greatestMovies += (title.getText()) + "\n"

print(greatestMovies)
