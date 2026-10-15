# ==============================================================================
# Ejemplo 6: Operaciones sobre cadenas de caracteres
# ==============================================================================


# Entrada con espacios extras y formato irregular (típico error de un usuario)
texto_original = "  hOLa mUnDo dESde pyTHon!  "

print("--- 1. DEMOSTRACIÓN DE MÉTODOS BÁSICOS ---")
print("Texto original (entre comillas para ver espacios):", f"'{texto_original}'")

# .strip() -> Elimina espacios en blanco al inicio y al final
texto_limpio = texto_original.strip()
print(".strip()  -> Quita espacios extremos:", f"'{texto_limpio}'")

# .upper() -> Convierte todo el texto a MAYÚSCULAS
print(".upper()  -> Todo a mayúsculas:    ", texto_limpio.upper())

# .lower() -> Convierte todo el texto a minúsculas
print(".lower()  -> Todo a minúsculas:    ", texto_limpio.lower())

# .title() -> Formato de Título (Primera letra de cada palabra en mayúscula)
print(".title()  -> Formato Título:       ", texto_limpio.title())

# .replace() -> Reemplaza un fragmento de texto por otro
print(".replace()-> Reemplazar 'Mundo' por 'Estudiantes':", texto_limpio.replace("mUnDo", "Estudiantes"))


print("\n--- 2. DEMOSTRACIÓN DE LA INMUTABILIDAD ---")

# Aplicamos un método directamente sobre la variable original
texto_original.upper()

# Al imprimir la variable original, comprobamos que NO cambió
print("Texto original después de ejecutar .upper():", f"'{texto_original}'")

# Para conservar los cambios, DEBEMOS reasignar el resultado a una nueva variable
# o a la misma variable original:
texto_modificado = texto_original.strip().title()
print("Variable con el resultado reasignado:      ", f"'{texto_modificado}'")