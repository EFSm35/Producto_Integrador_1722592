# -*- coding: utf-8 -*-
"""
Created on Mon May 29 2023
script: scrape_quote
@author: Eduardo Flores Smith
Matricula:1722592
"""
#Importar modulos
import requests
import csv
from bs4 import BeautifulSoup
# Direccion de la pagina web
url = "http://quotes.toscrape.com/"
# Ejecutar GET-Request
response = requests.get(url)
#Analizar sintacticamente el archivo HTML de BeutifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')
#Extraer todas las citas y autores del archivo HTML
quotes_html = html.find_all("span", class_="text")
authors_html = html.find_all("small", class_="author")
#Crear una lista de las citas
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)
# Crear una lista de los auotes
authors = list()
for author in authors_html:
    authors.append(author.text)
# Para hacer el test: combinar y mostrar las entradas de ambas listas
for t in zip(quotes, authors):
    print(t)
# Guardar las citas y los auotores en un archivo CSV en el directorio actual
# Abrir el archivo con Excel / Libre office, etc.
with open('./citas_1722592.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))