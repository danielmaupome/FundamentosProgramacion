# ==============================================================================
# Ejemplo 7: Uso del paquete random
# ==============================================================================

# Python provee de varios paquetes ya preinstalados. El paquete random provee
# de funciones que permiten obtener datos aleatorios.

# Primero importamos el paquete completo.
import random

# NOTA: a veces no nos queremos traer toda una función, entonces traemos solo
# lo que queremos, por ejemplo, para traer la función random() que usamos más
# adelante usaríamos

# from random import random

# Obtener un Número decimal entre 0 y 1, sin tomar el 1.
decimal = random.random()

# En caso de que hayamos aplicado la instrucción from random import random
# para obtener un decimal entre 0 y 1 usaríamos
# decimal = random()

# Obtener un Número entero entre 1 y 6, incluyendo estos.
dado = random.randint(1, 6)

# Elegir un elemento de una lista. La lista se explica más adelante.
colores = ["rojo", "verde", "azul"]
# Dada una lista, el método choice obtiene un valor aleatorio dentro de ellos.
color_elegido = random.choice(colores)

print(decimal, dado, color_elegido)

# NOTA FINAL: Si se usarán varias funciones del paquete, recomiendo usar import.