# Producto_Integrador_1722592
# Repositorio de Prácticas

Este repositorio contiene las prácticas realizadas por Eduardo Flores Smith | Matricula:1722592.

## Secciones

- [Scripting en PowerShell](vinculo)
- [Scripting en Bash](vinculo)
- [Webscraping](vinculo)
- [Escáner de Puertos](vinculo)
- [Envío de Correos](vinculo)

-Cada sección contendrá sus README correspondientes.

## Scripting en PowerShell
En esta sección, se presentan algunos scripts de powershell los cuales analizan la subred del equipo.

### -scan_alive1.ps1
Este script utiliza powershell para determinar los equipos activos en la subred y mostrar los que responden.

### -scan_alive2.ps1
Este script utiliza powershell para determinar los equipos activos en la subred y mostrar los que responden. Tiene la misma función que el primero pero este tiene diferente presentación.

### -scan_portv1
Este script de powershell tiene como objetivo escanear los puertos más comunes en equipos de la misma subred.

## Scripting en Bash
En esta seccion vemos diferentes scripts que realizan diversas tareas desde escanear puertos hasta cosas sencillas como mensajes personalizados para el usuario.

### -bro.sh
Este script interactivo de Bash le pide al usuario que ingrese su nombre y luego muestra un mensaje de saludo personalizado.

### -netdiscover.sh
Este script en Bash realiza un escaneo de red para descubrir hosts que responden en el segmento de red del dispositivo.

### -number.sh
Este script en Bash lee tres números proporcionados por el usuario y los muestra en la salida.

### -portscanv1.sh
Este script en Bash realiza un escaneo de puertos en una dirección IP especificada utilizando un archivo especial en `/dev`.

### -welcome.sh
Este script en Bash muestra un mensaje de bienvenida al usuario y muestra información sobre los usuarios actuales conectados y sus procesos.

### -Superscan.sh
Este script en Bash muestra un menú interactivo, que le permite al usuario, utilizar algunos de los scripts de esta sección

## Webscraping

En esta sección encontrarás scripts que te permitirán realizar webscraping y extraer datos de sitios web. Estos scripts utilizan la biblioteca BeautifulSoup para analizar el contenido HTML y obtener la información deseada.

### -scrap12.py

- [Scrape12](./webscraping/scrap_12.py): Este script realiza el webscraping del sitio web: https://realpython.github.io/fake-jobs/ donde extrae información específica de los trabajos relacionados con Python.

### -scrape__quote.py
- [ScrapeQuote](./webscraping/scrape_quote.py): Este script realiza el webscraping del sitio web: http://quotes.toscrape.com dónde extrae citas y autores para guardarlos en un archivo CSV.

## Escáner de Puertos

Esta sección contiene varios scripts en Python para realizar escaneos de puertos utilizando princpualmente las bibliotecas `nmap` y `socket`.

### -nmapactivad11.py

El script `nmapactivad11.py` permite realizar diferentes tipos de escaneos de puertos utilizando la biblioteca `nmap`. A continuación, se describen las opciones disponibles:

1. **Escaneo UDP**: Escanea una dirección IP en busca de puertos UDP abiertos.
2. **Escaneo Completo**: Realiza un escaneo completo de una dirección IP, incluyendo puertos TCP y UDP, con detección de servicios y sistema operativo.
3. **Detección de sistema operativo**: Escanea una dirección IP para determinar el sistema operativo utilizado.
4. **Escaneo de red con ping**: Escanea una red especificada por su dirección de red (ejemplo: 192.168.1.0/24) utilizando ping para determinar la disponibilidad de los hosts.

### -scan_portv1.py

El script `scan_portv1.py` permite realizar un escaneo de puertos en un host específico utilizando sockets en Python.

### -scan_portv2.py

El script `scan_portv2.py` permite realizar un escaneo de puertos en una lista de puertos predefinidos en un rango de direcciones IP utlizando la bibloteca `socket`.

### -scan_portv3.py

El script `scan_portv3.py` permite realizar un escaneo de puertos en un rango específico de puertos en un host utilizando `socket`  y `threading`en Python.

### -scan_portv4.py

El script `scan_portv4.py` utiliza la biblioteca `Nmap` para realizar un escaneo de puertos en un host específico.


## Envío de Correos

Esta sección contiene un script en Python llamado `correo.py` que permite enviar correos electrónicos utilizando el módulo `smtplib` de Python.

### -correo.py
El script incluye la configuración del remitente y destinatario del correo, así como un mensaje de correo electrónico con formato HTML y una imagen adjunta.
