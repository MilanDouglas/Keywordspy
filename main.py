import requests
from bs4 import BeautifulSoup

s = requests.get("https://en.wikipedia.org/wiki/List_of_French_monarchs")

soup = BeautifulSoup(s.content, features="html.parser")
body = soup.find("div", {"id": "mw-content-text"})
paragraphs = body.find_all("p")
for paragraph in paragraphs[:10]:
  print(paragraph.text)