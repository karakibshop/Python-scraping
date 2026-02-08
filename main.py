import requests
from bs4 import BeautifulSoup as bs
r = requests.get("https://www.tapology.com/fightcenter/events/135971-wood-vs-warrington-ii")
soup = bs(r.content)
print(soup.prettify())
div = soup.find("div")
print(div.prettify())
print(div.get_text())