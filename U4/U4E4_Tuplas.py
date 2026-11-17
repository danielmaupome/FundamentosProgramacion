
# Sistema de admisión de Hogwarts

# Lista de aprendices. Cada aprendiz será una tupla
aprendices = []

# Casas disponibles
casas = ("Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff")

print("===================================")
print(" COLEGIO HOGWARTS DE MAGIA")
print(" Sistema de admisión de aprendices")
print("===================================")

# Registro de aprendices
while True:

    nombre = input("\nNombre del aprendiz (salir para terminar): ")

    if nombre.lower() == "salir":
        break

    edad = int(input("Edad del aprendiz: "))

    print("\nCasas disponibles:")
    for casa in casas:
        print("-", casa)

    casa_asignada = input("Casa asignada: ").strip()

    if casa_asignada not in casas:
        print("Casa no válida. Intente nuevamente.")
        continue

    habilidad = input("Principal habilidad mágica: ")

    # Crear tupla con los datos del aprendiz
    aprendiz = (nombre, edad, casa_asignada, habilidad)

    # Agregar tupla a la lista
    aprendices.append(aprendiz)

    print("¡Aprendiz registrado correctamente!")

# Generar reporte
if len(aprendices) > 0:

    # Ordenar aprendices por nombre
    aprendices_ordenados = sorted(aprendices)

    print("\n===== REGISTRO DE HOGWARTS =====")

    # Recorrer la lista y desempaquetar las tuplas
    for nombre, edad, casa, habilidad in aprendices_ordenados:
        print(f"\nNombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Casa: {casa}")
        print(f"Habilidad: {habilidad}")

    # Buscar un aprendiz
    buscado = input("\nBuscar aprendiz: ")

    encontrado = False

    for aprendiz in aprendices:
        if aprendiz[0].lower() == buscado.lower():
            print("\nAprendiz encontrado:")
            print("Nombre:", aprendiz[0])
            print("Casa:", aprendiz[2])
            print("Habilidad:", aprendiz[3])
            encontrado = True
            break

    if not encontrado:
        print("Aprendiz no encontrado.")

    # Estadísticas
    suma_edades = 0

    # Contadores para las cuatro casas
    gryffindor = 0
    slytherin = 0
    ravenclaw = 0
    hufflepuff = 0

    for aprendiz in aprendices:

        suma_edades += aprendiz[1]

        if aprendiz[2] == "Gryffindor":
            gryffindor += 1
        elif aprendiz[2] == "Slytherin":
            slytherin += 1
        elif aprendiz[2] == "Ravenclaw":
            ravenclaw += 1
        elif aprendiz[2] == "Hufflepuff":
            hufflepuff += 1

    promedio = suma_edades / len(aprendices)

    print("\n===== ESTADÍSTICAS =====")
    print("Total de aprendices:", len(aprendices))
    print("Edad promedio:", round(promedio, 2))

    print("\nDistribución por casas:")
    print("Gryffindor:", gryffindor)
    print("Slytherin:", slytherin)
    print("Ravenclaw:", ravenclaw)
    print("Hufflepuff:", hufflepuff)

else:
    print("\nNo se registraron aprendices.")
