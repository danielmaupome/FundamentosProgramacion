# U4E5_Conjuntos.py
# Exploración de conjuntos (set) en Python

# 1. Crear un conjunto
numeros = {10, 20, 30, 40, 50}
print("Conjunto de números:", numeros)

# 2. Los conjuntos no permiten elementos duplicados
numeros_repetidos = {10, 20, 20, 30, 30, 30, 40}
print("\nConjunto con valores repetidos:", numeros_repetidos)

# 3. Crear un conjunto a partir de una lista
lista_nombres = ["Ana", "Luis", "Ana", "Pedro", "Luis"]
nombres = set(lista_nombres)
print("\nLista original:", lista_nombres)
print("Conjunto sin duplicados:", nombres)

# 4. Crear un conjunto vacío
# Importante: {} crea un diccionario vacío, no un conjunto
conjunto_vacio = set()
print("\nConjunto vacío:", conjunto_vacio)
print("Tipo de dato:", type(conjunto_vacio))

# 5. Agregar un elemento con add()
alumnos = {"Ana", "Luis", "Pedro"}
print("\nAlumnos:", alumnos)
alumnos.add("María")
print("Después de agregar a María:", alumnos)

# Agregar un elemento que ya existe no genera duplicados
alumnos.add("Ana")
print("Después de intentar agregar a Ana nuevamente:", alumnos)

# 6. Agregar varios elementos con update()
alumnos.update(["Sofía", "Diego", "Valeria"])
print("\nDespués de agregar varios alumnos:", alumnos)

# También podemos actualizar un conjunto con otro conjunto
grupo_a = {"Carlos", "Fernanda"}
grupo_b = {"Javier", "Lucía"}
grupo_a.update(grupo_b)
print("Grupo A después de update():", grupo_a)

# 7. Eliminar elementos con remove()
alumnos.remove("Luis")
print("\nDespués de eliminar a Luis:", alumnos)

# Si el elemento no existe, remove() genera KeyError
# alumnos.remove("Roberto")

# 8. Eliminar elementos con discard()
# A diferencia de remove(), discard() no genera error si no existe
alumnos.discard("Roberto")
print("Después de usar discard() con Roberto:", alumnos)

# 9. Eliminar y obtener un elemento con pop()
# Como los conjuntos no tienen posiciones, no podemos elegir qué elemento sale
elemento = alumnos.pop()
print("\nElemento extraído con pop():", elemento)
print("Conjunto después de pop():", alumnos)

# 10. Eliminar todos los elementos con clear()
copia_alumnos = alumnos.copy()
copia_alumnos.clear()
print("\nConjunto después de clear():", copia_alumnos)

# 11. Consultar la cantidad de elementos con len()
print("\nCantidad de alumnos:", len(alumnos))

# 12. Verificar si un elemento pertenece al conjunto con in
print("¿Ana pertenece al conjunto?", "Ana" in alumnos)
print("¿Pedro pertenece al conjunto?", "Pedro" in alumnos)

# 13. Recorrer un conjunto con for
print("\nRecorrido del conjunto:")
for alumno in alumnos:
    print(alumno)

# Recuerda: los conjuntos no mantienen un orden definido.
# Si necesitamos mostrar los elementos ordenados, podemos usar sorted().
print("\nAlumnos ordenados:")
for alumno in sorted(alumnos):
    print(alumno)

# 14. Unión de conjuntos con union() o |
python = {"Ana", "Luis", "Pedro", "María"}
java = {"Luis", "María", "Carlos", "Sofía"}

print("\nPython:", python)
print("Java:", java)
print("Unión:", python.union(java))
print("Unión usando |:", python | java)

# 15. Intersección con intersection() o &
print("\nIntersección:", python.intersection(java))
print("Intersección usando &:", python & java)

# 16. Diferencia con difference() o -
print("\nEstán en Python, pero no en Java:", python.difference(java))
print("Usando -:", python - java)

# La diferencia no es necesariamente igual en ambos sentidos
print("Están en Java, pero no en Python:", java - python)

# 17. Diferencia simétrica con symmetric_difference() o ^
print("\nEstán en uno de los conjuntos, pero no en ambos:")
print(python.symmetric_difference(java))
print("Usando ^:", python ^ java)

# 18. Verificar subconjuntos con issubset()
basico = {"Ana", "Luis"}
grupo = {"Ana", "Luis", "Pedro", "María"}
print("\n¿basico es subconjunto de grupo?", basico.issubset(grupo))

# También podemos usar <=
print("Usando <=:", basico <= grupo)

# 19. Verificar superconjuntos con issuperset()
print("\n¿grupo es superconjunto de basico?", grupo.issuperset(basico))

# También podemos usar >=
print("Usando >=:", grupo >= basico)

# 20. Verificar si dos conjuntos son disjuntos con isdisjoint()
grupo_1 = {"Ana", "Luis"}
grupo_2 = {"Pedro", "María"}
grupo_3 = {"Luis", "Sofía"}

print("\n¿grupo_1 y grupo_2 son disjuntos?", grupo_1.isdisjoint(grupo_2))
print("¿grupo_1 y grupo_3 son disjuntos?", grupo_1.isdisjoint(grupo_3))

# 21. Copiar un conjunto con copy()
original = {"Rojo", "Verde", "Azul"}
copia = original.copy()
copia.add("Amarillo")

print("\nConjunto original:", original)
print("Copia modificada:", copia)

# 22. Convertir un conjunto en una lista
colores = {"Rojo", "Verde", "Azul"}
lista_colores = list(colores)
print("\nConjunto de colores:", colores)
print("Lista de colores:", lista_colores)

# 23. Crear un conjunto inmutable con frozenset()
# No permite agregar ni eliminar elementos
dias = frozenset({"Lunes", "Martes", "Miércoles"})
print("\nConjunto inmutable:", dias)
# dias.add("Jueves")  # Esto generaría un error

# 24. Importante: los conjuntos no permiten acceder por índice
# print(python[0])  # Esto generaría un error: TypeError
