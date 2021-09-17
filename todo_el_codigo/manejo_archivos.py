# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/bf_698bfPDU

"""

def escribir(nombre, texto):
    with open(nombre, "w") as archivo:
        archivo.write(texto)

def leer(nombre):
    texto=""
    with open(nombre, "r") as archivo:
        texto = archivo.read()
    return texto

if __name__ == "__main__":
    escribir("prueba.txt", "Un texto cualquiera")
    print(leer("prueba.txt"))