# 🐍 Unidad IV · Estructuras de Datos en Python

**Fundamentos de Programación · AED-1285 · Tecnológico Nacional de México**

> Guía de estudio de los 8 ejemplos de la unidad. Cada sección presenta el propósito del programa, los conceptos que utiliza, una copia del código y aspectos que conviene observar al ejecutarlo.

[**← Volver al README principal**](../README.md)

## 🎯 Objetivo

Utilizar estructuras de datos fundamentales de Python para almacenar, organizar, consultar y manipular información. Comprender las características de las **listas**, **tuplas**, **conjuntos** y **diccionarios**, así como seleccionar la estructura adecuada de acuerdo con las necesidades de una aplicación.

## 📚 Índice de programas

| Ejemplo | Tema | Archivo |
|---|---|---|
| 01 | 4.1 Listas: operaciones y métodos | [`U4E1_Lista.py`](U4E1_Lista.py) |
| 02 | 4.1 Listas: inscripción y calificaciones | [`U4E2_Lista.py`](U4E2_Lista.py) |
| 03 | 4.2 Tuplas: operaciones y características | [`U4E1_Tuplas.py`](U4E1_Tuplas.py) |
| 04 | 4.2 Tuplas: admisión de aprendices en Hogwarts | [`U4E2_Tuplas.py`](U4E2_Tuplas.py) |
| 05 | 4.3 Conjuntos: operaciones y métodos | [`U4E5_Conjuntos.py`](U4E5_Conjuntos.py) |
| 06 | 4.3 Conjuntos: análisis de conjuntos en Matemáticas Discretas | [`U4E6_Conjuntos.py`](U4E6_Conjuntos.py) |
| 07 | 4.4 Diccionarios: operaciones y métodos | [`U4E7_Diccionarios.py`](U4E7_Diccionarios.py) |
| 08 | 4.4 Diccionarios: interfaz bilingüe español/inglés | [`U4E8_Diccionarios.py`](U4E8_Diccionarios.py) |

## ▶️ Cómo ejecutar los programas

1. Instala Python 3.
2. Abre una terminal dentro de la carpeta `U4`.
3. Ejecuta el archivo que quieras revisar. Por ejemplo: `python U4E1_Lista.py` (en algunos sistemas se utiliza `python3`).
4. Introduce los datos solicitados y observa la salida.
5. Para estudiar un programa por secciones, revisa los comentarios y ejecuta el archivo desde tu editor.

> **Nota:** Los programas tienen un propósito didáctico. Las explicaciones describen el comportamiento del código incluido; las actividades de reflexión proponen posibles mejoras o extensiones.

---

## 01. Exploración de listas

**Tema:** 4.1 Estructuras de datos: listas · **Archivo:** [`U4E1_Lista.py`](U4E1_Lista.py)

### Propósito

Presenta la creación de listas, el acceso mediante índices, la modificación de elementos, los métodos para agregar y eliminar datos, el recorrido y el trabajo con listas relacionadas.

### Código del programa

