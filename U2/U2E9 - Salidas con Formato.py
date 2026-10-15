# ==============================================================================
# Ejemplo 9: Salidas formateadas (f-strings)
# ==============================================================================

# Datos de un producto para una tienda
producto = "Laptop Gamer"
precio = 18999.50
descuento = 0.15  # 15%
piezas = 3

# Cálculos
precio_final = precio * (1 - descuento)
total = precio_final * piezas


# -------------------------------------------------------------
# 1. FORMA TRADICIONAL (Sin formato / Print normal con comas)
# -------------------------------------------------------------
print("=== IMPRESIÓN NORMAL (Sin formato) ===")
print("Producto:", producto)
print("Precio original: $", precio)
print("Descuento:", descuento * 100, "%")
print("Precio con descuento: $", precio_final)
print("Total a pagar por", piezas, "piezas: $", total)
print("---------------------------------------------------\n")

# Podemos observar que, con la salida normal, cuando trabajamos datos monetarios
# podemos tener demasiados decimales, pero en la realidad se manejan 2 decimales
# por convención, así que, nos conviene usar los f-strings, que son cadenas con
# formato definido por el usuario.


# -------------------------------------------------------------
# 2. FORMA MODERNA (Con f-strings / Salida formateada)
# -------------------------------------------------------------
print("=== IMPRESIÓN FORMATEADA (f-strings) ===")

# Inserción básica de variables dentro del texto
# justo despues de abrir el paréntesis se coloca una f, que le indica al intérprete
# que haremos uso de una salida formateada. La variable que saldrá impresa se coloca
# dentro de las comillas, pero encerrada entre llaves {}
print(f"Producto: {producto}")

# Control de decimales en números flotantes (:.2f)
# Aqui la variable que es tipo decimal se limita a tener dos decimales. Para lograrlo,
# justo despues de la variable se colocan :, que significa que esa variable tendrá un
# formato especial. Al usar .2 decimos que el valor se muestra con sólo 2 decimales.
# La f indica que es un numero de punto flotante.
print(f"Precio original: ${precio:.2f}")

# Expresiones y operaciones matemáticas directas dentro de las llaves
# Observa que dentro de las {} puedo hacer operaciones.
print(f"Descuento aplicable: {descuento * 100:.0f}%")
print(f"Precio con descuento: ${precio_final:.2f}")

# Alineación y formato completo de un ticket de compra
# Aquí, como puedes ver, despues del : usamos una , para indicar que los miles se
# separarán por , y mantenemos el .2f para los decimales.
print(f"Total a pagar por {piezas} piezas: ${total:,.2f}")
print("---------------------------------------------------")