from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import patch
import pytest


data_mock = [
    {
        "url": "https://blog.betrybe.com/desenvolvimento-web/angular-cli/",
        "title": "Angular CLI: como usar essa interface de linha de comando?",
        "timestamp": "08/03/2023",
        "writer": "Cairo Noleto",
        "reading_time": 6,
        "summary": """Criar um projeto web com todas as estruturas de pastas,
        arquivos e até mesmo os conteúdos dentro do arquivo pode ser
        assustador, ainda mais quando você está em um de seus primeiros
        projetos.""",
        "category": "Desenvolvimento Web",
    },
    {
        "url": """https://blog.betrybe.com/linguagem-de-programacao/
        o-que-e-array/""",
        "title": "O que é array, para que serve e como fazer?",
        "timestamp": "06/03/2023",
        "writer": "Gleiciane Kelly",
        "reading_time": 5,
        "summary": """Array é uma estrutura que comporta uma coleção de dados
        do mesmo tipo. Se você quer saber o que é array, precisa saber que
        eles são muito importantes na programação.""",
        "category": "Linguagem de Programação",
    },
    {
        "url": """https://blog.betrybe.com/tecnologia/usabilidade-no
        -desenvolvimento-de-software/""",
        "title": """Usabilidade no Desenvolvimento de software e UX: como
        funciona?""",
        "timestamp": "01/03/2023",
        "writer": "Cairo Noleto",
        "reading_time": 11,
        "summary": """Você já passou pela frustração de tentar usar um
        aplicativo ou sistema e ele não corresponder às suas ações? Isso pode
        ocorrer com frequência quando não utilizamos os conceitos de
        usabilidade durante o desenvolvimento de um software,
        produto ou serviço.""",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/antivirus-android/",
        "title": """Antivírus Android: conheça os 10 melhores e
        saiba por que usar!""",
        "timestamp": "27/02/2023",
        "writer": "Cairo Noleto",
        "reading_time": 10,
        "summary": """Com o grande crescimento da tecnologia e das tecnologias
        móveis, como os dispositivos Android, as pessoas dependem cada vez
        mais desses dispositivos que são verdadeiros facilitadores em nossa
        rotina diária.\xa0Realizar compras pela internet ou até mesmo
        transferências através aplicativo de banco sem ter que sair do
        conforto de sua casa é a melhor coisa, não é mesmo?""",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/tipos-de-firewall/",
        "title": """Conheça os 11 tipos de firewall,
        saiba como funcionam e qual usar""",
        "timestamp": "22/02/2023",
        "writer": "Cairo Noleto",
        "reading_time": 9,
        "summary": """O surgimento dos tipos de firewall foi um avançado
        excepcional na tecnologia, já que firewall é o sistema de segurança
        capaz de realizar análises em sites e proteger as pessoas
        usuárias de ataques e páginas maliciosas.""",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/protocolo-tcp-ip/",
        "title": "Protocolo TCP/IP: o que é e exemplos de como funciona",
        "timestamp": "17/02/2023",
        "writer": "Cairo Noleto",
        "reading_time": 9,
        "summary": """A todo o instante diversos dados trafegam pela rede:
        seja o envio de um e-mail, uma mensagem, foto, arquivo, esses dados
        partem de um ponto A para um ponto B. Mas como essa comunicação é
        feita? Para respondermos a essa pergunta, vamos aprender sobre o
        protocolo TCP/IP.""",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/programacao-em-arduino/",
        "title": "Programação em Arduino para iniciantes em 11 passos!",
        "timestamp": "14/02/2023",
        "writer": "Cairo Noleto",
        "reading_time": 14,
        "summary": """Você sabia que com a utilização de um arduino é possível fazer
        sensores de led ou até mesmo aqueles carrinhos autônomos
        bastante parecidos com um robô?
        Pois bem, com um arduino em mãos é possível desenvolver diversas
        coisas que podem trazer algumas facilidades em seu cotidiano.""",
        "category": "Tecnologia",
    },
    {
        "url": """https://blog.betrybe.com/tecnologia/
        sistema-operacional-windows/""",
        "title": """Sistema Operacional Windows: versões,
        dicas e como instalar?""",
        "timestamp": "06/02/2023",
        "writer": "Cairo Noleto",
        "reading_time": 18,
        "summary": """É fato que todo computador necessita de um sistema
        operacional para funcionar. Entretanto, diversas opções estão
        disponíveis no mercado, como o Windows, o Mac OS, o Linux e suas
        variações.""",
        "category": "Tecnologia",
    },
]


@patch("tech_news.analyzer.reading_plan.ReadingPlanService")
def test_reading_plan_group_news(mock_find_news):
    mock_find_news.return_value = data_mock
    news_for_available_time = ReadingPlanService.group_news_for_available_time(
        8
    )

    assert len(news_for_available_time["readable"]) == 3
    assert len(news_for_available_time["unreadable"]) == 7
    assert news_for_available_time["readable"][0]["unfilled_time"] == 2

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)
