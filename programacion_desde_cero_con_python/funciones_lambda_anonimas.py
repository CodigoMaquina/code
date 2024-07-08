# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/BY0uu-ueisM

"""

suma = lambda a, b : a + b 
multiplicacion = lambda a, b, c : a * b * c
constante = lambda : 10

print(suma(2,3), multiplicacion(2,3,4), constante())

personas = [("Juan", 82, 5), ("Luisa", 41, 10), ("Arnulfo", 75, 20)]

print("Desordenada", personas)
personas.sort()
print("Ordenada por nombre", personas)
personas.sort(key=lambda persona : persona[1]) # Edad
print ("Ordenada por edad",personas)
personas.sort(key=lambda persona : persona[1]+persona[2])
print ("Ordenada edad+credito", personas)


