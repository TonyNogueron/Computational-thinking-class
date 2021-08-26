'''

Casillas

Antonio Noguerón

Programa que recoge las tiradas y si son iguales,
avanza el doble de la suma de los dados
si cae en un múltiplo de 6 se le adicionan 2 casillas más.

'''
import random
import math

casillas = 0

def casilla(dado1, dado2, casillas):  
    if dado1 == dado2:
        casillas = casillas + dado1*4
    else: casillas = casillas + dado1 + dado2

    if casillas % 6 == 0:
        casillas = casillas + 2
    return casillas

casillas = casilla(random.randint(1,6),random.randint(1,6),casillas)
print(casillas)
casillas = casilla(random.randint(1,6),random.randint(1,6),casillas)
print(casillas)

    

    
    