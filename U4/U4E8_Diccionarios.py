# U4E8_Diccionarios.py
# Proyecto: Interfaz bilingüe para una aplicación
# Idiomas disponibles: español e inglés
#
# El programa utiliza diccionarios anidados para almacenar
# los textos de la interfaz en diferentes idiomas.
# El usuario puede cambiar el idioma mientras utiliza la aplicación.

# 1. Diccionario principal de idiomas
# Cada idioma contiene otro diccionario con los textos de la interfaz.

idiomas = {
    "es": {
        "nombre_app": "MI APLICACIÓN",
        "bienvenida": "¡Bienvenido!",
        "menu_titulo": "MENÚ PRINCIPAL",
        "opcion_perfil": "Ver perfil",
        "opcion_notificaciones": "Consultar notificaciones",
        "opcion_configuracion": "Configuración",
        "opcion_idioma": "Cambiar idioma",
        "opcion_salir": "Salir",
        "seleccione": "Seleccione una opción: ",
        "perfil_titulo": "PERFIL DEL USUARIO",
        "nombre": "Nombre",
        "carrera": "Carrera",
        "institucion": "Institución",
        "notificaciones_titulo": "NOTIFICACIONES",
        "sin_notificaciones": "No tiene notificaciones nuevas.",
        "configuracion_titulo": "CONFIGURACIÓN",
        "idioma_actual": "Idioma actual",
        "idioma_espanol": "Español",
        "idioma_ingles": "Inglés",
        "seleccionar_idioma": "Seleccione el idioma (es/en): ",
        "idioma_cambiado": "Idioma actualizado correctamente.",
        "idioma_no_valido": "Idioma no válido.",
        "opcion_no_valida": "Opción no válida. Intente nuevamente.",
        "despedida": "Gracias por utilizar la aplicación. ¡Hasta pronto!"
    },

    "en": {
        "nombre_app": "MY APPLICATION",
        "bienvenida": "Welcome!",
        "menu_titulo": "MAIN MENU",
        "opcion_perfil": "View profile",
        "opcion_notificaciones": "Check notifications",
        "opcion_configuracion": "Settings",
        "opcion_idioma": "Change language",
        "opcion_salir": "Exit",
        "seleccione": "Select an option: ",
        "perfil_titulo": "USER PROFILE",
        "nombre": "Name",
        "carrera": "Degree program",
        "institucion": "Institution",
        "notificaciones_titulo": "NOTIFICATIONS",
        "sin_notificaciones": "You have no new notifications.",
        "configuracion_titulo": "SETTINGS",
        "idioma_actual": "Current language",
        "idioma_espanol": "Spanish",
        "idioma_ingles": "English",
        "seleccionar_idioma": "Select language (es/en): ",
        "idioma_cambiado": "Language updated successfully.",
        "idioma_no_valido": "Invalid language.",
        "opcion_no_valida": "Invalid option. Please try again.",
        "despedida": "Thank you for using the application. See you soon!"
    }
}

# 2. Información del usuario
# Este diccionario representa los datos que mostraría la aplicación.
usuario = {
    "nombre": "Daniel Maupomé",
    "carrera": "Ingeniería en Sistemas Computacionales",
    "institucion": "TecNM"
}

# 3. Notificaciones de ejemplo
notificaciones = [
    "Tienes una nueva actividad disponible.",
    "Tu perfil se encuentra actualizado."
]

# 4. Seleccionar el idioma inicial
idioma = "es"

print("===================================")
print(idiomas[idioma]["nombre_app"])
print("===================================")
print(idiomas[idioma]["bienvenida"])

# 5. Menú principal
while True:

    # Obtener los textos del idioma seleccionado
    textos = idiomas[idioma]

    print("\n===================================")
    print(textos["menu_titulo"])
    print("===================================")

    print("1.", textos["opcion_perfil"])
    print("2.", textos["opcion_notificaciones"])
    print("3.", textos["opcion_configuracion"])
    print("4.", textos["opcion_idioma"])
    print("5.", textos["opcion_salir"])

    opcion = input(textos["seleccione"])

    # 6. Consultar el perfil del usuario
    if opcion == "1":

        print("\n==========", textos["perfil_titulo"], "==========")
        print(textos["nombre"] + ":", usuario["nombre"])
        print(textos["carrera"] + ":", usuario["carrera"])
        print(textos["institucion"] + ":", usuario["institucion"])

    # 7. Consultar notificaciones
    elif opcion == "2":

        print("\n==========", textos["notificaciones_titulo"], "==========")

        if len(notificaciones) == 0:
            print(textos["sin_notificaciones"])
        else:
            for notificacion in notificaciones:
                print("-", notificacion)

    # 8. Consultar configuración
    elif opcion == "3":

        print("\n==========", textos["configuracion_titulo"], "==========")

        if idioma == "es":
            nombre_idioma = textos["idioma_espanol"]
        else:
            nombre_idioma = textos["idioma_ingles"]

        print(textos["idioma_actual"] + ":", nombre_idioma)

    # 9. Cambiar el idioma de la aplicación
    elif opcion == "4":

        nuevo_idioma = input(textos["seleccionar_idioma"]).strip().lower()

        if nuevo_idioma in idiomas:
            idioma = nuevo_idioma
            print(idiomas[idioma]["idioma_cambiado"])
        else:
            print(textos["idioma_no_valido"])

    # 10. Salir de la aplicación
    elif opcion == "5":

        print("\n" + textos["despedida"])
        break

    else:
        print(textos["opcion_no_valida"])
