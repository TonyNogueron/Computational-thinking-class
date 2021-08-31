"""
Tarea 08 - Simulación de juego de Cartas

Antonio Noguerón - César Antonio López

Programa en el que el usuario inicia con 1000 pesos, se le pide que apueste contra la computadora
y el juego termina cuando el humano se queda sin dinero.

Se debe pedir que ingrese la cantidad a apostar
Se tiene que validar que la cantidad que ingresó es correcta. (No mayor a su dinero ni negativa)

"""
import random

dinero = 1000
turnos = 1

while dinero > 0:
    
    print("--- Turno ", turnos, "---")
    print("Saldo:", dinero)
    cartaComputadora = random.randint(2,14)
    if cartaComputadora == 14:
        print("Carta de la Computadora: A")
    elif cartaComputadora == 11:
        print("Carta de la Computadora: J")
    elif cartaComputadora == 12:
        print("Carta de la Computadora: Q")
    elif cartaComputadora == 13:
        print("Carta de la Computadora: K")
    else: print("Carta de la Computadora:", cartaComputadora)
    
    apuesta = int(input("Ingresa tu apuesta:"))
    while apuesta < 1 or apuesta > dinero:
        print("No puedes apostar de manera negativa o más de lo que tienes")
        apuesta = int(input("Ingresa tu apuesta:"))
    
    cartaHumano = random.randint(2,14)
    if cartaHumano == 14:
        print("Carta del Humano: A")
    elif cartaHumano == 11:
        print("Carta del Humano: J")
    elif cartaHumano == 12:
        print("Carta del Humano: Q")
    elif cartaHumano == 13:
        print("Carta del Humano: K")
    else: print("Carta del Humano:", cartaHumano)
    
    if cartaComputadora > cartaHumano:
        print("Gana la computadora")
        dinero = dinero - apuesta
    elif cartaHumano > cartaComputadora:
        print("Gana el usuario")
        dinero = dinero + apuesta
    else: print("Empate")
    
    turnos += 1
    print("")
print("")
print("Fin del Juego")
    