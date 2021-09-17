# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/8FjY7_mhuqM

"""

class Producto:
    
    def __init__(self, id, descripcion, costo):
        self.id = id
        self.descripcion = descripcion
        self.costo = costo
        
    def crear_etiqueta(self):
        return " %s \n %s \n %0.2f" % (self.id, 
                                       self.descripcion, 
                                       self.costo)
    
class Electronico(Producto):
    
    def __init__(self, id, descripcion, costo, marca):
        super().__init__(id, descripcion, costo)
        self.marca = marca
        
class Perecedero(Producto):

    def __init__(self, id, descripcion, costo, caducidad):
        super().__init__(id, descripcion, costo)
        self.caducidad = caducidad
        
    def crear_etiqueta(self):
        return super().crear_etiqueta()+ "\n %s" % self.caducidad


productos = (Producto("g", "Producto", 100),
             Perecedero("p", "Tomates", 200, "01/01/2022"),
             Electronico("e", "Electrónico 1", 300, "Sony"))     

for objeto  in productos:
    print ("*****")
    print (objeto.crear_etiqueta())
    
    
    

        





    