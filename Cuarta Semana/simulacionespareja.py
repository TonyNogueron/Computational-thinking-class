"""
Simulación de niños y niñas

Antonio Noguerón

Se debe pedir que ingrese el número de simulaciones

Hacer 5 simulaciones asumiendo que la probabilidad de tener un niño o niña es de 1/2

"""
import random

simulaciones = int(input("Ingresa el número de simulaciones: "))
suma = 0

for i in range(1, simulaciones+1):
    niño = 0
    niña = 0
    hijos = 0
    print("")
    print("Simulación no.",i)
    while niño < 1 or niña < 1:
        sexo = random.randint(0,1)
        if sexo == 0:
            print("niño ", end = "")
            niño += 1
        else:
            print("niña ", end = "")
            niña += 1
        hijos += 1
    print("")
    print("El número de hijos para tener niño y niña fue:", hijos)
    suma = suma + hijos
promedio = suma / simulaciones
print("")
print("El promedio de hijos de el total de simulaciones fue:", promedio)
    
