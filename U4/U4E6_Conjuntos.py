# U4E6_Conjuntos.py
# Proyecto: Análisis de conjuntos de estudiantes
# Aplicación para Matemáticas Discretas
#
# Situación:
# En un grupo de Ingeniería en Sistemas Computacionales se realiza
# una encuesta para conocer qué lenguajes de programación conocen
# los estudiantes: Python, Java y C++.
#
# Cada conjunto representa a los estudiantes que conocen un lenguaje.
# El conjunto "estudiantes" representa el universo de la encuesta.

print("================================================")
print("       ANÁLISIS DE CONJUNTOS")
print("       MATEMÁTICAS DISCRETAS - TECNM")
print("================================================")

# 1. Registrar el universo de estudiantes
estudiantes = set()

print("\nREGISTRO DEL GRUPO")
print("Ingrese los nombres de los estudiantes.")
print("Escriba 'salir' para terminar el registro.")

while True:
    nombre = input("Nombre del estudiante: ").strip().title()

    if nombre.lower() == "salir":
        break

    if nombre == "":
        print("El nombre no puede estar vacío.")
    else:
        estudiantes.add(nombre)
        print("Estudiante registrado.")

if len(estudiantes) == 0:
    print("\nNo se registraron estudiantes. Fin del programa.")

else:
    # 2. Registrar quiénes conocen Python
    python = set()

    print("\nESTUDIANTES QUE CONOCEN PYTHON")
    print("Escriba un nombre del grupo o 'fin' para terminar.")

    while True:
        nombre = input("Estudiante: ").strip().title()

        if nombre.lower() == "fin":
            break

        if nombre in estudiantes:
            python.add(nombre)
        else:
            print("El estudiante no pertenece al grupo registrado.")

    # 3. Registrar quiénes conocen Java
    java = set()

    print("\nESTUDIANTES QUE CONOCEN JAVA")
    print("Escriba un nombre del grupo o 'fin' para terminar.")

    while True:
        nombre = input("Estudiante: ").strip().title()

        if nombre.lower() == "fin":
            break

        if nombre in estudiantes:
            java.add(nombre)
        else:
            print("El estudiante no pertenece al grupo registrado.")

    # 4. Registrar quiénes conocen C++
    cpp = set()

    print("\nESTUDIANTES QUE CONOCEN C++")
    print("Escriba un nombre del grupo o 'fin' para terminar.")

    while True:
        nombre = input("Estudiante: ").strip().title()

        if nombre.lower() == "fin":
            break

        if nombre in estudiantes:
            cpp.add(nombre)
        else:
            print("El estudiante no pertenece al grupo registrado.")

    # 5. Mostrar los conjuntos registrados
    print("\n================================================")
    print("CONJUNTOS REGISTRADOS")
    print("================================================")

    print("\nUniverso de estudiantes:")
    print(sorted(estudiantes))

    print("\nConocen Python:")
    print(sorted(python))

    print("\nConocen Java:")
    print(sorted(java))

    print("\nConocen C++:")
    print(sorted(cpp))

    # 6. Operaciones entre conjuntos
    print("\n================================================")
    print("OPERACIONES CON CONJUNTOS")
    print("================================================")

    # Unión: estudiantes que conocen al menos un lenguaje
    conocen_algun_lenguaje = python | java | cpp
    print("\nUnión (Python o Java o C++):")
    print(sorted(conocen_algun_lenguaje))

    # Intersección: estudiantes que conocen los tres lenguajes
    conocen_todos = python & java & cpp
    print("\nIntersección (conocen los tres lenguajes):")
    print(sorted(conocen_todos))

    # Intersecciones de dos conjuntos
    python_java = python & java
    python_cpp = python & cpp
    java_cpp = java & cpp

    print("\nConocen Python y Java:")
    print(sorted(python_java))

    print("\nConocen Python y C++:")
    print(sorted(python_cpp))

    print("\nConocen Java y C++:")
    print(sorted(java_cpp))

    # Diferencia: conocen un lenguaje, pero no los otros dos
    solo_python = python - (java | cpp)
    solo_java = java - (python | cpp)
    solo_cpp = cpp - (python | java)

    print("\nConocen solamente Python:")
    print(sorted(solo_python))

    print("\nConocen solamente Java:")
    print(sorted(solo_java))

    print("\nConocen solamente C++:")
    print(sorted(solo_cpp))

    # Complemento: estudiantes que no conocen ningún lenguaje
    ningun_lenguaje = estudiantes - conocen_algun_lenguaje

    print("\nNo conocen ninguno de los tres lenguajes:")
    print(sorted(ningun_lenguaje))

    # 7. Diferencia simétrica entre Python y Java
    python_o_java_pero_no_ambos = python ^ java

    print("\nConocen Python o Java, pero no ambos:")
    print(sorted(python_o_java_pero_no_ambos))

    # 8. Cardinalidad de los conjuntos
    print("\n================================================")
    print("CARDINALIDAD DE LOS CONJUNTOS")
    print("================================================")

    print("Total de estudiantes:", len(estudiantes))
    print("Conocen Python:", len(python))
    print("Conocen Java:", len(java))
    print("Conocen C++:", len(cpp))
    print("Conocen al menos un lenguaje:", len(conocen_algun_lenguaje))
    print("Conocen los tres lenguajes:", len(conocen_todos))
    print("No conocen ninguno:", len(ningun_lenguaje))

    # 9. Verificar relaciones entre conjuntos
    print("\n================================================")
    print("RELACIONES ENTRE CONJUNTOS")
    print("================================================")

    if python.issubset(estudiantes):
        print("Python es subconjunto del universo de estudiantes.")

    if estudiantes.issuperset(java):
        print("El grupo es superconjunto de quienes conocen Java.")

    if python.isdisjoint(ningun_lenguaje):
        print("Python y quienes no conocen ningún lenguaje son disjuntos.")

    # 10. Resumen por lenguaje
    print("\n================================================")
    print("RESUMEN FINAL")
    print("================================================")

    print("Estudiantes registrados:", len(estudiantes))
    print("Conocen al menos un lenguaje:", len(conocen_algun_lenguaje))
    print("No conocen ningún lenguaje:", len(ningun_lenguaje))

    if len(estudiantes) > 0:
        porcentaje = len(conocen_algun_lenguaje) * 100 / len(estudiantes)
        print("Porcentaje que conoce al menos un lenguaje:", round(porcentaje, 2), "%")

    print("\nAnálisis de conjuntos finalizado.")
