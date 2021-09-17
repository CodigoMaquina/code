# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/d1Tl2ZDV0Cc

"""

def suma_dos_numeros(a, b):
    suma = a + b
    return suma

def suma_muchos_numeros(*numeros):
    suma = 0
    for numero in numeros:
        suma = suma + numero
    return suma

# nombre = "JUAN"
# paterno = "HERNANDEZ"
# materno = "JIMENEZ"

# JUAN Hernadez Jimenez

def formatea_nombre(nombre, paterno, materno):
    formato = nombre.upper()+" "+ paterno.capitalize()+" "+ materno.capitalize()
    return formato
    

# nombre = "JUAN HERNANDEZ JIMENEZ"
# fecha_nacimiento = 1980

# clave -> JHJ80

def crea_clave(nombre, fecha_nacimiento):
    clave = ""
    for vocablo in nombre.split():
        clave = clave + vocablo[0]
    fecha_nacimiento = str(fecha_nacimiento)
    return clave+fecha_nacimiento[-2:]

print (crea_clave("JUAN HERNANDEZ JIMENEZ", 1980))











    