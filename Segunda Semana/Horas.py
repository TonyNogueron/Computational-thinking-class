'''

Introducción a if: Tiempo

Antonio Noguerón


'''

hora = int(input("Hora: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

if segundos == 59 and minutos == 59 and hora == 23:
    segundos = 0
    minutos = 0
    hora = 0
elif segundos == 59:
    segundos = 0
    minutos = minutos + 1
else:
    segundos = segundos + 1

print(hora,minutos,segundos)