from bs4 import BeautifulSoup

with open("./website.html") as website:
  contents = website.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)
print(soup.prettify)
allTages = (soup.findAll(name="a"))

for tag in allTages:
  print(tag.getText())
  print(tag.get("href"))

heading = soup.findAll(name="h1", id="name")
print(heading)

section_heading = soup.findAll(name="h3", class_="heading")
print(section_heading.getText())

companyUrl = soup.select_one("p a")
name = soup.select_one("#name")
headings = soup.select(".heading")