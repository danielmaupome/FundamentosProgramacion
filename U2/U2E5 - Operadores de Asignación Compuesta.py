# ==============================================================================
# Ejemplo 5: Uso de los operadores de Asignación Compuesta
# ==============================================================================

print("=== SISTEMA DE PUNTOS Y RECOMPENSAS EN UN JUEGO ===")

# Estado inicial del jugador
puntos = 100
multiplicador = 2
monedas = 50

print("Estado Inicial:")
print("Puntos:", puntos)
print("Monedas:", monedas)
print("---------------------------------------------------\n")

# 1. SUMA COMPUESTA (+=) -> Ganar puntos por completar una misión
# Equivalente a: puntos = puntos + 50
puntos += 50
print("1. += (Ganó 50 puntos por misión):", puntos)

# 2. RESTA COMPUESTA (-=) -> Perder vida o comprar un objeto
# Equivalente a: monedas = monedas - 15
monedas -= 15
print("2. -= (Compró una poción por 15 monedas):", monedas)

# 3. MULTIPLICACIÓN COMPUESTA (*=) -> Bonificación de poder / Doble puntuación
# Equivalente a: puntos = puntos * multiplicador
puntos *= multiplicador
print("3. *= (Doble de puntos activado):", puntos)

# 4. DIVISIÓN COMPUESTA (/=) -> Penalización por falta / Reducción a la mitad
# Equivalente a: puntos = puntos / 2
puntos /= 2
print("4. /= (Penalización: perdió la mitad de puntos):", puntos)

# 5. DIVISIÓN ENTERA COMPUESTA (//=) -> Reparto exacto de botín entre 3 aliados
# Equivalente a: monedas = monedas // 3
monedas //= 3
print("5. //= (Monedas enteras repartidas entre 3 aliados):", monedas)

# 6. MÓDULO COMPUESTO (%=) -> Sobrante del reparto anterior
# Si teníamos 11 monedas y las dividimos entre 3 (3 cada uno), nos quedan 2
monedas_restantes = 11
monedas_restantes %= 3
print("6. %= (Cambio o residuo que sobró del reparto):", monedas_restantes)