import requests
from requests import HTTPError, ReadTimeout
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url, wait=3):
    headers = {"user-agent": "Fake user-agent"}
    try:
        sleep(1)
        response = requests.get(url, timeout=wait, headers=headers)
        response.raise_for_status()
    except(HTTPError, ReadTimeout):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    try:
        quotes = selector.css('.entry-title > a::attr(href)').getall()
    except(requests.exceptions.ConnectionError):
        return []

    return quotes


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    try:
        next_page = selector.css('.next::attr(href)').get()
    except(requests.exceptions.ConnectionError, HTTPError):
        return None
    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    scrape = {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css('.entry-title::text').get().strip(),
        "timestamp": selector.css('.meta-date::text').get(),
        "writer": selector.css('.author > a::text').get(),
        "reading_time": int(selector.css('.meta-reading-time::text')
                            .get()[:2]),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "category": selector.css(".label::text").get(),
    }

    return scrape


# Requisito 5
def get_tech_news(amount: int):
    BASE_URL = "https://blog.betrybe.com"
    paginator = True
    news: list[dict] = []

    while paginator and len(news) < amount:
        content = fetch(BASE_URL)
        links = scrape_updates(content)
        BASE_URL = scrape_next_page_link(content)
        for link in links:
            if len(news) < amount:
                page_content = fetch(link)
                new = scrape_news(page_content)
                news.append(new)
            else:
                paginator = False
                break

    create_news(news)
    return news[:amount]
