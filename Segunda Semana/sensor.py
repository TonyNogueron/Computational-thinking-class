sensor = int(input("Ingresa el número de oscilaciones: "))

if sensor >= 100:
    print("alerta roja")
elif 20 <= sensor < 100:
    print("alerta amarilla")
    rk = sensor / 100
    print("El factor RK es:", rk)
else:
    print("normal")