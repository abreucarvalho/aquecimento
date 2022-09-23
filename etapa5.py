
# Aquecimento para a Formação em Infraestrutura de Dados | Escritório de Dados

# Etapa 5: Analisando dados com agrupamento 📊

# Rodrigo Abreu Carvalho

""" 
Objetivo: utilizar técnicas de agrupamento para descobrir usuários que moram 
no mesmo país e estado. 

Descrição da solução: uma função que recebe, como parâmetro, um pandas.DataFrame 
e retorna um pandas.DataFrame com as mesmas colunas, mas com os dados agrupados 
por país e estado. 

"""

import requests

import json

import csv

import pandas 

def my_function(n):
    urln = "https://randomuser.me/api/?inc=gender,location,dob&format=csv&results=" + str(n)
    table = pandas.read_csv(urln)
    table = table.groupby(['location.state', 'location.country'])[['dob.age']].mean()
    print(table)

my_function(n = 500)
  


