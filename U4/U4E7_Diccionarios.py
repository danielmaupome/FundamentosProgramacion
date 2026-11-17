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
