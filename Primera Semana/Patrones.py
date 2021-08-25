'''

Patrones

Antonio Noguerón 

Dado un número entero, necesito generar una pesa de gimnasio vertical y perfectamente centrada
'''

ancho = int(input("Ingresa el ancho:"))

guiones = ancho
espacio = ancho % 2
barras = (ancho // 2) - 1



print("-"*ancho)
print("-"*ancho)
print(" "*barras + "|"+ " "*espacio+ "|" )
print("-"*ancho)
print("-"*ancho)


''' Ejemplo de como debería ser al ingresar el número 4
print("----")
print("----")
print(" || ")
print("----")
print("----")
'''

