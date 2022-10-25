lista1 = [9,3,6,4]
lista2 = [5,1,8,3,9,2,6]
if len(lista1) < len(lista2): lista = lista1
else: lista = lista2

lista3 = []

for i in lista:
    if i in lista1 and i in lista2:
        lista3.append(i)
print(lista3)