```python
# Vamos a crear una lista numérica

numeros = [10, 20, 30, 40, 50]
print("Lista original:", numeros)

# Python me permite crear una lista con varios tipos de datos
mixta = [10, "Hola", 3.14, True]
print("Lista mixta:", mixta)

# Operaciones con listas
# Agregar elementos a la lista
alumnos = ["Ana", "Luis", "Pedro"]
print("Lista de alumnos:", alumnos)
alumnos.append("María")
print("Lista de alumnos después de agregar a María:", alumnos)

# Manejo de índices
print("Primer alumno:", alumnos[0])
print("Segundo alumno:", alumnos[1])
print("Tercer alumno:", alumnos[2])
print("Cuarto alumno:", alumnos[3])

# Usando el índice negativo para acceder al último elemento
print("Último alumno:", alumnos[-1])

# ¿Qué pasa si intento acceder a un índice que no existe?
# print("Quinto alumno:", alumnos[4])  # Esto causará un error, hay que comentarlo

# Qué pasa si intento acceder a un índice negativo diferente a -1
print("Penúltimo alumno:", alumnos[-2])  # Esto funciona y devuelve "Pedro"

# Vamos a ordenar elementos de una lista
alumnos.sort()
print("Lista de alumnos ordenada:", alumnos)

# Eliminar elementos de la lista
alumnos.remove("Luis")
print("Lista de alumnos después de eliminar a Luis:", alumnos)

# Eliminar un elemento por su índice
del alumnos[0]
print("Lista de alumnos después de eliminar al primer alumno:", alumnos)

# Eliminar el último elemento de la lista
alumnos.pop()
print("Lista de alumnos después de eliminar el último alumno:", alumnos)

# Agregaremos un elemento al final de la lista
alumnos.append("Sofía")
alumnos.append("Diego")
alumnos.append("Valeria")
alumnos.append("Javier")
alumnos.sort()
print("Lista de alumnos después de agregar varios alumnos y ordenar:", alumnos)


# Recorrido de la lista con un bucle for
print("Recorrido de la lista de alumnos:")
for alumno in alumnos:
    print(alumno)

# Recorrido de lista iterando con índices
print("Recorrido de la lista de alumnos con índices:")
for i in range(len(alumnos)):
    print(f"Alumno {i + 1}: {alumnos[i]}")

# Forma de iterar usando enumerate para obtener el índice y el valor
print("Recorrido de la lista de alumnos con enumerate:")
for index, l in enumerate(alumnos):
    print(index, l)

# Creamos dos listas, cuyos elementos se van a relacionar entre sí, por ejemplo, una lista de productos y otra de precios. Cada producto tiene un precio asociado, y ambos se relacionan por su posición en la lista.
productos = ["Sabritas", "Coca Cola 600ml", "Pingüinos", "Donitas Bimbo"]
precios = [22.50, 24.00, 18.00, 14.50]

# Impresión de dos listas relacionadas usando zip
print("Lista de productos y sus precios:")
for elem1, elem2 in zip(productos, precios):
    print(f"{elem1} --> ${elem2:.2f}")

# Se añade una lista de productos y precios a las listas existentes usando extend
productos.extend(["Galletas", "Chicles", "Chocolate"])
precios.extend([15.00, 5.00, 20.00])

# Se añade un producto y su precio usando insert, para colocarlo en una posición específica
productos.insert(2, "Agua Mineral 500ml")
precios.insert(2, 12.00)

# Impresión de dos listas relacionadas usando zip
print("Lista de productos y sus precios:")
for elem1, elem2 in zip(productos, precios):
    print(f"{elem1} --> ${elem2:.2f}")

# Invertimos el orden de la lista de productos y precios usando reverse
productos.reverse()
precios.reverse()

# Impresión de dos listas relacionadas usando zip
print("Lista de productos y sus precios:")
for elem1, elem2 in zip(productos, precios):
    print(f"{elem1} --> ${elem2:.2f}")

# Buscamos un producto en la lista y mostramos su precio
producto_buscado = "Pingüinos"
indice = productos.index(producto_buscado)
print(f"El precio de {producto_buscado} es: ${precios[indice]:.2f}")

# Que pasa si intento buscar un producto que no existe en la lista. Cuando lo hayas buscado, comenta la línea de código para que no cause un error y puedas seguir ejecutando el programa.
# producto_buscado = "Galletas de Chocolate"
# indice = productos.index(producto_buscado)
# print(f"El precio de {producto_buscado} es: ${precios[indice]:.2f}")

# Sería mas correcto usar un condicional para verificar si el producto existe en la lista antes de intentar buscar su índice
producto_buscado = "Galletas de Chocolate"
if producto_buscado in productos:
    indice = productos.index(producto_buscado)
    print(f"El precio de {producto_buscado} es: ${precios[indice]:.2f}")
else:
    print(f"El producto {producto_buscado} no está en la lista.")
```

### Explicación paso a paso

1. `[]` crea una lista y permite almacenar varios elementos, incluso de distintos tipos.
2. `append()`, `extend()` e `insert()` agregan elementos de diferentes maneras.
3. `sort()` y `reverse()` modifican el orden de la lista original.
4. `remove()`, `del` y `pop()` permiten eliminar elementos.
5. `len()`, `index()` y el operador `in` ayudan a consultar la lista.
6. `for`, `range()` y `enumerate()` permiten recorrer sus elementos.
7. `zip()` permite recorrer simultáneamente listas relacionadas, como productos y precios.

**Prueba sugerida:** Observar cómo cambia la lista después de cada operación y comprobar que las posiciones de productos y precios se mantienen relacionadas.

**Aprendizaje:** Presenta la creación de listas, el acceso mediante índices, la modificación de elementos, los métodos para agregar y eliminar datos, el recorrido y el trabajo con listas relacionadas.

**Para reflexionar:** ¿Qué podría ocurrir si se agrega un producto a la lista de productos, pero no se agrega su precio en la posición correspondiente?

---


## 02. Aplicación: inscripción de estudiantes y captura de calificaciones

**Tema:** 4.1 Estructuras de datos: listas · **Archivo:** [`U4E2_Lista.py`](U4E2_Lista.py)

### Propósito

Construye un pequeño sistema que registra estudiantes en una materia, ordena sus nombres, captura calificaciones y calcula el promedio grupal.

### Código del programa

```python
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
```

### Explicación paso a paso

