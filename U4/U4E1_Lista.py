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