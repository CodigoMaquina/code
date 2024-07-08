# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/aVN2wp1Oosk

"""

def doblar(referencia, valor):
    referencia *= 2
    valor *= 2
    print ("DURANTE", referencia, valor)

estructura = ["a", "b", "c"]
primitiva = "abc"

print("ANTES", estructura, primitiva)
doblar(estructura, primitiva)
print("DESPUES", estructura, primitiva) 