1. Una lista almacena los nombres de los estudiantes inscritos.
2. `while` permite registrar nombres hasta que se escriba `salir`.
3. `append()` agrega cada nuevo estudiante.
4. `sort()` ordena alfabéticamente la lista.
5. Una segunda lista almacena las calificaciones en el mismo orden.
6. `enumerate()` permite mostrar cada estudiante junto con la calificación ubicada en la misma posición.
7. `sum()` y `len()` permiten calcular el promedio.

**Prueba sugerida:** Registrar varios estudiantes, finalizar la captura y después introducir una calificación para cada uno. Comparar el reporte con el promedio calculado.

**Aprendizaje:** Construye un pequeño sistema que registra estudiantes en una materia, ordena sus nombres, captura calificaciones y calcula el promedio grupal.

**Para reflexionar:** ¿Por qué es importante mantener el mismo orden en las listas de estudiantes y calificaciones?

---


## 03. Exploración de tuplas

**Tema:** 4.2 Estructuras de datos: tuplas · **Archivo:** [`U4E1_Tuplas.py`](U4E1_Tuplas.py)

### Propósito

Explica cómo crear tuplas, acceder a sus elementos, obtener segmentos, consultar información y combinar tuplas. También compara las tuplas con las listas.

### Código del programa

```python
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
```

### Explicación paso a paso

1. Las tuplas se crean normalmente con paréntesis y sus elementos se separan mediante comas.
2. Una tupla de un solo elemento requiere una coma final, por ejemplo `(25,)`.
3. Los índices positivos y negativos permiten consultar elementos; el slicing obtiene segmentos.
4. `count()` cuenta apariciones e `index()` devuelve la posición de un elemento.
5. El operador `in` verifica si un elemento pertenece a la tupla.
6. `+` concatena tuplas y `*` repite sus elementos.
7. `for`, `range()` y `enumerate()` permiten recorrerlas.
8. El desempaquetado asigna los elementos de una tupla a variables.
9. `sorted()` devuelve una lista ordenada; se puede convertir nuevamente con `tuple()`.
10. La inmutabilidad impide cambiar o eliminar directamente elementos de una tupla.

**Prueba sugerida:** Ejecutar los ejemplos de consulta y recorrido. Después, descomentar por separado las instrucciones que intentan modificar o eliminar elementos para observar el error.

**Aprendizaje:** Explica cómo crear tuplas, acceder a sus elementos, obtener segmentos, consultar información y combinar tuplas. También compara las tuplas con las listas.

**Para reflexionar:** ¿En qué situaciones conviene utilizar una tupla en lugar de una lista?

---


## 04. Aplicación: sistema de admisión de Hogwarts

**Tema:** 4.2 Estructuras de datos: tuplas · **Archivo:** [`U4E2_Tuplas.py`](U4E2_Tuplas.py)

### Propósito

Simula el registro de aprendices del Colegio Hogwarts de Magia y Hechicería. Cada aprendiz se representa mediante una tupla con nombre, edad, casa y habilidad mágica; una lista reúne todos los registros.

### Código del programa

```python
# U4E2_Tuplas.py
# Aplicación: Registro de estudiantes y calificaciones
#
# En este programa cada estudiante se representa mediante una tupla:
# (nombre, calificacion)
#
# Las tuplas permiten mantener juntos los datos de cada estudiante
# y evitar que se modifique accidentalmente uno de sus valores.
# La lista permite agregar nuevos registros al grupo.

materia = input("Ingrese el nombre de la materia: ")

# Lista que almacenará tuplas con los datos de cada estudiante
estudiantes = []

print("\nRegistro de estudiantes en:", materia)

while True:
    nombre = input("Nombre del estudiante (o 'salir' para terminar): ").strip()

    if nombre.lower() == "salir":
        break

    if nombre == "":
        print("El nombre no puede estar vacío.")
        continue

    # Capturamos y validamos la calificación
    try:
        calificacion = float(input(f"Calificación de {nombre}: "))
    except ValueError:
        print("Ingrese una calificación numérica.")
        continue

    if calificacion < 0 or calificacion > 100:
        print("La calificación debe estar entre 0 y 100.")
        continue

    # Creamos una tupla con el nombre y la calificación
    estudiante = (nombre, calificacion)

    # Agregamos la tupla a la lista
    estudiantes.append(estudiante)

    print("Registro agregado correctamente.\n")

# Verificamos que existan estudiantes antes de generar el reporte
if len(estudiantes) == 0:
    print("\nNo se registraron estudiantes. No es posible generar el promedio.")

else:
    # Ordenamos los registros alfabéticamente por el nombre.
    # sorted() crea una nueva lista y conserva cada tupla completa.
    estudiantes_ordenados = sorted(estudiantes, key=lambda registro: registro[0].lower())

    print(f"\nESTUDIANTES INSCRITOS EN {materia.upper()}")
    print("-" * 45)

    # Recorremos la lista y desempaquetamos cada tupla
    for nombre, calificacion in estudiantes_ordenados:
        print(f"{nombre}: {calificacion:.2f}")

    # Calculamos el promedio utilizando las calificaciones de las tuplas
    suma_calificaciones = 0

    for nombre, calificacion in estudiantes:
        suma_calificaciones += calificacion

    promedio = suma_calificaciones / len(estudiantes)

    # Identificamos la calificación mayor y menor
    estudiante_mayor = max(estudiantes, key=lambda registro: registro[1])
    estudiante_menor = min(estudiantes, key=lambda registro: registro[1])

    print("\nRESUMEN DE CALIFICACIONES")
    print("-" * 45)
    print("Total de estudiantes:", len(estudiantes))
    print(f"Promedio grupal: {promedio:.2f}")
    print(f"Calificación más alta: {estudiante_mayor[0]} ({estudiante_mayor[1]:.2f})")
    print(f"Calificación más baja: {estudiante_menor[0]} ({estudiante_menor[1]:.2f})")

    # Buscamos a un estudiante por su nombre
    buscado = input("\nIngrese el nombre de un estudiante para consultar su calificación: ").strip()

    encontrado = False

    for nombre, calificacion in estudiantes:
        if nombre.lower() == buscado.lower():
            print(f"La calificación de {nombre} es {calificacion:.2f}.")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró al estudiante:", buscado)

    # Ordenamos por calificación de mayor a menor
    por_calificacion = sorted(estudiantes, key=lambda registro: registro[1], reverse=True)

    print("\nESTUDIANTES ORDENADOS POR CALIFICACIÓN")
    print("-" * 45)

    for posicion, (nombre, calificacion) in enumerate(por_calificacion, start=1):
        print(f"{posicion}. {nombre}: {calificacion:.2f}")
```

