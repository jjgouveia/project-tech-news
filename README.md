# Projeto - Tech news

## 🔨 Desenvolvimento

Nesse projeto, com base nos principais conceitos sobre a arquitetura de redes e como a internet e as diversas redes funcionam com seus diversos protocolos aprendidos, a Trybe designou um desafio em que efetivei a raspagem e análise de dados coletados da web. O principal objetivo do projeto seria criar um banco de dados (MongoDB) de notícias sobre tecnologia e realizar algumas consultas nas notícias registradas.

Essas notícias podem ser obtidas através da raspagem do Blog da Trybe.

## 🎯 O que foi avaliado?

## As capacidades de:

    📌 Técnicas de raspagem e manipulação de arquivos.;
    📌 Os arquivos de especificações deverão conter exatamente as configurações pedidas;
    📌 Os códigos deverão ser adaptados conforme proposto;
    📌 A organização e a aderência do código à especificação.
    📌 O arquivo com as instruções para execução do projeto deverá conter os comandos e o passo-a-passo conforme especificação;
    📌 Todas as adaptações e configurações deverão ser funcionais, de maneira a se comportarem conforme o esperado.
    📌 Testes deverão garantir o funcionamento das soluções, cuidando de não aprovar soluções incorretas.



## 💻 Tecnologias e Metodologias utilizadas:

    * Python;
    * Pytest;
    * Parsel;


## 📦 Instalação da aplicação:

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado

  <strong>Executar os testes</strong>

  ```bash
python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py
  ```

  Caso queria executar um teste especifico de um arquivo basta executar o comando:

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

  <strong>✍️ Teste Manual</strong>
  
  Abra um terminal Python importando as funções de interesse através do comando:

  <code>python3 -i tech_news/arquivo_de_interesse.py</code>

</details>

<details>
  <summary><strong>🐳Docker</strong></summary>
  Caso queria executar os seus testes de projeto via `Docker-compose`, substituindo o ambiente virtual, execute o comando:

  ```bash
  docker-compose run --rm news pytest
  ```

</details>

<details>
  <summary><strong>🏃🏾 Executando o Projeto</strong></summary>
  As notícias a serem raspadas estarão disponíveis no _Blog da Trybe_: https://blog.betrybe.com.
  Essas notícias devem ser salvas no banco de dados utilizando as funções python que já vêm prontas no módulo `database.py`

  <strong>MongoDB</strong>

  Para a realização deste projeto, utilizaremos um banco de dados chamado `tech_news`.
  As notícias serão armazenadas em uma coleção chamada `news`.
  Já existem algumas funções prontas no arquivo `tech_news/database.py` que te auxiliarão no desenvolvimento.
  Não altere as funções deste arquivo; mudanças nele não serão executadas no avaliador automático.

  Rodar MongoDB via Docker:
  <code>docker-compose up -d mongodb</code> no terminal.
  Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`

  Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:

  Ubuntu: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>
  MacOS:  <https://docs.mongodb.com/guides/server/install/>
  
  Com o banco de dados rodando, o nosso módulo conseguirá acessá-lo sem problemas. Importe o módulo `tech_news/database.py` e chame as funções contidas nele.
  Lembre-se de que o mongoDB utilizará por padrão a porta 27017. Se já houver outro serviço utilizando esta porta, considere desativá-lo.

</details>