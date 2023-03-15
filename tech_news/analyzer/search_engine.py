from tech_news.database import search_news


def search_adapter(filter):
    engine = search_news(filter)
    news_list: list[tuple] = [(news["title"], news["url"]) for news in engine]

    return news_list


# Requisito 7
def search_by_title(title: str):
    news = search_adapter({"title": {"$regex": title, "$options": "i"}})
    return news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# search_by_title("O que é array, para que serve e como fazer?")
