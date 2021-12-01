
![Logo](https://miro.medium.com/max/1200/0*cw-3C4ArykPRrv8T.png)


# Scrapy Project

Scrapy é um framework open source para extrair informações de diversas páginas, prosseguindo as mesmas para pipelines que vão operar com esses dados.

Esse repositório é um conjunto de dois projetos utilizando esse framework, utilizando a seguinte estrutura para organizar o projeto:

## Features

- Web scrapping (scrapy)
- Armazenamento em banco de dados (sqlite)


## Como executar

Para executar essa aplicação, é necessário criar um ambiente virtual utilizando venv, você pode fazer isso da seguinte maneira:

```bash
  python -m venv ./env
  source ./env/bin/activate
```
  
Após isso, é necessário instalar todas as dependências necessárias e executar a aplicação:
```bash
  pip install --upgrage pip
  pip install -r requirements.txt
  cd quotes
  scrapy crawl quotes
```
    
## Autores

- [@matheusafonsouza](https://www.github.com/matheusafonsouza)


## Contribuição

Qualquer contribuição é extremamente bem vinda!
