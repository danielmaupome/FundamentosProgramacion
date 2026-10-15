# ==============================================================================
# Ejemplo 2: Tipos de datos
# ==============================================================================

# Python no  tiene un tipo de datos definido, sino que el intérprete detecta en función del valor

# Se declaran una serie de variables
materia = "Fundamentos de Programación"
alumno = "Linus Torvalds"
clave_mat = "AED - 1285"
horas_teoria = 2
horas_practica = 3

# Operación + entre str (cadenas) es concatenación (pegar las dos cadenas)
cve_mat = clave_mat + " " +materia

# Operación + entre numéricos (enteros y flotantes) es suma.
creditos_satca = horas_teoria + horas_practica


promedio = (85 + 92 + 83 + 94 + 89)/5
isAlumnoInscrito = True


print ("La materia ", cve_mat, " es de ",creditos_satca, "horas.")
print("El alumno ", alumno, "cuenta con estatus ", isAlumnoInscrito)
print("El promedio del alumno es de ", promedio)

# Podemos saber el tipo de variable con el método type()
print("Tipo de la variable materia: ", type(materia))
print("Tipo de la variable horas_teoria: ", type(horas_teoria))
print("Tipo de la variable promedio: ", type(promedio))
print("Tipo de la variable isAlumnoInscrito: ", type(isAlumnoInscrito))