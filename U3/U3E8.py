texto = "Torneo de fútbol Sub23"
print(f"{texto:=^30}")
edad = int(input("Edad: "))
permiso = input("Tiene Permiso? (s/n): ").upper()
if edad <= 23 or permiso == "S":
    print("Acceso autorizado")
else:
    print("Acceso denegado")