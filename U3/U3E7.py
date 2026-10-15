opcion = input("Elige A, B o C: ").upper()
match opcion:
    case "A":
        print("Alta")
    case "B":
        print("Baja")
    case "C":
        print("Consulta")
    case _:
        print("Opción inválida")
