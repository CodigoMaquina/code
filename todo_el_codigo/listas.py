# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/WCfR0nWOKdU
"""

edades = [13, 45, 23, 13]
print(edades[0])
print(edades[2])
edades[2]=33
print(edades)
print(edades[0:2])
print(edades[:2])
print(edades[2:])
print(len(edades))
print(max(edades))
print(min(edades))
print(sum(edades))
print(sum(edades)/len(edades))
edades.insert(2, 50)
print(edades)
edades.append(55)
print(edades)
edades.extend([56])
print(edades)
edades.extend([80, 88])
print(edades)
del edades[1]
print(edades)
edades.remove(50)
print(edades)
edades.pop()
print(edades)
print(edades.count(33))
print(edades.count(13))
print(edades.index(55))
print(edades.sort())
edades.reverse()
print(edades)
persona1 = ["Juan", 44]
print(persona1[0])
print(persona1[1])
persona2 = ["Maria", 30]
personas = [persona1, persona2]
print(personas[0])
print(personas[1])
print(personas[0][0], personas[0][1])











