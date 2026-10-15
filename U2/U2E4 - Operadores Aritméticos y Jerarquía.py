# ==============================================================================
# Ejemplo 4: Operadores Aritméticos
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. ENTRADA DE DATOS POR EL USUARIO
# ------------------------------------------------------------------------------
# Se usa input() para recibir datos del usuario y float() para convertirlos
# a números decimales y así permitir cualquier tipo de cálculo.

print("=== INGRESO DE DATOS ===")
num1 = float(input("Ingresa el primer número (num1): "))
num2 = float(input("Ingresa el segundo número (num2): "))
num3 = float(input("Ingresa el tercer número (num3): "))

# Si deseo repetir una cadena un n número de veces, lo hago de esta forma.
print("-" * 50)


# ------------------------------------------------------------------------------
# 2. OPERACIONES ARITMÉTICAS BÁSICAS
# ------------------------------------------------------------------------------
print("\n=== OPERACIONES ARITMÉTICAS BÁSICAS ===")

# Suma (+)
suma = num1 + num2
print("Suma (num1 + num2):", suma)

# Resta (-)
resta = num1 - num2
print("Resta (num1 - num2):", resta)

# Multiplicación (*)
multiplicacion = num1 * num2
print("Multiplicación (num1 * num2):", multiplicacion)

# División Real (/) -> Siempre devuelve un número decimal (float)
division = num1 / num2
print("División real (num1 / num2):", division)

# División Entera (//) -> Devuelve solo la parte entera del cociente
division_entera = num1 // num2
print("División entera (num1 // num2):", division_entera)

# Módulo (%) -> Devuelve el residuo/resto de la división
modulo = num1 % num2
print("Módulo o residuo (num1 % num2):", modulo)

# Potencia (**) -> Eleva el primer número al cubo (exponente 3)
potencia_cubo = num1 ** 3
print("Potencia al cubo del primer número (num1 ** 3):", potencia_cubo)
print("-" * 50)


# ------------------------------------------------------------------------------
# 3. DEMOSTRACIÓN DE LA JERARQUÍA DE OPERADORES
# ------------------------------------------------------------------------------
# Regla de jerarquía en Python:
# 1. Paréntesis ()
# 2. Exponenciación (**)
# 3. Multiplicación (*), División (/), División Entera (//) y Módulo (%)  [De izq. a der.]
# 4. Suma (+) y Resta (-)  [De izq. a der.]

print("\n=== DEMOSTRACIÓN DE LA JERARQUÍA DE OPERADORES ===")

# Caso A: Sin paréntesis
# Primero se evalúa (num2 * num3) y la potencia (num1 ** 3).
# Luego se realizan las sumas de izquierda a derecha.
operacion_sin_parentesis = num1 + num2 * num3 + num1 ** 3
print("Operación SIN paréntesis (num1 + num2 * num3 + num1 ** 3):")
print("Resultado:", operacion_sin_parentesis)

# Caso B: Con paréntesis agrupando sumas
# Los paréntesis obligan a evaluar primero (num1 + num2) antes de multiplicar.
operacion_con_parentesis = (num1 + num2) * num3 + num1 ** 3
print("\nOperación CON paréntesis ((num1 + num2) * num3 + num1 ** 3):")
print("Resultado:", operacion_con_parentesis)

# Caso C: Expresión compleja para analizar paso a paso
# Estructura: (num1 + num2) * (num3 ** 2) / num2
# 1º Se resuelven los paréntesis: el primero (num1 + num2) y dentro del segundo la potencia (num3 ** 2).
# 2º Se realiza la multiplicación del resultado por la potencia.
# 3º Se divide el resultado entre num2.
operacion_compleja = (num1 + num2) * (num3 ** 2) / num2
print("\nOperación Compleja ((num1 + num2) * (num3 ** 2) / num2):")
print("Resultado:", operacion_compleja)
print("=" * 50)