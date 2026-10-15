# ==============================================================================
# Ejemplo 3: Ingreso de valores desde teclado
# ==============================================================================

print("--- Entrega de Equipo de Seguridad ---")

# Para ingresar valores usamos la función input, que lee una cadena de caracteres.
id_emp = input("Ingrese el ID de Empleado: ")
nombre = input("Ingrese el nombre del empleado: ")

# Si deseamos que el valor que ingresemos sea reconocido como número entero, usamos int(input("Mensaje"))
edad = int(input("¿Cuál es la edad del empleado?: "))

# Si deseamos que el valor que ingresemos sea reconocido como número real, usamos float(input("Mensaje"))
talla = float(input("¿Cuál es la talla de calzado del empleado?: "))

print("Al empleado ", nombre, "se le hace entrega de: ")
print("Casco,\nGuantes,\nLentes,\nBotas del ", talla)