### Explicación paso a paso

1. La lista `aprendices` almacena los registros capturados.
2. Cada registro es una tupla con cuatro datos: nombre, edad, casa y habilidad.
3. La tupla `casas` contiene las cuatro casas disponibles.
4. El ciclo `while` permite registrar aprendices hasta escribir `salir`.
5. `in` valida que la casa seleccionada exista en la tupla de casas.
6. `append()` agrega cada tupla a la lista de aprendices.
7. `sorted()` crea una nueva lista ordenada por el contenido de las tuplas; en este ejemplo, el nombre es el primer elemento.
8. El programa busca aprendices, calcula la edad promedio y cuenta cuántos pertenecen a cada casa.

**Prueba sugerida:** Registrar aprendices de distintas casas, generar el reporte, buscar un nombre existente y otro inexistente, y revisar las estadísticas.

**Aprendizaje:** Simula el registro de aprendices del Colegio Hogwarts de Magia y Hechicería. Cada aprendiz se representa mediante una tupla con nombre, edad, casa y habilidad mágica; una lista reúne todos los registros.

**Para reflexionar:** ¿Por qué se utiliza una lista para almacenar a todos los aprendices y una tupla para representar los datos de cada uno?

---


## 05. Exploración de conjuntos

**Tema:** 4.3 Estructuras de datos: conjuntos · **Archivo:** [`U4E5_Conjuntos.py`](U4E5_Conjuntos.py)

### Propósito

Presenta los conjuntos como colecciones sin elementos duplicados y sin posiciones definidas. Incluye operaciones para agregar, eliminar, consultar y comparar conjuntos.

### Código del programa

```python
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
```

### Explicación paso a paso

1. `{}` con elementos crea un conjunto; `set()` crea un conjunto vacío. Las llaves vacías `{}` crean un diccionario.
2. `add()` agrega un elemento y `update()` agrega varios.
3. `remove()`, `discard()`, `pop()` y `clear()` permiten eliminar elementos con comportamientos diferentes.
4. `len()` y `in` permiten consultar cantidad y pertenencia.
5. `union()` o `|` obtiene la unión.
6. `intersection()` o `&` obtiene la intersección.
7. `difference()` o `-` obtiene la diferencia.
8. `symmetric_difference()` o `^` obtiene la diferencia simétrica.
9. `issubset()`, `issuperset()` e `isdisjoint()` permiten comprobar relaciones entre conjuntos.
10. `copy()` crea una copia y `frozenset()` crea un conjunto inmutable.
11. `sorted()` permite presentar los elementos ordenados, aunque devuelve una lista.

**Prueba sugerida:** Crear dos conjuntos con elementos repetidos y ejecutar unión, intersección, diferencia y diferencia simétrica. Comparar los resultados con las operaciones escritas en notación matemática.

**Aprendizaje:** Presenta los conjuntos como colecciones sin elementos duplicados y sin posiciones definidas. Incluye operaciones para agregar, eliminar, consultar y comparar conjuntos.

**Para reflexionar:** ¿Por qué no podemos acceder a un elemento de un conjunto mediante un índice?

