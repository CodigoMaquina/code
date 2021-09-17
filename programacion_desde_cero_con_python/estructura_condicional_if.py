# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/AaeVXnf-xno
"""

artes = False
deportes = True
matematicas = True

if artes:
    print("Estudia Teatro")
    
if deportes:
    print("Estudia Medicina Deportiva")
    
if matematicas:
    print("Estudia Matemáticas")
    
if artes and matematicas:
    print("Estudia Arquitectura")
    
if artes or matematicas:
    print("Estudia Arquitectura")
    
if artes and not matematicas:
    print("Estudia Pintura")
    
edad = 15

if edad >= 10 and edad <= 14:
    print("Equipo Juvenil A")
elif edad > 14 and edad <= 17:
    print("Equipo Juvenil B")
elif edad == 18:
    print("Equipo profesional")
else:
    print("Eres demasiado pequeño o demasiado grande para el club juvenil")
    

        