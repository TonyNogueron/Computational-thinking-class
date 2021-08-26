'''
Tarea Patrones

Antonio Noguerón

Problema: Dado un número entero elaborar una caja horizontal, del ancho indicado por el número entero.

Ejemplos:

Para ancho = 4
----
|  |
----

Para ancho = 5 
-----
|   |
-----

Para ancho: 8
--------
|      |
--------

Para ancho: 10
----------
|        |
----------

'''

ancho = int(input("Ingresa el ancho:"))

guiones = ancho
espacio = ancho - 2

print("-"*ancho)
print("|"+ " "*espacio + "|" )
print("-"*ancho)



#El programa fue realizado con lo visto en clase, por eso no hay condicionales
#y otros aditivos como la validación de datos, entonces si ingresamos un ancho
#negativo o decimal, no funcionará.