---


## 06. Aplicación: análisis de conjuntos en Matemáticas Discretas

**Tema:** 4.3 Estructuras de datos: conjuntos · **Archivo:** [`U4E6_Conjuntos.py`](U4E6_Conjuntos.py)

### Propósito

Analiza los lenguajes de programación que conocen los estudiantes de un grupo. El universo contiene a todos los estudiantes y tres conjuntos representan quiénes conocen Python, Java y C++.

### Código del programa

```python
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
```

### Explicación paso a paso

1. El conjunto `estudiantes` representa el universo de la encuesta.
2. Los conjuntos `python`, `java` y `cpp` almacenan a quienes conocen cada lenguaje.
3. El programa verifica que los nombres ingresados pertenezcan al universo registrado.
4. La unión identifica a quienes conocen al menos uno de los lenguajes.
5. La intersección identifica a quienes conocen los tres lenguajes y también permite analizar pares.
6. La diferencia permite identificar quiénes conocen solamente un lenguaje.
7. El complemento se obtiene restando del universo a quienes conocen al menos un lenguaje.
8. La diferencia simétrica identifica a quienes pertenecen a uno de dos conjuntos, pero no a ambos.
9. `len()` permite obtener la cardinalidad de los conjuntos.
10. `issubset()`, `issuperset()` e `isdisjoint()` permiten comprobar relaciones.

**Prueba sugerida:** Registrar un grupo pequeño y asignar estudiantes a los conjuntos de Python, Java y C++. Comprobar manualmente las operaciones con un diagrama de Venn.

**Aprendizaje:** Analiza los lenguajes de programación que conocen los estudiantes de un grupo. El universo contiene a todos los estudiantes y tres conjuntos representan quiénes conocen Python, Java y C++.

**Para reflexionar:** ¿Cómo se interpreta el complemento de la unión de Python, Java y C++ respecto al universo de estudiantes?

---


## 07. Exploración de diccionarios

**Tema:** 4.4 Estructuras de datos: diccionarios · **Archivo:** [`U4E7_Diccionarios.py`](U4E7_Diccionarios.py)

### Propósito

Explica cómo almacenar información mediante pares de clave y valor, consultar y modificar datos, recorrer diccionarios y organizar estructuras anidadas.

### Código del programa

