# ==============================================================================
# Ejemplo 10: Distribución de espacios en Python
# ==============================================================================

# En python puedo declarar un espacio para imprimir de forma distribuida.

# Espacios entre Texto / Cadenas:
#  - :20   -> Define un ancho fijo de 20 caracteres
#  - :<20  -> Alinea a la izquierda
#  - :>20  -> Alinea a la derecha
#  - :^20  -> Centra el texto
producto1 = "Laptop"
precio1 = 15999.90
disponible1 = True

producto2 = "Mouse Optico"
precio2 = 350.50
disponible2 = False

# Texto al vuelo, centrado en 43 espacios.
print(f"\n{'=== INVENTARIO DE TIENDA ===':^43}")
# Creación de espacios tipo columnas
print(f"{'PRODUCTO':<15} | {'PRECIO':>10} | {'DISPONIBLE':^12}")
print("-" * 43)

# Impresion de salida respetando las alineaciones (Izq. | Der. | Centro.)
print(f"{producto1:<15} | ${precio1:>9,.2f} | {str(disponible1):^12}")
print(f"{producto2:<15} | ${precio2:>9,.2f} | {str(disponible2):^12}")