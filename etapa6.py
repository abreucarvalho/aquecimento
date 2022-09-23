
# Aquecimento para a Formação em Infraestrutura de Dados | Escritório de Dados

# Etapa 6 (opcional): Particionando dados 🎼

# Rodrigo Abreu Carvalho

""" 
Objetivo: realizar o particionamento dos dados em formato Hive¹ utilizando as 
informações de país e estado de cada usuário.

Descrição da solução: uma função que recebe, como parâmetro, um pandas.DataFrame 
e salva todos os dados em arquivos CSV particionados por país e estado.

¹. The Apache Hive ™ data warehouse software facilitates reading, writing, and 
managing large datasets residing in distributed storage using SQL. Structure 
can be projected onto data already in storage. A command line tool and JDBC 
driver are provided to connect users to Hive.

"""

from pyhive import hive

import requests

import json

import csv

import pandas 

conn = hive.Connection(host='192.168.1.196', port='10000', database='default', auth='NONE')


def my_function(n):
    urln = "https://randomuser.me/api/?inc=gender,location,dob&format=csv&results=" + str(n)
    table = pandas.read_csv(urln)
    table = table.groupby(['location.state', 'location.country'])[['dob.age']].mean()
    print(table)

my_function(n = 500)

