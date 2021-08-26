'''

Tarea 04: Cuadrante

Antonio Noguerón

Realiza un programa que solicite un número enterp que representa la ubicación en grados
dentro de un plano cartesiano y como resultado de el número de cuadrante donde se encuentra.

En el caso de que caiga en un EJE que muestre "EJE", si es menor que 0 o mayor a 360, muestra "EXCEDE"

'''

grados = int(input("Ingresa el ángulo para saber su cuadrante: "))

if grados < 0 or grados > 360:
    print("Excede")
elif grados == 0 or grados == 90 or grados == 180 or grados == 270 or grados == 360:
    print("Eje")
elif grados < 90:
    print("1 - Primer Cuadrante")
elif grados < 180:
    print("2 - Segundo Cuadrante")
elif grados < 270:
    print("3 - Tercer Cuadrante")
else:
    print("4 - Cuarto Cuadrante")