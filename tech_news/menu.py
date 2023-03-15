import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)


# Requisitos 11 e 12
def analyzer_menu():
    option = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.\n"""
    )

    match option:
        case "0":
            parameter = input(
                "Digite quantas notícias serão buscadas: "
            ).isnumeric()
            get_tech_news(parameter)
        case "1":
            parameter = input("Digite o título: ")
            search_by_title(parameter)
        case "2":
            parameter = input("Digite a data no formato aaaa-mm-dd: ")
            search_by_date(parameter)
        case "3":
            parameter = input("Digite a categoria: ")
            search_by_category(parameter)
        case "4":
            top_5_categories()
        case "5":
            print("Encerrando script")
        case _:
            sys.stderr.write("Opção inválida\n")

    return option
