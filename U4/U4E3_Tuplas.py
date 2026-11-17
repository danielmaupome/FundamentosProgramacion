# U4E1_Tuplas.py
# Exploración de tuplas en Python

# 1. Vamos a crear una tupla numérica
numeros = (10, 20, 30, 40, 50)
print("Tupla original:", numeros)

# 2. Una tupla puede almacenar diferentes tipos de datos
mixta = (10, "Hola", 3.14, True)
print("Tupla mixta:", mixta)

# 3. También podemos crear una tupla sin paréntesis
colores = "Rojo", "Verde", "Azul"
print("Tupla de colores:", colores)

# 4. Cuidado con las tuplas de un solo elemento:
# La coma es necesaria para que Python la reconozca como tupla
tupla_un_elemento = (25,)
print("Tupla de un elemento:", tupla_un_elemento)
print("Tipo de dato:", type(tupla_un_elemento))

# 5. Manejo de índices
alumnos = ("Ana", "Luis", "Pedro", "María")
print("\nTupla de alumnos:", alumnos)
print("Primer alumno:", alumnos[0])
print("Segundo alumno:", alumnos[1])
print("Último alumno:", alumnos[-1])
print("Penúltimo alumno:", alumnos[-2])

# ¿Qué pasa si intento acceder a un índice que no existe?
# print(alumnos[4])  # Esto causará un error: IndexError

# 6. Obtener una parte de la tupla (slicing)
print("\nDos primeros alumnos:", alumnos[0:2])
print("Desde el segundo alumno:", alumnos[1:])
print("Todos menos el último:", alumnos[:-1])

# 7. ¿Cuántos elementos tiene la tupla?
print("\nCantidad de alumnos:", len(alumnos))

# 8. Buscar cuántas veces aparece un elemento usando count
vocales = ("a", "e", "i", "o", "a", "u", "a")
print("La letra 'a' aparece:", vocales.count("a"), "veces")

# 9. Buscar la posición de un elemento usando index
print("La posición de Pedro es:", alumnos.index("Pedro"))

# ¿Qué pasa si buscamos un elemento que no existe?
# print(alumnos.index("Carlos"))  # Esto causará un error: ValueError

# Es conveniente verificar si el elemento existe antes de buscar su índice
alumno_buscado = "Carlos"
if alumno_buscado in alumnos:
    print("Posición:", alumnos.index(alumno_buscado))
else:
    print(alumno_buscado, "no está en la tupla.")

# 10. Verificar si un elemento existe usando in
print("\n¿Está Ana en la tupla?", "Ana" in alumnos)
print("¿Está Javier en la tupla?", "Javier" in alumnos)

# 11. Concatenar tuplas usando +
grupo_a = ("Ana", "Luis")
grupo_b = ("Pedro", "María")
grupo_completo = grupo_a + grupo_b
print("\nGrupos unidos:", grupo_completo)

# 12. Repetir los elementos de una tupla usando *
repetida = ("Python",) * 3
print("Tupla repetida:", repetida)

# 13. Recorrido de una tupla con for
print("\nRecorrido de alumnos:")
for alumno in alumnos:
    print(alumno)

# 14. Recorrido usando índices
print("\nRecorrido con índices:")
for i in range(len(alumnos)):
    print(f"Alumno {i + 1}: {alumnos[i]}")

# 15. Recorrido usando enumerate
print("\nRecorrido con enumerate:")
for indice, alumno in enumerate(alumnos):
    print(indice, alumno)

# 16. Desempaquetado de tuplas
# Cada variable recibe el valor de una posición
nombre, edad, carrera = ("Daniel", 40, "Sistemas")
print("\nNombre:", nombre)
print("Edad:", edad)
print("Carrera:", carrera)

# 17. Uso de zip para recorrer tuplas relacionadas
productos = ("Sabritas", "Coca Cola 600ml", "Pingüinos", "Donitas Bimbo")
precios = (22.50, 24.00, 18.00, 14.50)

print("\nProductos y precios:")
for producto, precio in zip(productos, precios):
    print(f"{producto} --> ${precio:.2f}")

# 18. Funciones que podemos utilizar con tuplas numéricas
calificaciones = (85, 92, 78, 95, 88)
print("\nCalificaciones:", calificaciones)
print("Cantidad:", len(calificaciones))
print("Suma:", sum(calificaciones))
print("Mayor:", max(calificaciones))
print("Menor:", min(calificaciones))
print("Promedio:", sum(calificaciones) / len(calificaciones))

# 19. Ordenar una tupla usando sorted
# sorted() devuelve una LISTA nueva, no una tupla
numeros_desordenados = (40, 10, 30, 20)
ordenados_lista = sorted(numeros_desordenados)
print("\nTupla original:", numeros_desordenados)
print("Resultado de sorted():", ordenados_lista)
print("Tipo del resultado:", type(ordenados_lista))

# Si necesitamos conservar el tipo tupla, convertimos el resultado
ordenados_tupla = tuple(sorted(numeros_desordenados))
print("Resultado convertido a tupla:", ordenados_tupla)

# 20. Convertir entre listas y tuplas
# Una lista sí permite agregar, eliminar y modificar elementos
lista_alumnos = list(alumnos)
lista_alumnos.append("Sofía")
print("\nLista después de agregar a Sofía:", lista_alumnos)

# Podemos volver a convertirla en tupla
alumnos_actualizados = tuple(lista_alumnos)
print("Tupla actualizada:", alumnos_actualizados)

# 21. Inmutabilidad: no podemos cambiar una posición directamente
# alumnos[0] = "Andrea"  # Esto causará un error: TypeError
# del alumnos[0]         # Esto también causará un error

# Si necesitamos un cambio, creamos una tupla nueva
alumnos_nueva = ("Andrea",) + alumnos[1:]
print("\nTupla original:", alumnos)
print("Nueva tupla:", alumnos_nueva)
