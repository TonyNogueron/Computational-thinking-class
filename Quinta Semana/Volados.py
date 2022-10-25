"""
Volados

Antonio, Efraín, Armando, Patricio

En este juego el niño deberá indicar una apuesta
y la cara de la moneda que él prefiere (Cara o Cruz)
Enseguida deberá simular 5 tiradas de una moneda
y Gana el primero en ganar 3 volados de 5, si gana duplica su apuesta.

"""
"""```
Ejemplo: 
¿Cuánto apuestas? 5
¿Sol o águila?: Sol
Sol
Sol
Aguila
Aguila
Sol
Ganaste 10 pesos
"""

import random

def jugar(saldo):
  
  print("")
  print("Bienvenido a los volados")
  apuesta = int(input("¿Cuánto apuestas? "))
  while apuesta > saldo or apuesta < 0:
    print("Ingresa un valor válido, no puedes apostar más que tu saldo o negativamente")
    apuesta = int(input("¿Cuánto apuestas? "))
  preferencia = str(input("¿Sol o águila? "))

  sol = 0
  aguila = 0
  print("Presiona Enter para ir viendo las tiradas")

  while aguila <3 and sol <3:
    tiro = random.randint(0,1)
    input("")
    if tiro == 1:
      print("Sol")
      sol += 1
    else:
      print("Águila")
      aguila += 1
  if preferencia == "sol" and sol >= 3:
    apuesta=apuesta*2
    saldo = saldo + apuesta
    print("Ganaste {} pesos".format(apuesta))
    print("")
  elif preferencia == "aguila" and aguila >= 3:
    apuesta=apuesta*2
    saldo = saldo + apuesta
    print("Ganaste {} pesos".format(apuesta)) 
    print("")
  else: 
    saldo = saldo-apuesta
    print("Perdiste",apuesta ," pesos")
    print("")
  return saldo
  


print(jugar(100))
