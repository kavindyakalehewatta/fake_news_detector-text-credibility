 # Fetch & search content
import requests
from bs4 import BeautifulSoup

def search_site(url, keywords):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text().lower()

        matches = sum(1 for k in keywords if k.lower() in text)
        return matches
    except:
        return 0
