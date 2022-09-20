
# Aquecimento para a Formação em Infraestrutura de Dados | Escritório de Dados

# Etapa 3: Manipulando dados 📝

# Rodrigo Abreu Carvalho


""" 
Objetivo: agora, você pode observar que, na base de dados obtida, devido às diferentes 
nacionalidades dos usuários, os números de telefone e celular têm formatos diferentes. 
Você deve transformá-los para um formato único, escolhido arbitrariamente.

Descrição da solução: uma função que recebe, como parâmetro, um pandas.DataFrame 
e retorna um pandas.DataFrame com as mesmas colunas, mas com os números de telefone 
e celular formatados de forma única. 

"""


import requests

import json

import csv

import pandas 

def my_function(url, n):
    urln = url + '&results=' + str(n)
    table = pandas.read_csv(urln)
    table['phone'] = table['phone'].str.replace(r'\D', '') # \D : regex for non digit
    table['cell'] = table['cell'].str.replace(r'\D', '')
    table.to_csv('etapa3_table.csv', encoding = 'utf-8')

my_function(url = "https://randomuser.me/api/?format=csv", n = 500)
