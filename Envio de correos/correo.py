# -*- coding: utf-8 -*-
"""
Created on Tue May  2 18:13:54 2023
script:correo.py
@author: edo-s
Nommbre: Eduardo Flores Smith
Matricula: 1722592
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Datos del remitente
correo = "Insertar correo"
contraseña = "Insertar contraseña"

# Datos del destinatario
destinatario = "correoelectronico"


# mensaje de correo electrónico
mensaje = MIMEMultipart()
mensaje["From"] = correo
mensaje["To"] = destinatario
mensaje["Subject"] = f"Prueba de envío (script Python) - 1722592"

# cuerpo del mensaje como texto HTML
cuerpo = MIMEText(f"""
<html>
  <body>
    <p><font size="5"><b>Actividad 12</b></font></p>
    <p>Ejercicio de la practica 12 para envío de correos</p>
    <p><b>Alumno:</b> Eduardo Flores Smith</p>
    <p><b>Matrícula:</b> 1722592</p>
  </body>
</html>
""", "html")
mensaje.attach(cuerpo)

# imagen como archivo adjunto
with open("fcfm_cool.png", "rb") as archivo_imagen:
    imagen = MIMEImage(archivo_imagen.read())
    imagen.add_header("Content-Disposition", "attachment", filename="FCFM_COOL.jpg")
    mensaje.attach(imagen)

# Enviar el correo electrónico
with smtplib.SMTP("smtp.gmail.com", 587) as servidor_smtp:
    servidor_smtp.ehlo()
    servidor_smtp.starttls()
    servidor_smtp.login(correo, contraseña)
    servidor_smtp.sendmail(correo, destinatario, mensaje.as_string())
    print("Correo electrónico enviado con éxito.")
