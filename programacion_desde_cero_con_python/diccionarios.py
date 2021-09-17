# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/YK1aKWAdeyc

"""

"""
PERSONA
Llaves: nombre, edad, direccion, altura, peso
valores: Juan, 33, Reforma 333, 1.70, 80
"""
persona = { "nombre":"Juan", "edad":33, "direccion":"Reforma 333"}

print(persona["edad"])
print(persona.get("edad"))

for valor in persona.values():
    print(valor)
    
for llave in persona.keys():
    print(llave)    
    
for elemento in persona.items():
    print(elemento)

for llave, valor in persona.items():
    print(llave, valor)
    
persona["direccion"] = "Reforma 300"

persona.update({"direccion":"Reforma 200", "altura":1.70})

persona["peso"] = 80

persona.pop("peso")

texto= "Un alunizaje del tipo que tuvieron las misiones Apolo se inicia a los 110 km de altura, separándose entonces el módulo de descenso ocupado por el comandante de la expedición y el piloto del LEM. Al cabo de media revolución, el motor de descenso entra en ignición, que disminuye la velocidad de la nave situándola en una órbita elíptica de 110 x 15 km. Una vez alcanzada esta órbita, se vuelve a encender el motor de descenso, reduciendo la velocidad del módulo lunar hasta alcanzar los 35 m/s estando en ese momento la altura controlada constantemente por el radar de aterrizaje. Existen dos puntos importantes de control en la fase de alunizaje llamados puerta alta y puerta baja. Tras finalizar la fase de frenado, la altura del módulo es de 3 metros (aproximadamente 10 pies), el ángulo de inclinación del mismo es de 23° y el empuje entonces es de 2721 kgf. En los alunizajes se han dejado instrumentos en la superficie lunar, como este retroreflector para medir con precisión la distancia Tierra-Luna mediante láser. Cuando se avista el punto de descenso, el módulo se encuentra a una altitud de 2950 metros, funcionando el retrocohete con un empuje de 2540 kgf. mientras la nave presenta una inclinación de 49°. La primera fase consiste en pasar a una distancia sobre la superficie lunar de unos 2300 metros y a una distancia de entre 4 y 8 kilómetros del punto de descenso y a una velocidad de traslación de unos 150 m/s, habiendo reducido la velocidad de descenso a 45 m/s. A los 914 metros de altitud la nave presenta una inclinación de 57 grados. A la puerta baja se llega un minuto y medio después. La altura en ese momento es de 152,3 metros, la inclinación de la nave de 80 grados y la distancia al punto de descenso de 550 metros, mientras que la velocidad se ha reducido a 17 m/s gracias al empuje negativo de 1270 kgf. La trayectoria se va incurvando cada vez más, hasta pasar al descenso vertical de 90° a unos 45 metros de altitud, entonces la velocidad que es controlada por el ordenador de a bordo disminuye desde los 8,2 hasta alcanzar solo 1 m/s. Los sensores que existen en tres de las cuatro patas del módulo de descenso indican el primer contacto, ordenando entonces la parada del motor. El descenso dura del orden de los 11 minutos y 54 segundos. Esta maniobra se simplificó a partir del alunizaje del Apolo 14, permitiendo una mayor disponibilidad de combustible del módulo de descenso para un caso de emergencia. Para ello, la nave Apolo se situó en una órbita lunar elíptica de 108 por 16,5 kilómetros, de manera que el módulo lunar inició la maniobra de descenso y alunizaje a solo 16 500 metros de altura en vez de los 110 000 del caso anterior"

simbolos_a_quitar = (",", ".", "(", ")")

for simbolo in simbolos_a_quitar:
    texto = texto.replace(simbolo,"")

texto = texto.upper()
    
vocablos = texto.split()
palabras = {}
for vocablo in vocablos:
    if vocablo in palabras.keys():
        palabras[vocablo] = palabras[vocablo] + 1
    else:
        palabras[vocablo] = 1

lista = list(palabras.items())

lista.sort(key=lambda palabra : palabra[1])

