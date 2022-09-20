
# Aquecimento para a Formação em Infraestrutura de Dados | Escritório de Dados

# Etapa 2: Coletando dados 💾

# Rodrigo Abreu Carvalho

""" 
Objetivo: nessa etapa, você deve coletar dados da API e armazená-los em um arquivo CSV.

Descrição da solução: a solução dessa etapa consiste em uma função para coletar uma 
quantidade n de dados da API (sendo n um valor fornecido via parâmetro da função), 
manipulá-los para montar um pandas.DataFrame e salvar o resultado em um arquivo CSV. 

"""

import requests

import json

import csv

import pandas 

def my_function(url, n):
    urln = url + '&results=' + str(n)
    table = pandas.read_csv(urln)
    table.columns = table.columns.str.replace('\.', '_')
    table.to_csv('etapa2_table.csv', encoding = 'utf-8')

my_function(url = "https://randomuser.me/api/?format=csv", n = 500)
