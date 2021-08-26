'''

Número perfecto - Tarea 06

Antonio Noguerón

Programa que pide un número entero positivo y si la suma de sus divisores propios menor que n
es igual a n. Imprime un mensaje que indica si es perfecto o no.

'''


try:
    n = int(input("Ingresa un número entero: "))
    if n > 0:
        pass
except:
    print("Ese valor no es válido")
    n = int(input("Ingresa un número entero: "))



sumaDivisores = 0

for i in range(1,n):
    if n % i == 0:
        sumaDivisores += i

if sumaDivisores == n:
    print("El número es perfecto")
else:
    print("El número no es perfecto")


