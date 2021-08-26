'''
Estacionamiento

Antonio Noguerón

Programa que pide el costo del estacionamiento y la denominación del billete.
El programa calcula el cambio con monedas de 10,5,2 y 1 peso, se requiere que entregue el menor número de monedas posibles.

Ejemplo: poner un costo de 34 pesos y co un billete de 100 pesos, el programa indicará 6 monedas de 10, 1 de 5 y 1 de peso

'''

precio = int(input("Ingresa el costo del estacionamiento:"))
billete = int(input("Indique el monto introducido en la máquina:"))

cambioInicial = billete - precio
cambio = cambioInicial

moneda_de_10 = cambio//10

cambio = cambio - moneda_de_10 * 10

moneda_de_5 = cambio//5

cambio = cambio - moneda_de_5 * 5

moneda_de_2 = cambio//2

cambio = cambio - moneda_de_2 * 2

moneda_de_1 = cambio



print("Son",cambioInicial, "de cambio")
print(moneda_de_10, "monedas de 10 pesos")
print(moneda_de_5, "monedas de 5 pesos")
print(moneda_de_2, "monedas de 2 pesos")
print(moneda_de_1, "moneda de 1 peso")


#El programa fue realizado con lo visto en clase, por eso no hay condicionales
#y otros aditivos como la validación de datos, entonces si ingresamos un costo
#mayor que el billete, da cambio negativo y monedas negativas



