# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/Oy9vWWss1n4

"""

"""
    CASO BASE: El caso más simple o el último caso.
    
    CASO RECURSIVO: La función se llama a sí misma, pero resolviendo
                    un problema menor.
"""
"""
0! =                    = 1
1! = 1                  = 1
2! = 1 * 2              = 2
3! = 1 * 2 * 3          = 6
4! = 1 * 2 * 3 * 4      = 24
5! = 1 * 2 * 3 * 4 * 5  = 120

factorial(n) = n*factorial(n-1)

"""

def factorial_iterativo(n):
    if n == 0 or n == 1: 
        return 1
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    if n == 0 or n == 1: # Caso base
        return 1
    return n*factorial_recursivo(n-1) # caso recursivo 
    
for i in range(6):
    print (i,factorial_iterativo(i), factorial_recursivo(i))
    
from time import perf_counter

inicio = perf_counter()
for i in range(1000000):
    factorial_iterativo(100)
fin = perf_counter()
print ("Iterativo %0.4f" % (fin-inicio)) 

inicio = perf_counter()
for i in range(1000000):
    factorial_recursivo(100)
fin = perf_counter()
print ("Recursivo %0.4f" % (fin-inicio)) 
    


