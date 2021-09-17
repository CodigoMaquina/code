# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/Qc0qD00RmRA

"""

from random import randint

class Tragamonedas:
    
    def __init__(self, id, premio):
        self.id = id
        self.premio = premio
        self.monedas = 0
        self.jackpots = 0
        
    def __str__(self):
        return "Id: "+ str(self.id) + " - Premio: " + str(self.premio) 
    
    def __eq__(self, otro):
        return self.monedas == otro.monedas
    
    def __lt__(self, otro):
        return self.monedas < otro.monedas
    
    def __gt__(self, otro):
        return self.monedas > otro.monedas    
        
    def jugar(self):
        self.monedas += 1
        numeros = randint(0, 9), randint(0, 9), randint(0, 9)
        mensaje = "" 
        if numeros[0] == numeros[1] == numeros[2]:
            self.jackpots += 1
            mensaje = "Felicidades !!! Ganaste %0.2f" % self.premio 
        else:
            mensaje = "Mejor suerte para la próxima"
        return numeros, mensaje
    
tragamonedas_a = Tragamonedas(1, 1000)
tragamonedas_b = Tragamonedas(1, 1000)


for i in range(100):
    print(tragamonedas_a.jugar())
    print(tragamonedas_b.jugar())




            
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
        

