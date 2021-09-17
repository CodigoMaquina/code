# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/JQTZB979H1A

"""

archivo = open("datos.txt", "r", encoding="utf-8")

lineas = archivo.readlines()

for linea in lineas:
    print(linea.strip())

archivo.close()

archivo = open("personas.txt", "a", encoding="utf-8")
archivo.write("Juan Hernández 18\n")
archivo.write("Eulalio Pérez 20\n")
archivo.close()

with open("personas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Juan Hernández 18\n")
    archivo.write("Eulalio Pérez 20\n")

pasajeros = {}
with open("datos_metro.csv", "r", encoding="utf-8") as archivo:
    archivo.readline()
    estaciones=archivo.readlines()    
    for estacion in estaciones:
        estacion = estacion.strip().split(",");
        pasajeros[estacion[0]]= list(map(int, estacion[1:]))
    
print(pasajeros)

        
    
    
    

















