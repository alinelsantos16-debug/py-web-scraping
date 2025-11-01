import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")

Soup = BeautifulSoup(response.text, "html.parser")

frases = Soup.find_all("span", class_="text")

for frase in frases:
    print(frase.text)



