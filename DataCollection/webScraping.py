from bs4 import BeautifulSoup
import requests
import json

# Placeholder URLs to scrape the data
URLs = ['https://venturebeat.com/tag/data-science/']

articles = []

def fetchContent(link):
    """This function fetches the content from the given link

    Args:
        link (str): link of the article
    """
    response = requests.get(link)
    response_soup = BeautifulSoup(response.content, 'html.parser')
    link_result = response_soup.find(id='content')
    content = link_result.find_all(class_='article-content')
    paragraphs = []
    for content_div in content:
        for p in content_div.find_all('p'):
            paragraphs.append(p.get_text().replace('\xa0', ' ').replace('“', '').replace('”', '').strip())

    return ' '.join(paragraphs)

counter = 0
for url in URLs:
    # Fetch webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Locate articles (assuming they are within the articles tag)
    results = soup.find(id='river')

    for article in results.find_all('a', class_='ArticleListing__title-link'):
        if counter > 1:
            break
        title = article.text
        content = fetchContent(article.get('href'))

        articles.append({
            'title': title,
            'content': content
        })
        counter += 1
print(articles)