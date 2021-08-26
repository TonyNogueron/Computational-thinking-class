'''

Conjetura de Goldbach

Antonio Noguerón - Efraín Antonio

Programa que dado un Número positivo menor que 100 decida si cumple la hipótesis de Goldbach o no.
En caso de que indicar la suma de numeros primos que dan como resultado el número.

Cualquier número par mayor que 2 puede ser escrito como la suma de dos números primos
'''

import random

n = random.randint(1,99)

def esPrimo(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True    

if n % 2 == 0 and n != 2:
    #Probar la conjetura
    for i in range(2,n):
        if esPrimo(i):
            j = n - i
            if esPrimo(j):
                if i <= j:
                    print("Si cumple la conjetura para",n, "sus primos son:", i,"y", j)
else:
    print("La conjetura no se cumple para",n)


    
