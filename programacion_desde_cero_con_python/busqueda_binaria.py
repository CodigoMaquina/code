# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/Ds61hiuBcOk

"""

"""

[11     12      13      14      15      16      17]  dato = 15
bajo                   centro                   alto  centro =(bajo+alto)//2
                                                      lista[centro]<15 - der

[11     12      13      14      15      16      17]  dato = 15
                               bajo    centro   alto  centro =(bajo+alto)//2
                                                      lista[centro]>15 - izq
[11     12      13      14      15      16      17]  dato = 15
                               bajo                  centro =(bajo+alto)//2
                               alto        
                               centro        
"""

def busqueda_iterativa(lista, dato):
    bajo = 0
    alto = len(lista) - 1
    centro = (bajo + alto) // 2
    while bajo <= alto:
        if lista[centro] == dato:
            return centro
        elif lista[centro] < dato:
            bajo = centro + 1
        else: 
            alto = centro - 1
        centro = (bajo + alto)//2
    return -1 # Que no existe

lista = [11, 12, 13, 14, 15, 16, 17]

def busqueda_recursiva(lista, bajo, alto, dato):
    if bajo > alto: #caso base
        return -1
    centro = (bajo+alto) // 2  # caso recursiva
    if lista[centro] == dato:
        return centro
    elif lista[centro] < dato:
        return busqueda_recursiva(lista, centro + 1, alto, dato)
    else:
        return busqueda_recursiva(lista, bajo, centro - 1, dato)
        

for i in range(10, 19):
    print(i, busqueda_iterativa(lista, i))
    print(i, busqueda_recursiva(lista, 0, len(lista)-1, i))
  
