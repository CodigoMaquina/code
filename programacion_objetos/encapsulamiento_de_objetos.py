# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/5kMOFIOWKvs

"""

class Cuenta:
    
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.__balance = 0.00
    
    def retirar(self, monto):
        if self.__balance >= monto:
            self.__balance -= monto 
    
    def depositar(self, monto):
        if monto > 0:
            self.__balance += monto
        
    
        
        