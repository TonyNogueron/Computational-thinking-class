"""
First Class Python Program

Antonio Noguerón Bárcenas


Programa que determine el rendimiento de gasolina de un auto a partir de la distacia recorrida y la gasolina empleada.
"""
km = input("Ingresa el número de kilómetros que recorrió el auto:")
lt = input("Ingresa la cantidad de litros que utilizó en este recorrido:")
rendimiento = float(km) / float(lt)

print("El rendimiento es: " + str(round(rendimiento,3)) + " km/L")


