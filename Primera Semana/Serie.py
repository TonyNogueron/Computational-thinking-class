"""
Programa de Serie

Antonio Noguerón Bárcenas

Programa que reciba 3 números y con adiciones y sustracciones, buscar la manera de seguir la serie.
"""
a = int(input("Ingresa el primer número de la serie: ")) #1
b = int(input("Ingresa el segundo número de la serie: ")) #2
c = int(input("Ingresa el tercer número de la serie: ")) #3

d = c + (b - a)  
e = d + (c - b)

print("La serie es:", a, b, c, d, e)