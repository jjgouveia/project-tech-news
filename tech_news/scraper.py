import requests
from requests import HTTPError, ReadTimeout
from time import sleep
from parsel import Selector


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
        "url": selector.css("link[rel='canonical']::attr(href)").get().strip(),
        "title": selector.css('.entry-title::text').get().strip(),
        "timestamp": selector.css('.meta-date::text').get().strip(),
        "writer": selector.css('.author > a::text').get().strip(),
        "reading_time": int(selector.css('.meta-reading-time::text')
                            .get()[:2]),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "category": selector.css(".label::text").get().strip(),
    }

    return scrape


# html = fetch("""https://blog.betrybe.com/linguagem-de-
# programacao/o-que-e-array/""")
# print(scrape_news(html))


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
