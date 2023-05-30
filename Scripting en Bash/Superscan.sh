#!/bin/bash
#
# Script superscan.sh
# 28/05/2023 - Eduardo Flores Smith
#
# Ejemplo de Menú en BASH

date
echo "|"
echo "|---------------------------|"
echo "|   Menu Principal          |"
echo "|---------------------------|"
echo "|1. Netdiscover"
echo "|2. Portscanv1"
echo "|3. Welcome"
echo "|4. Exit"
echo "|"
read -p "Opción  [ 1 - 4 ] " c

case $c in
  1) /home/edsmith/Scripting/netdiscover.sh ;;
  2) read -p "Ingresa el comando para Portscanv1: " comando
     /home/edsmith/Scripting/portscanv1.sh $comando ;;
  3) /home/edsmith/Scripting/welcome.sh ;;
  4) echo "¡Adiós!"; exit 0 ;;
esac
