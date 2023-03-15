from tech_news.database import search_news
from datetime import datetime


def search_adapter(query):
    engine = search_news(query)
    news_list: list[tuple] = [(news["title"], news["url"]) for news in engine]

    return news_list


# Requisito 7
def search_by_title(title: str):
    news = search_adapter({"title": {"$regex": title, "$options": "i"}})
    return news


# Requisito 8
def search_by_date(date: str):
    try:
        date_formated: str = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        return search_adapter({"timestamp": {"$regex": date_formated}})
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# search_by_title("O que é array, para que serve e como fazer?")

# print(search_by_date("2021-04-04"))
