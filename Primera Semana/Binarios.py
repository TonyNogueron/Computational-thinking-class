"""
Binarios

Antonio Noguerón Bárcenas


Programa que recibe 5 números binarios y regresa el número de ceros y de unos
"""
ceros = 0
unos = 0

for i in range(5):
    i = int(input("Ingresa el número binario:"))
    if i == 0:
        ceros = ceros + 1
    elif i == 1:
        unos = unos + 1
    else: print("Ese no es un dato válido")

print("Hay", unos, "unos y",ceros, "ceros.")

'''
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = int(input("d:"))
e = int(input("e:"))
'''