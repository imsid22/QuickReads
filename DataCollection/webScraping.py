from bs4 import BeautifulSoup
import requests
import json

# Placeholder URLs to scrape the data
URLs = ['https://venturebeat.com/tag/data-science/']

articles = []

for url in URLs:
    # Fetch webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Locate articles (assuming they are within the articles tag)
    results = soup.find(id='river')

    for article in results.find_all('article', class_='ArticleListing'):
        
        title = article.text

        articles.append({
            'title': title,
            'content': ''
        })

print(articles)