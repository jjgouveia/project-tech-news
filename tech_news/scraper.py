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


# html = fetch("https://blog.betrybe.com/")
# print(scrape_updates(html))


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
