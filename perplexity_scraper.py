import requests
from bs4 import BeautifulSoup

def get_trending_posts(industry):
    query = f"site:linkedin.com what's trending this week for {industry}"
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        links = [a.get_text() for a in soup.select("h3")]
        return links[:5]  # Top 5 post ideas
    except:
        return []
