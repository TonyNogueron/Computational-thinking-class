'''

Matusalén

Antonio Noguerón

Tarea 06 - Programa que permita adivinar la edad de un anciano, debe indicar al usuario
que introduzca una edad hasta que adivine la respuesta, pero si no es la correcta deberá
decirle si es mayor o menor. Matusalén tiene 969 años.

'''

n = 0

while n != 969:
    try:
        n = int(input("Indique una edad: "))
    except:
        print("Ese valor no es válido")
        n = int(input("Indique una edad: "))

    edad = 969
    
    if n < edad:
        print("La edad de Matusalén es mayor")
    elif n > edad:
        print("La edad de Matusalén es menor")
    print(" ")
print("Respuesta correcta")