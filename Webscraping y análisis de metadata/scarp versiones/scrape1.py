# -*- coding: utf-8 -*-
"""
Created on Mon May 29 2023
Script: Scrape1
@author: Eduardo Flores Smith
Matricula:1722592
"""
#importar modulos
import requests
# Obtener la informacion HTML de la URL
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
# Imprimir el texto de la peticion GET
print(page.text)

