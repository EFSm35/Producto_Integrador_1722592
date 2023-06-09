# -*- coding: utf-8 -*-
"""
Created on Mon May 29 2023
Script: scrap 4
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
# En el objeto job_elemento buscamos solo aquellos elementos con
#titulo e informacion relevante
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()
