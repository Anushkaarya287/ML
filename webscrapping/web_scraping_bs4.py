import requests
from bs4 import BeautifulSoup

url = "https://example.com"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
titles = soup.find_all("h1")

for t in titles:
    print(t.text)
