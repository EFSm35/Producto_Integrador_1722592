# -*- coding: utf-8 -*-
"""
Created on Mon May 29 2023
Script: Scrape3
@author: Eduardo Flores Smith
Matricula:1722592
"""

#importacion de modulogs
import requests
from bs4 import BeautifulSoup
# Obtencion de los datos mediante peticion GET
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# Analizamos el contenido HTML con BeautifulSoup
soup= BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# Buscar todos los elementos que el class "card-content"
job_elements = results.find_all("div", class_="card-content")
# Por cada elemento encontrado job_element imprimimos.
for job_element in job_elements:
    print(job_element, end="\n"*2)