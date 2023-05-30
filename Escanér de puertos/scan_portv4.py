# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:11:08 2023
script:scan_portv4
@author: edo-s
Nombre: Eduardo Flores smith
matirucla1722592
"""

import nmap
escaner = nmap.PortScanner()

escaner.scan('192.168.138.1', '1-1024', '-v -sV' )
escaner.command_line()
escaner.all_hosts()
escaner['192.168.138.1'].state()
escaner['192.168.138.1'].all_protocols()
escaner['192.168.138.1']['tcp'].keys()
escaner['192.168.138.1'].has_tcp(21)
escaner['192.168.138.1'].has_tcp(22)
escaner['192.168.138.1']['tcp'][135]
escaner['192.168.138.1']['tcp'][135]['product']