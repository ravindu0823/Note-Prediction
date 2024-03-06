import requests
from bs4 import BeautifulSoup
import json

url = "https://medicalxpress.com/tags/perfect+pitch/sort/popular/all"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

items = soup.find_all('article', class_='sorted-article d-flex')

newsArray = []


for item in items:
    category = item.find('div', class_='sorted-article-topic mb-2').text # Category
    title = item.find('a', class_='news-link').text # Title
    target = item.find('a', class_='news-link')['href'] # Target
    desc = item.find('p', class_='mb-4').text.strip()
    if item.find('img'):
        image = item.find('img')['data-src']
    else:
        image = "null"
    date = item.find('p', class_='text-uppercase text-low').text.strip().replace("weblog", "")

    newsData = {
        "category": category,
        "title": title,
        "target": target,
        "desc": desc,
        "date": date,
        "image": image
    }

    newsArray.append(newsData)

final_steam_json = json.dumps(newsArray, indent=4)
print(final_steam_json)
