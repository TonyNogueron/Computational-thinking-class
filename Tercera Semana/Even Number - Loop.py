import random
import math

'''

Antonio Noguerón

Elaborar un programa que genere números aleatorios de 0 a 100, si hay 3 primos deberá detenerse.

'''

primos = 0

def esPrimo(num):
    if num == 0 or num <= 1:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
    return True        

while primos != 3:
    n = random.randint(0,100)
    if esPrimo(n):
        primos += 1
        print("El número", n , "es primo")
    else:
        print(n)
        
