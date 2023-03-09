import requests
from bs4 import BeautifulSoup
import smtplib

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

URL = "https://www.amazon.fr/Seiko-Montre-Analogique-Automatique-Bracelet/dp/B0043R5WP4/ref=sr_1_8?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=seiko&qid=1628759079&s=watch&sr=1-8"

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.find(id="priceblock_saleprice").get_text())
