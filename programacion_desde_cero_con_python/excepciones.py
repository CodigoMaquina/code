# -*- coding: utf-8 -*-
"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/Itmbtm_3kfM

"""

try: 
    monto = float(input("Monto del crédito: "))
    num_pagos = int(input("Número de pagos mensuales: "))
    if num_pagos < 0: 
        raise Exception("El número de pagos tiene que ser mayor a 0")
    elif num_pagos > 12:
        raise Exception("Tienes que pagar en un año")    
    print("El pago mensual será de: ", monto / num_pagos)

except ValueError:
    print("Introduzca valores númericos válidos")
except ZeroDivisionError:
    print("El número de pagos a realizar debe ser diferente de 0")
except Exception as error: 
    print(error.args[0]) 
else:
    print("Ha completado éxitosamente la solicitud de su crédito")    
finally: 
    print("Agradecemos su preferencia")
    