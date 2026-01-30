import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"


response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

  
    quotes = []
    authors = []

    quote_elements = soup.find_all("span", class_="text")
    author_elements = soup.find_all("small", class_="author")

    for q, a in zip(quote_elements, author_elements):
        quotes.append(q.text)
        authors.append(a.text)
    df = pd.DataFrame({
        "Quote": quotes,
        "Author": authors
    })

    print(df)

    df.to_csv("scraped_quotes.csv", index=False)
    print("\nData Saved to scraped_quotes.csv")

else:
    print("Failed to retrieve page:", response.status_code)