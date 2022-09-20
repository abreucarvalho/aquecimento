
# Aquecimento para a formação em infraestrutura

# Etapa 1: Entendendo os dados 🎲

# Rodrigo Abreu Carvalho

""" 
Objetivo: nessa etapa, você deve somente ingerir dados da API do randomuser.me e observar 
o formato dos dados, tentando imaginar como eles poderiam ser usados para construir uma tabela.

Descrição da solução: a solução dessa etapa consiste em uma função para consumir a API na 
URL https://randomuser.me/api/ e retornar um dicionário com os dados. 

"""

# Making API Requests in Python

import requests # requires installation > python -m pip install requests

import json

# Print JSON function

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(text)

# Request and print function

def my_function(url):
    response = requests.get(url)
    jprint(response.json())

url = "https://randomuser.me/api/?results=5000"

my_function(url)
