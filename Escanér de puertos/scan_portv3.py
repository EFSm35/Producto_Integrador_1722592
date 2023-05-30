# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 20:31:50 2023
script:scan_portv3
@author: edo-s
nombre: Eduardo Flores Smith
Matricula: 1722592
"""

import sys
import threading
from socket import *

#part2
def tcp_test(port):
    sock=socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result=sock.connect_ex((target_ip, port))
    if result==0:
        print("Opened Port:",port)
#port3
if __name__=="__main__":
    host=sys.argv[1]
    portstrs=sys.argv[2].split("-")
#part4
start_port=int(portstrs[0])
end_port=int(portstrs[1])
#part5
target_ip=gethostbyname(host)
#part6
hilos=[]
for port in range(start_port, end_port):
    hilo=threading.Thread(target=tcp_test, args=(port,))
    hilos.append(hilo)
    hilo.start()