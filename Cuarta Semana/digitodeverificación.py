'''

Dígitos de Verificación

Antonio Noguerón

Programa que un dígito de verificación, dado un código de producto entero positivo, calcular el dígito
Se calcula sumando sus dígitos hasta que quede un solo dígito.

'''

codigo = int(input("Introduce el código del producto: ")) #345  763562

suma = 0

while codigo > 0:
    unidades = codigo % 10
    codigo = codigo //10
    suma = suma + unidades
    if suma > 9 and codigo == 0:
        codigo = suma
        suma = 0
print("El dígito de verificación es:",suma)







"""
#Ideas iniciales para el planteamiento del problema

def digito(num):
    unidades = codigo % 10
    resto = codigo // 10
    return unidades, resto

unidades, resto = digito(codigo)

centena = codigo // 100
codigo = codigo - centena*100
decena = codigo // 10
codigo = codigo - decena*10
unidad = codigo
"""


