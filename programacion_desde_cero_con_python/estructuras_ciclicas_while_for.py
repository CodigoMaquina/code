# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/JP7ljJe-rAQ

"""


contador = 0

while contador < 10:
    print("Iteración", contador)
    contador += 1
    
print("Termina Ejecución")

total = 0
num_sumas = 5
contador = 0

while contador < num_sumas:
    num = int(input("Ingresa un número: "))
    total = total + num
    contador +=1
    
print("El total de la suma es", total)    

autorizacion = False

while autorizacion == False:
    contrasena = input("Ingresa tu contraseña: ")
    if contrasena == "123456" :
        autorizacion = True
    else:
        print("Acceso denegado")

print("Ingresé al sistema exitosamente")

for numero in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("Iteración", numero)
    
print("-----")

for numero in [33, 45, 25, 23, 55]:
    print("Número", numero)
  
print("-----")

colores = ["rojo", "verde", "amarillo", "azul"]

for color in colores:
    print("Hay pintura color:", color)
    
indice = 0
while indice < len(colores):
    print("Hay pintura color:", colores[indice])
    indice +=1

print("-----")

for numero in range(10):
        print("Iteración", numero)

print("-----")

for numero in range(5, 10):
        print("Iteración", numero)
    
    


