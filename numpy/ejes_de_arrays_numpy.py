# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/l0dAuuNZZvg

"""

import numpy as np

altura_y_pesos = np.array([[ 1.74, 91.40 ],
                           [ 1.80, 88.70 ],
                           [ 1.78, 87.30 ],
                           [ 1.68, 62.70 ],
                           [ 1.78, 81.60 ]])

print("Minimo", altura_y_pesos.min())
print("Maximo", altura_y_pesos.max())
print("Pos Min", altura_y_pesos.argmin())
print("Pos Max", altura_y_pesos.argmax())
print("Suma", altura_y_pesos.sum())
print("Promedio", altura_y_pesos.mean())

print("Minimo", altura_y_pesos.min(axis=1))
print("Maximo", altura_y_pesos.max(axis=1))
print("Pos Min", altura_y_pesos.argmin(axis=1))
print("Pos Max", altura_y_pesos.argmax(axis=1))
print("Suma", altura_y_pesos.sum(axis=1))
print("Promedio", altura_y_pesos.mean(axis=1))