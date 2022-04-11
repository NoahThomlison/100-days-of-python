import re
from bs4 import BeautifulSoup
import requests
url = "https://news.ycombinator.com/news"
response = requests.get(url)
data = BeautifulSoup(response.text, "html.parser")

articleTexts = []
articleLinks = []

titles = data.findAll(class_="titlelink", name="a")
for title in titles:
  titleText = title.getText()
  linkText = title.get("href")
  articleTexts.append(titleText)
  articleLinks.append(linkText)

articleScore = [int(score.getText().split()[0]) for score in data.findAll(class_="score")]

maxUpvoted = articleScore.index(max(articleScore))
print(articleTexts[maxUpvoted], articleScore[maxUpvoted], articleLinks[maxUpvoted])