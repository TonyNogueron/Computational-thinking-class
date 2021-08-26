'''

Ejercicio de Ciclos 2

Antonio Noguerón

Suma de valores que da el usuario hasta 1000
'''

suma = 0
n = 0

while suma < 1000:
    valor = int(input("Ingresa un valor:"))
    suma += valor
    n += 1
print("El valor de la suma es:", suma)
print("La cantidad de números es:", n)