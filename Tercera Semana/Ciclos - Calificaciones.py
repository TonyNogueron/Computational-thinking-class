'''

Antonio Noguerón


Make a program that asks the number of students and then aks the user
to introduce each grade and then returns the mean of the grades and the highest
and lowest grades.
'''

alumnos = int(input("Ingresa el número de alumnos: "))
alta = 0
baja = 100
sumatoria = 0

for i in range(alumnos):
    nota = int(input("Nota: "))
    if nota > alta:
        alta = nota
    elif nota < baja:
        baja = nota
    sumatoria += nota

promedio = sumatoria / alumnos

print("El promedio de calificaciones es:", promedio)
print("La calificación más alta es:", alta)
print("La calificación más baja es:", baja)