# %%

# Aquecimento para a Formação em Infraestrutura de Dados | Escritório de Dados

# Etapa 7: Parametrizando seu código ⚙️

# Rodrigo Abreu Carvalho

""" 
Objetivo: nessa etapa, você deve parametrizar seu código para que ele seja 
executado com valores diversos fornecidos pelo usuário.

Descrição da solução: a solução dessa etapa consiste em uma função principal 
que recebe diversos parâmetros e executa as diversas etapas descritas 
anteriormente em função dos parâmetros fornecidos. Note que essa etapa é 
crucial para que seu código se torne reutilizável.

Dicas:
Tente pensar no maior número de parâmetros que sejam relevantes para sua 
pipeline de dados, sem afetar sua funcionalidade.

Colocar valores padrão para alguns desses parâmetros reduz o ônus do usuário 
de preenchê-los por conta própria.

"""
from pyhive import hive

import matplotlib.pyplot as plt

import requests

import json

import csv

import pandas 

def my_function(n = 500, min_age = 20, max_age = 80, bins = 60, dpi = 300):
    url = "https://randomuser.me/api/?format=csv&results=" + str(n)
    table = pandas.read_csv(url)
    table.columns = table.columns.str.replace('\.', '_')
    with open("etapa7.txt", "a") as f:
        print((table.groupby('gender')['gender'].count() / len(table.index) * 100), file=f)
        print((table.groupby('nat')['nat'].count() / len(table.index) * 100), file=f)
    table.plot.hist(column=['dob_age'], bins = 60, range=(min_age, max_age), alpha=.5).set_xlabel('age (years)')
    plt.savefig('hist7.png', dpi = dpi, bbox_inches = 'tight')
 
my_function(min_age = 40, max_age = 80, bins = 40,)


# %%
