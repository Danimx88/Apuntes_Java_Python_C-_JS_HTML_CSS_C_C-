calificación_estudiantes = [10, 4, 5, 8, 7, 3, 9, 4, 6, 9, 7, 7, 5, 4, 2, 3, 9, 9, 9, 6]

calificación_más_alta = 0
calificación_más_baja = 10

for calificación in calificación_estudiantes:
    if calificación > calificación_más_alta:
        calificación_más_alta = calificación

print(calificación_más_alta)

for calbaja in calificación_estudiantes:
    if calbaja < calificación_más_baja:
        calificación_más_baja = calbaja

print(calificación_más_baja)
