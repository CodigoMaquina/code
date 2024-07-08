"""
@author: Octavio Gutiérrez de Código Máquina

URL del canal: https://www.youtube.com/CodigoMaquina

URL del video: https://youtu.be/rHiu2ZAp4eA
"""

nombres2020 = {"Juan", "Pedro", "Luis", "Pedro"}
nombres2021 = {"Luis", "Maria", "Rosa"}
print(nombres2020)
print(nombres2021)
nombres2021.add("Luis")
print(nombres2021)
nombres2021.add("Jose")
print(nombres2021)
nombres2021.remove("Jose")
print(nombres2021)
print(nombres2020)
nombres = nombres2020.union(nombres2021)
print(nombres)
nombres_ambos_anios = nombres2020.intersection(nombres2021)
print(nombres_ambos_anios)
nombres.difference(nombres_ambos_anios)
print(nombres)
print(nombres2021.issubset(nombres))
print(nombres.issubset(nombres2020))
print(nombres.issuperset(nombres2020))







