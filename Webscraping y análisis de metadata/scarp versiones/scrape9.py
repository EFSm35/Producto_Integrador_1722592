# -*- coding: utf-8 -*-

"""
Created on Mon May 29 2023
Script: Scrape9
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
# Buscar todos los elementos que el h2 contenga en su texto
# la palabra "python"
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
    )
# Buscamos cada elemento que tenga referencia de python_jobs
# Y almacernarlo en python_jobs_elements
python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
    ]
#Mostramos informacion de python_jobs_elements
for job_element in python_jobs_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()