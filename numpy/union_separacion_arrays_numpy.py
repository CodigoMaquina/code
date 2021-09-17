# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/E1i8fVEfMOo

"""

import numpy as np

altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78])

peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6])

union = np.stack((altura, peso), axis=0)

print(union, type(union))

print()

separados = np.split(union, 2)

print(separados, type(separados))










