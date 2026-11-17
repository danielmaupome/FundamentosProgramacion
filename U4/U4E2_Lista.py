materia = input("Ingrese la materia: ")
estudiantes = []
print("Inscribiendo Estudiantes en la materia:", materia)
while True:
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    estudiantes.append(nombre)

print(f"Estudiantes Inscritos en {materia}:")
for estudiante in estudiantes:
    print(estudiante)

# Ordenar la lista de estudiantes alfabéticamente
estudiantes.sort()

print(f"\nEstudiantes Inscritos en {materia}: {estudiantes}")

calificaciones = []
for estudiante in estudiantes:
    calificacion = float(input(f"Ingrese la calificación de {estudiante}: "))
    calificaciones.append(calificacion)

print(f"\nCalificaciones de {materia}:")
for i, estudiante in enumerate(estudiantes):
    print(f"{estudiante}: {calificaciones[i]}")

# Calcular el promedio
promedio = sum(calificaciones) / len(calificaciones)
print(f"\nPromedio de calificaciones en {materia}: {promedio:.2f}")