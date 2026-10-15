calificacion = int(input("Calificación: "))
if calificacion < 0 or calificacion > 100:
    print("Calificación no válida")
elif calificacion >= 95:
    print("Excelente")
elif calificacion >= 85:
    print("Notable")
elif calificacion >= 75:
    print("Bueno")
elif calificacion >= 70:
    print("Suficiente")
else:
    print("Insuficiente - Competencia no alcanzada")