```python
# U4E7_Diccionarios.py
# Exploración de diccionarios en Python

# 1. Crear un diccionario
alumno = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Ingeniería en Sistemas Computacionales"
}
print("Diccionario del alumno:", alumno)

# 2. Un diccionario almacena pares de clave y valor
producto = {
    "codigo": "P001",
    "descripcion": "Teclado",
    "precio": 450.50,
    "existencia": 15
}
print("\nInformación del producto:", producto)

# 3. Acceder a los valores mediante sus claves
print("\nNombre del alumno:", alumno["nombre"])
print("Edad del alumno:", alumno["edad"])

# Si intentamos consultar una clave que no existe, se genera KeyError
# print(alumno["correo"])

# 4. Consultar valores con get()
# get() permite indicar un valor alternativo si la clave no existe
print("\nCorreo del alumno:", alumno.get("correo"))
print("Correo alternativo:", alumno.get("correo", "No registrado"))

# 5. Agregar nuevos pares clave-valor
alumno["correo"] = "ana@ejemplo.com"
alumno["semestre"] = 4
print("\nAlumno después de agregar datos:", alumno)

# 6. Modificar el valor asociado a una clave
alumno["edad"] = 21
print("\nEdad modificada:", alumno["edad"])

# 7. Actualizar varios datos con update()
alumno.update({
    "semestre": 5,
    "carrera": "Ingeniería en Sistemas"
})
print("\nDiccionario después de update():", alumno)

# 8. Verificar si una clave existe con in
print("\n¿Existe la clave nombre?", "nombre" in alumno)
print("¿Existe la clave teléfono?", "telefono" in alumno)

# Importante: in verifica las claves, no los valores
print("¿Existe el valor Ana?", "Ana" in alumno)

# Para verificar un valor podemos utilizar values()
print("¿Existe Ana entre los valores?", "Ana" in alumno.values())

# 9. Consultar la cantidad de elementos con len()
print("\nCantidad de pares clave-valor:", len(alumno))

# 10. Obtener todas las claves con keys()
print("\nClaves del diccionario:")
print(alumno.keys())

# 11. Obtener todos los valores con values()
print("\nValores del diccionario:")
print(alumno.values())

# 12. Obtener pares clave-valor con items()
print("\nPares clave-valor:")
print(alumno.items())

# 13. Recorrer las claves de un diccionario
print("\nRecorrido de claves:")
for clave in alumno:
    print(clave)

# 14. Recorrer los valores de un diccionario
print("\nRecorrido de valores:")
for valor in alumno.values():
    print(valor)

# 15. Recorrer claves y valores con items()
print("\nRecorrido de claves y valores:")
for clave, valor in alumno.items():
    print(clave, ":", valor)

# 16. Eliminar un elemento con pop()
# pop() elimina la clave indicada y devuelve su valor
correo_eliminado = alumno.pop("correo")
print("\nCorreo eliminado:", correo_eliminado)
print("Diccionario actualizado:", alumno)

# 17. Eliminar el último par insertado con popitem()
elemento_eliminado = alumno.popitem()
print("\nÚltimo elemento eliminado:", elemento_eliminado)
print("Diccionario actualizado:", alumno)

# 18. Eliminar un elemento con del
del alumno["edad"]
print("\nDespués de eliminar la edad:", alumno)

# 19. Crear un diccionario a partir de claves con fromkeys()
claves = ("lunes", "martes", "miércoles")
asistencia = dict.fromkeys(claves, False)
print("\nRegistro inicial de asistencia:", asistencia)

# 20. Agregar un valor solamente si la clave no existe con setdefault()
asistencia.setdefault("jueves", False)
asistencia.setdefault("lunes", True)

print("\nDespués de utilizar setdefault():", asistencia)
# La clave lunes conserva su valor original porque ya existía

# 21. Copiar un diccionario con copy()
original = {
    "nombre": "Carlos",
    "calificacion": 90
}
copia = original.copy()
copia["calificacion"] = 95

print("\nDiccionario original:", original)
print("Copia modificada:", copia)

# 22. Eliminar todos los elementos con clear()
copia.clear()
print("\nDiccionario después de clear():", copia)

# 23. Diccionarios anidados: un diccionario dentro de otro
estudiantes = {
    "A001": {
        "nombre": "Mariana",
        "edad": 20,
        "promedio": 92
    },
    "A002": {
        "nombre": "José",
        "edad": 21,
        "promedio": 85
    }
}

print("\nDiccionario de estudiantes:", estudiantes)

# Acceder a un dato de un diccionario anidado
print("Nombre del estudiante A001:", estudiantes["A001"]["nombre"])
print("Promedio del estudiante A002:", estudiantes["A002"]["promedio"])

# 24. Recorrer un diccionario anidado
print("\nReporte de estudiantes:")
for matricula, datos in estudiantes.items():
    print("\nMatrícula:", matricula)
    for clave, valor in datos.items():
        print(clave, ":", valor)

# 25. Diccionarios y listas: almacenar varios valores en una clave
inventario = {
    "producto": "Cuadernos",
    "precios": [25.50, 30.00, 35.00]
}

print("\nProducto:", inventario["producto"])
print("Lista de precios:", inventario["precios"])
print("Segundo precio:", inventario["precios"][1])

# 26. Convertir las claves de un diccionario en una lista
lista_claves = list(alumno.keys())
print("\nLista de claves:", lista_claves)

# 27. Convertir los pares clave-valor en una lista
lista_elementos = list(producto.items())
print("Lista de pares:", lista_elementos)

# 28. Importante: las claves deben ser únicas
# Si repetimos una clave, el último valor reemplaza al anterior
colores = {
    "principal": "Azul",
    "secundario": "Verde",
    "principal": "Rojo"
}
print("\nDiccionario con clave repetida:", colores)
```

### Explicación paso a paso

1. Los diccionarios se crean con llaves y almacenan pares de clave y valor.
2. Los valores se consultan mediante su clave o con `get()`.
3. La asignación permite agregar una clave nueva o modificar su valor.
4. `update()` actualiza varios pares; `setdefault()` agrega una clave solamente si no existe.
5. `in` verifica la existencia de claves; `values()` permite consultar los valores.
6. `keys()`, `values()` e `items()` permiten obtener claves, valores y pares.
7. `pop()`, `popitem()`, `del` y `clear()` permiten eliminar información.
8. `copy()` crea una copia del diccionario.
9. Los diccionarios pueden contener otros diccionarios, listas y diferentes tipos de datos.
10. Las claves deben ser únicas; si una clave se repite al crear el diccionario, prevalece el último valor asignado.

**Prueba sugerida:** Crear un diccionario, agregar y modificar datos, consultar claves existentes e inexistentes y recorrer sus pares con `items()`.

**Aprendizaje:** Explica cómo almacenar información mediante pares de clave y valor, consultar y modificar datos, recorrer diccionarios y organizar estructuras anidadas.

**Para reflexionar:** ¿Qué ventajas ofrece consultar un dato mediante una clave descriptiva en lugar de utilizar una posición numérica?

---


## 08. Aplicación: interfaz bilingüe español/inglés

**Tema:** 4.4 Estructuras de datos: diccionarios · **Archivo:** [`U4E8_Diccionarios.py`](U4E8_Diccionarios.py)

