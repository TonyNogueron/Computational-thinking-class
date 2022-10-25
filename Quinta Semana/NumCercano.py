
n = int(input())
multiplicador = 1
num = n

while num <= 100:
    num = n * multiplicador
    multiplicador += 1
num = n * (multiplicador - 2)
print(num)
