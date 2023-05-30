# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 20:06:13 2023
script:scan_portv2
@author: edo-s
nombre: Eduardo Flores Smith
Matricula: 1722592
"""

import socket
#part2
def scan (addr,port):
    socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result=socket_obj.connect_ex((addr,port))
    socket_obj.close()
    
    return result
#part3
ports=[21,22,25,80]
#port4
for i in range(1,225):
    addr="192.168.0.{}".format(i)
    for port in ports:
        result=scan(addr,port)
        if result==0:
            print(addr,port,"OK")
        else:
            print(addr,port,"Failed")
            