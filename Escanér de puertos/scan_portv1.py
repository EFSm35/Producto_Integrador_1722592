# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:36:03 2023
script:scan_portv1
@author: edo-s

nombre: Eduardo Flores Smith
Matricula: 1722592
"""

import sys
from socket import *
#parte2
host= sys.argv[1]
portstrs=sys.argv[2].split("-")
#part3
start_port=int(portstrs[0])
end_port=int(portstrs[1])
#part4
target_ip=gethostbyname(host)
opened_ports=[]
#part5
for port in range (start_port, end_port):
    sock=socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result=sock.connect_ex((target_ip, port))
    if result ==0:
        opened_ports.append(port)
print("opened ports: ")
for i in opened_ports:
    print(i)