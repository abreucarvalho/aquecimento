# %%

# Aquecimento para a Formação em Infraestrutura de Dados | Escritório de Dados

# Etapa 4: Analisando dados sem agrupamento 📊

# Rodrigo Abreu Carvalho


""" 
Objetivo: com seus dados devidamente tratados, você deve gerar os seguintes itens:
    Um relatório em texto (não precisa de formatação) contendo:
        
        A porcentagem dos usuários por gênero

        A porcentagem dos usuários por país

    Uma imagem contendo um gráfico de distribuição da idade dos 
    usuários (a biblioteca utilizada para o plot pode ser qualquer uma).

Descrição da solução: uma função que recebe, como parâmetro, um pandas.DataFrame 
e gera dois arquivos: um relatório em texto e outro contendo um gráfico de 
distribuição da idade dos usuários.

"""

import matplotlib.pyplot as plt

import requests

import json

import csv

import pandas 

def my_function(url, n):
    urln = url + '&results=' + str(n)
    table = pandas.read_csv(urln)
    table.columns = table.columns.str.replace('\.', '_')
    with open("etapa4.txt", "a") as f:
        print((table.groupby('gender')['gender'].count() / len(table.index) * 100), file=f)
        print((table.groupby('nat')['nat'].count() / len(table.index) * 100), file=f)
    table.plot.hist(column=['dob_age'], bins = 60, range=(20, 80), alpha=.5).set_xlabel('age (years)')
    plt.savefig('plot.png', dpi=300, bbox_inches='tight')

 
my_function(url = "https://randomuser.me/api/?format=csv", n = 500)

# %%