### Propósito

Construye una interfaz de consola cuyos textos cambian entre español e inglés. Los diccionarios anidados almacenan las traducciones y permiten mostrar menús, perfil, notificaciones y configuración en el idioma seleccionado.

### Código del programa

```python
# U4E8_Diccionarios.py
# Proyecto: Interfaz bilingüe para una aplicación
# Idiomas disponibles: español e inglés
#
# El programa utiliza diccionarios anidados para almacenar
# los textos de la interfaz en diferentes idiomas.
# El usuario puede cambiar el idioma mientras utiliza la aplicación.

# 1. Diccionario principal de idiomas
# Cada idioma contiene otro diccionario con los textos de la interfaz.

idiomas = {
    "es": {
        "nombre_app": "MI APLICACIÓN",
        "bienvenida": "¡Bienvenido!",
        "menu_titulo": "MENÚ PRINCIPAL",
        "opcion_perfil": "Ver perfil",
        "opcion_notificaciones": "Consultar notificaciones",
        "opcion_configuracion": "Configuración",
        "opcion_idioma": "Cambiar idioma",
        "opcion_salir": "Salir",
        "seleccione": "Seleccione una opción: ",
        "perfil_titulo": "PERFIL DEL USUARIO",
        "nombre": "Nombre",
        "carrera": "Carrera",
        "institucion": "Institución",
        "notificaciones_titulo": "NOTIFICACIONES",
        "sin_notificaciones": "No tiene notificaciones nuevas.",
        "configuracion_titulo": "CONFIGURACIÓN",
        "idioma_actual": "Idioma actual",
        "idioma_espanol": "Español",
        "idioma_ingles": "Inglés",
        "seleccionar_idioma": "Seleccione el idioma (es/en): ",
        "idioma_cambiado": "Idioma actualizado correctamente.",
        "idioma_no_valido": "Idioma no válido.",
        "opcion_no_valida": "Opción no válida. Intente nuevamente.",
        "despedida": "Gracias por utilizar la aplicación. ¡Hasta pronto!"
    },

    "en": {
        "nombre_app": "MY APPLICATION",
        "bienvenida": "Welcome!",
        "menu_titulo": "MAIN MENU",
        "opcion_perfil": "View profile",
        "opcion_notificaciones": "Check notifications",
        "opcion_configuracion": "Settings",
        "opcion_idioma": "Change language",
        "opcion_salir": "Exit",
        "seleccione": "Select an option: ",
        "perfil_titulo": "USER PROFILE",
        "nombre": "Name",
        "carrera": "Degree program",
        "institucion": "Institution",
        "notificaciones_titulo": "NOTIFICATIONS",
        "sin_notificaciones": "You have no new notifications.",
        "configuracion_titulo": "SETTINGS",
        "idioma_actual": "Current language",
        "idioma_espanol": "Spanish",
        "idioma_ingles": "English",
        "seleccionar_idioma": "Select language (es/en): ",
        "idioma_cambiado": "Language updated successfully.",
        "idioma_no_valido": "Invalid language.",
        "opcion_no_valida": "Invalid option. Please try again.",
        "despedida": "Thank you for using the application. See you soon!"
    }
}

# 2. Información del usuario
# Este diccionario representa los datos que mostraría la aplicación.
usuario = {
    "nombre": "Daniel Maupomé",
    "carrera": "Ingeniería en Sistemas Computacionales",
    "institucion": "TecNM"
}

# 3. Notificaciones de ejemplo
notificaciones = [
    "Tienes una nueva actividad disponible.",
    "Tu perfil se encuentra actualizado."
]

# 4. Seleccionar el idioma inicial
idioma = "es"

print("===================================")
print(idiomas[idioma]["nombre_app"])
print("===================================")
print(idiomas[idioma]["bienvenida"])

# 5. Menú principal
while True:

    # Obtener los textos del idioma seleccionado
    textos = idiomas[idioma]

    print("\n===================================")
    print(textos["menu_titulo"])
    print("===================================")

    print("1.", textos["opcion_perfil"])
    print("2.", textos["opcion_notificaciones"])
    print("3.", textos["opcion_configuracion"])
    print("4.", textos["opcion_idioma"])
    print("5.", textos["opcion_salir"])

    opcion = input(textos["seleccione"])

    # 6. Consultar el perfil del usuario
    if opcion == "1":

        print("\n==========", textos["perfil_titulo"], "==========")
        print(textos["nombre"] + ":", usuario["nombre"])
        print(textos["carrera"] + ":", usuario["carrera"])
        print(textos["institucion"] + ":", usuario["institucion"])

    # 7. Consultar notificaciones
    elif opcion == "2":

        print("\n==========", textos["notificaciones_titulo"], "==========")

        if len(notificaciones) == 0:
            print(textos["sin_notificaciones"])
        else:
            for notificacion in notificaciones:
                print("-", notificacion)

    # 8. Consultar configuración
    elif opcion == "3":

        print("\n==========", textos["configuracion_titulo"], "==========")

        if idioma == "es":
            nombre_idioma = textos["idioma_espanol"]
        else:
            nombre_idioma = textos["idioma_ingles"]

        print(textos["idioma_actual"] + ":", nombre_idioma)

    # 9. Cambiar el idioma de la aplicación
    elif opcion == "4":

        nuevo_idioma = input(textos["seleccionar_idioma"]).strip().lower()

        if nuevo_idioma in idiomas:
            idioma = nuevo_idioma
            print(idiomas[idioma]["idioma_cambiado"])
        else:
            print(textos["idioma_no_valido"])

    # 10. Salir de la aplicación
    elif opcion == "5":

        print("\n" + textos["despedida"])
        break

    else:
        print(textos["opcion_no_valida"])
```

