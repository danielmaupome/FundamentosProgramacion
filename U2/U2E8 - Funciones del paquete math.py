# ==============================================================================
# Ejemplo 8: Uso del paquete math
# ==============================================================================

# Python incorpora tambien un paquete math, con funciones muy interesantes enfocadas
# en resolver cálculos avanzados. Como se usarán múltiples funciones, usaremos import

import math

print("=== DEMOSTRACIÓN DEL PAQUETE MATH EN PYTHON ===")

# 1. CONSTANTES MATEMÁTICAS
print("1. CONSTANTES:")
print("Número Pi (pi):", math.pi)
print("Número de Euler (e):", math.e)
print("Infinito (inf):", math.inf)

# 2. REDONDEO Y TRUNCAMIENTO
numero_decimal = 7.64

print("2. FUNCIONES DE REDONDEO:")
print("Número original:", numero_decimal)
print("math.ceil()  (Redondeo hacia arriba / Techo):", math.ceil(numero_decimal))
print("math.floor() (Redondeo hacia abajo / Piso):", math.floor(numero_decimal))
print("math.trunc() (Elimina decimales / Trunca):", math.trunc(numero_decimal))

# 3. POTENCIAS Y RAÍCES
print("3. POTENCIAS, RAÍCES Y VALOR ABSOLUTO:")
print("math.pow(2, 3) (2 elevado a la 3):", math.pow(2, 3))
print("math.sqrt(25)  (Raíz cuadrada de 25):", math.sqrt(25))
print("math.fabs(-15.5) (Valor absoluto decimal):", math.fabs(-15.5))

# 4. TRIGONOMETRÍA (Los ángulos deben estar en RADIANES)
angulo_grados = 45
angulo_radianes = math.radians(angulo_grados)

print("4. TRIGONOMETRÍA:")
print("Grados a radianes:", angulo_radianes)
print("math.sin(): Seno de 45°:", math.sin(angulo_radianes))
print("math.cos(): Coseno de 45°:", math.cos(angulo_radianes))
print("math.tan(): Tangente de 45°:", math.tan(angulo_radianes))

# 5. OTRAS FUNCIONES ÚTILES
print("5. OTRAS FUNCIONES ÚTILES:")
print("math.log(10)   (Logaritmo natural de 10):", math.log(10))
print("math.log10(100)(Logaritmo en base 10):", math.log10(100))
print("math.factorial(5) (Factorial de 5!):", math.factorial(5))
print("math.gcd(12, 18)  (Máximo Común Divisor):", math.gcd(12, 18))