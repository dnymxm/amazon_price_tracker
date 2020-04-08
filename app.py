import requests
from bs4 import BeautifulSoup

# Common User Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537"
}

# URL of product you want to track
URL = "ENTER YOUR URL HERE"

# Get and Parse Data from Amazon to get the price
r = requests.get(URL, headers=headers)
if r.ok:
    soup = BeautifulSoup(r.content, "html.parser")
    price = soup.find(id="priceblock_ourprice").get_text()[:-2]
    print(price)
