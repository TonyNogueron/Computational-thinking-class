'''

Ejercicio de Ciclos 1

Antonio Noguerón

Programa que lea valores a y b y muestre todos los pares que hay entre ellos.
'''

a = int(input("Ingrese un valor inicial a:"))
b = int(input("Ingrese un valor inicial b:"))

for i in range(a,b+1):
    if i % 2 == 0:
        print(i)