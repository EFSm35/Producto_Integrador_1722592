# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:46:57 2023
Script:nmapactivad11
@author: edo-s
Matricula:1722592
Nombre:Eduardo Flores Smith
"""

import nmap

scanner = nmap.PortScanner()

def scan_udp():
    ip = input("Introduce la dirección IP a escanear: ")
    print("Escaneando la dirección: ", ip)
    scanner.scan(ip, arguments='-sU -p 1-65535')
    for port in scanner[ip]['udp'].keys():
        print("Puerto UDP {} abierto".format(port))

def scan_completo():
    ip = input("Introduce la dirección IP a escanear: ")
    print("Escaneando la dirección: ", ip)
    scanner.scan(ip, arguments='-p 1-65535 -sS -sV -O')
    print(scanner[ip].all_protocols())
    for port in scanner[ip]['tcp'].keys():
        print("Puerto TCP {} abierto".format(port))

def deteccion_sistema_operativo():
    ip = input("Introduce la dirección IP a escanear: ")
    print("Escaneando la dirección: ", ip)
    scanner.scan(ip, arguments='-O')
    print("El sistema operativo detectado es: ", scanner[ip]['osmatch'][0]['name'])

def escaneo_red_ping():
    ip = input("Introduce la dirección de red a escanear (ej. 192.168.1.0/24): ")
    print("Escaneando la red: ", ip)
    scanner.scan(ip, arguments='-sn')
    for host in scanner.all_hosts():
        print("Host %s está %s" % (host, scanner[host].state()))

while True:
    print("""
    Seleccione una opción:
    1. Escaneo UDP
    2. Escaneo Completo
    3. Detección de sistema operativo
    4. Escaneo de red con ping
    5. Salir
    """)

    opcion = input("Introduzca una opción: ")
    
    if opcion == "1":
        scan_udp()
    elif opcion == "2":
        scan_completo()
    elif opcion == "3":
        deteccion_sistema_operativo()
    elif opcion == "4":
        escaneo_red_ping()
    elif opcion == "5":
        break
    else:
        print("Opción inválida, por favor seleccione una opción válida.")
