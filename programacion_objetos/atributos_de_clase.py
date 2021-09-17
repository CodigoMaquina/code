# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/CpgxlrImUhk

"""

class Vehiculo:
    
    folio = 0
    COLORES = ("BLANCO", "ROJO", "VERDE") 
    
    def __init__(self, color):
        Vehiculo.folio += 1
        self.serie = Vehiculo.folio
        self.set_color(color)
    
    def __str__(self):
        return str(self.serie) + " " + self.color
    
    def set_color(self, color):
        color = color.upper().strip()
        if color in Vehiculo.COLORES:
            self.color = color
        else:
            self.color = Vehiculo.COLORES[0] #default

vehiculo_a = Vehiculo("Rojo ")
vehiculo_b = Vehiculo(" Azul")

print(vehiculo_a)
print(vehiculo_b)