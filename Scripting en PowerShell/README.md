# Producto_Integrador_1722592

# Sección Scripting en Powershell
Este repositorio contiene scripts de extracción de datos en sitos web desarrollados en Python. Estos scripts utilizan la biblioteca BeautifulSoup para analizar el contenido HTML y obtener la información deseada.

## Scripts incluidos
# [scan_alivev1.py](https://github.com/EFSm35/Producto_Integrador_1722592/blob/main/Scripting%20en%20PowerShell/scan_alivev1.ps1)
### El objetivo de este script es realizar un escaneo de equipos activos en una subred utilizando powershell.

### Funcionamiento
- Determina el gateway de la subred actual.
- Calcula el rango de la subred.
- Verifica si el rango de subred termina en un punto y lo corrige si es necesario.
- Crea un array con 254 números del 1 al 254 y los almacena en la variable $rango_ip.
- Realiza un bucle foreach para validar los hosts activos en la subred.
- Utiliza el cmdlet Test-Connection para verificar la conectividad con cada dirección IP en el rango.
- Muestra en pantalla los hosts que responden a la prueba de conexión.

# [scan_alivev2.py](https://github.com/EFSm35/Producto_Integrador_1722592/blob/main/Scripting%20en%20PowerShell/scan_alivev2.ps2)
### El propósito de este script es realizar un escaneo de equipos activos en la subred. Este script proporciona una presentación más clara de la información encontrada por el script.
### Esto se logra utilizando una combinación de mensajes de texto y los cmdlets Write-Host y Write-Output para imprimir información en la consola. Además de determinar el gateway y generar el rango de subred, se muestra en pantalla la subred actual y el rango de subred a escanear. Luego, se realiza el escaneo de los hosts activos y se muestra en pantalla cada host que responde a la prueba de conexión.

### Funcionamiento
- Determina el gateway de la subred actual.
- Calcula el rango de la subred.
- Verifica si el rango de subred termina en un punto y lo corrige si es necesario.
- Crea un array con 254 números del 1 al 254 y los almacena en la variable $rango_ip.
- Realiza un bucle foreach para validar los hosts activos en la subred.
- Utiliza el cmdlet Test-Connection para verificar la conectividad con cada dirección IP en el rango.
- Muestra en pantalla los hosts que responden a la prueba de conexión.

# [scan_portv1](https://github.com/EFSm35/Producto_Integrador_1722592/blob/main/Scripting%20en%20PowerShell/scan_portv1.ps1)
### El propósito de este script es realizar un escaneo de los puertos más comunes en equipos de la misma subred.

### Funcionamiento
- Determina automáticamente el gateway de la subred actual.
- Calcula el rango de la subred basado en el gateway.
- Verifica si el rango de subred termina en un punto y lo corrige si es necesario.
- Define un array con los puertos a escanear.
- Establece una variable de tiempo de espera ($waittime).
- Solicita la dirección IP a escanear al usuario.
- Utiliza un bucle foreach para evaluar cada puerto en la lista $portstoscan.
- Utiliza el objeto System.Net.Sockets.TcpClient para intentar la conexión a cada dirección IP y puerto especificados.
- Muestra en pantalla los puertos que están abiertos en la dirección IP especificada.

## Autor

Este script fue desarrollado por [EFSm35](https://github.com/EFSm35).
