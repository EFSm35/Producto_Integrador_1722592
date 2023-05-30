# -*- coding: utf-8 -*-
"""
Created on Mon May 29 2023
Script: Scrape2
@author: Eduardo Flores Smith
Matricula:1722592
"""
#importacion de modulogs
import requests
from bs4 import BeautifulSoup
# Obtencion de los datos mediante peticion GET
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#Analizamos el contenido HTML con BeaitifulSoup
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# Formateamos la salida del objeto results de BeautifulSoup
print(results.prettify())