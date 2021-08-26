'''
Actividad en clase Tiro de dardos

Antonio Noguerón - Efra Antonio - Chris Ruiz

'''
import math
import random


x1 = random.uniform(-4,4)
y1 = random.uniform(-4,4)

x2 = random.uniform(-4,4)
y2 = random.uniform(-4,4)

'''
x1 = 0.5
y1 = -0.8

x2 = -1.9
y2 = 2.0
'''

puntaje = 0

print("Tirada uno:", round(x1,2) , round(y1,2))
distancia = math.sqrt((x1-0)**2 + (y1-0)**2)
print("Distancia del centro:", round(distancia,2) )
if distancia <= 1:
    puntaje = puntaje + 100
elif distancia <= 3:
    puntaje = puntaje + 80


print("Tirada dos:", round(x2,2) , round(y2,2))
distancia = math.sqrt((x2-0)**2 + (y2-0)**2)
print("Distancia del centro:", round(distancia,2) )
if distancia <= 1:
    puntaje = puntaje + 100
elif distancia <= 3:
    puntaje = puntaje + 80



"""
def tiro(x1, y1, puntaje):
    distancia = math.sqrt((x1-0)**2 + (y1-0)**2)
    if distancia <= 1:
        print("Zona1")
        puntaje = puntaje + 100
    elif distancia <= 3:
        print("Zona 2")
        puntaje = puntaje + 80
    else:
        print("Fuera")
    return puntaje
"""

print("El puntaje es:",puntaje)







