'''

Introducción a if

Antonio Noguerón

Pedir un número entre 0 y 9999 y decir cuantas cifras tiene.

'''

n = int(input("Ingresa el número: "))

if n < 10:
    print("Tiene 1 dígito")
elif n < 100:
    print("Tiene 2 dígitos")
elif n < 1000:
    print("Tiene 3 dígitos")
elif n < 10000:
    print("Tiene 4 dígitos")
else: print("El número no está dentro de los parámetros inciales; 0-9999")
