lista = [5,6,7,7,5,5,2]
r = []

for i in lista:
    if lista.count(i) > 1:
        print("{} apareció {} veces".format(i,lista.count(i)))
        for j in range(lista.count(i)-1):
            lista.remove(i)
print(lista)