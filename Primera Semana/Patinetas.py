"""
Programa de Patinetas

Antonio Noguerón Bárcenas

Programa que reciba la cantidad de tablas y la cantidad de ruedas. 
Se necesitan 2 tablas y 4 ruedas para hacer una patineta.
"""

tablas = int(input("Ingresa el número de tablas: "))
ruedas = int(input("Ingresa la cantidad de ruedas: "))

tablas_completas = tablas // 2
ruedas_completas = ruedas // 4

print("Se pueden hacer", min(tablas_completas,ruedas_completas), "patinetas")

'''
if tablas_completas == ruedas_completas:
    print("Se pueden hacer",tablas_completas,"patinetas")
elif tablas_completas < ruedas_completas:
    print("Se pueden hacer", tablas_completas, "patinetas")
else: print("Se pueden hacer", ruedas_completas,"patinetas")
'''