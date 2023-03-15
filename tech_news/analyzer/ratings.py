from tech_news.database import get_collection


# Requisito 10
def top_5_categories():
    query = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]

    categories_list = get_collection().aggregate(query)
    categories = [category["_id"] for category in categories_list]

    return categories
