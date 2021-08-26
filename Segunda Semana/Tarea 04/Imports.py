import math
import random

x1 = float(input("x1: "))
y1 = float(input("y1: "))

x2 = float(input("x2: "))
y2 = float(input("y2: "))

diametro = float(input("Diámetro: "))

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if distancia > diametro:
    print("No hay colisión")
else:
    print("Sí hay colisión")


print(distancia)