### Explicación paso a paso

1. El diccionario `idiomas` contiene dos claves principales: `es` y `en`.
2. Cada idioma contiene un diccionario interno con los textos de la interfaz.
3. El diccionario `usuario` almacena los datos del perfil.
4. La lista `notificaciones` contiene mensajes que se muestran al usuario.
5. La variable `idioma` determina qué conjunto de textos se utiliza.
6. El menú permite consultar perfil, notificaciones y configuración.
7. La opción de cambio de idioma verifica que la clave ingresada exista en `idiomas`.
8. Al cambiar la variable `idioma`, los siguientes textos del menú se muestran en el idioma seleccionado.

**Prueba sugerida:** Ejecutar la aplicación en español, cambiar a inglés, recorrer las opciones del menú y regresar a español.

**Aprendizaje:** Construye una interfaz de consola cuyos textos cambian entre español e inglés. Los diccionarios anidados almacenan las traducciones y permiten mostrar menús, perfil, notificaciones y configuración en el idioma seleccionado.

**Para reflexionar:** ¿Qué tendrías que agregar al diccionario `idiomas` para incorporar un tercer idioma sin modificar la lógica del menú?

---

## 🧩 Conceptos que se practican

| Estructura | Ejemplos | Elementos clave |
|---|---|---|
| Listas | 01–02 | Índices, slicing, `append()`, `extend()`, `insert()`, `sort()`, `remove()`, `pop()`, `zip()` |
| Tuplas | 03–04 | Inmutabilidad, índices, slicing, `count()`, `index()`, concatenación, desempaquetado |
| Conjuntos | 05–06 | Elementos únicos, pertenencia, unión, intersección, diferencia, complemento y cardinalidad |
| Diccionarios | 07–08 | Claves y valores, `get()`, `update()`, `keys()`, `values()`, `items()` y estructuras anidadas |

## 🧪 Retos de práctica

- **Listas:** agrega una opción para modificar la calificación de un estudiante y vuelve a calcular el promedio.
- **Tuplas:** incorpora un nuevo dato al registro de cada aprendiz y adapta el reporte para mostrarlo.
- **Conjuntos:** agrega un cuarto lenguaje de programación y analiza las operaciones entre los cuatro conjuntos.
- **Diccionarios:** incorpora un tercer idioma a la interfaz y traduce todos los textos del menú.
- **Comparación:** representa la misma información utilizando una lista, una tupla, un conjunto y un diccionario. Explica qué cambia y qué estructura resulta más conveniente.

## 📌 Observaciones de programación

- Las **listas** son colecciones ordenadas y mutables; permiten agregar, modificar y eliminar elementos.
- Las **tuplas** son colecciones ordenadas e inmutables; una vez creadas, no se pueden modificar directamente.
- Los **conjuntos** almacenan elementos únicos y no permiten acceder a ellos mediante índices. No debe suponerse un orden específico al recorrerlos.
- Los **diccionarios** almacenan pares de clave y valor. Las claves deben ser únicas y permiten consultar directamente la información asociada.
- `sorted()` devuelve una nueva lista ordenada; no modifica la colección original.
- `input()` devuelve texto. Cuando se necesitan números, deben utilizarse conversiones como `int()` o `float()`.
- Los métodos de modificación de listas, conjuntos y diccionarios pueden cambiar la estructura original.
- Las estructuras pueden combinarse. Por ejemplo, una lista puede almacenar tuplas y un diccionario puede contener listas u otros diccionarios.
- Los ejemplos de esta unidad se enfocan en las estructuras de datos y en su uso con los elementos de programación estudiados previamente.

---

**Material de apoyo para la asignatura Fundamentos de Programación (AED-1285).**

[**⬆ Volver al inicio**](#-unidad-iv--estructuras-de-datos-en-python) · [**🏠 Repositorio principal**](../README.md)
