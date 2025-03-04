# Importamos las clases desde la carpeta API
from API.busqueda_personajes import BusquedaPersonaje  # Clase para buscar un personaje específico
from API.personajes_completos import PersonajesCompletos  # Clase para obtener la lista de personajes

# Bucle infinito para mantener el programa en ejecución hasta que el usuario decida salir
while True:
    # Imprimimos el menú principal
    print("""
            BIENVENIDO A LA ENCICLOPEDIA DE STAR WARS
            1. Investigar personaje.
            2. Personajes completos
            3. Salir
    """)

    try:
        # Solicitamos la opción del usuario y convertimos la entrada en un número entero
        usuario = int(input("Ingresa una opción: "))

        # Opción 1: Buscar información de un personaje específico
        if usuario == 1:
            BusquedaPersonaje()  # Llamamos a la clase directamente

        # Opción 2: Mostrar la lista de todos los personajes disponibles
        elif usuario == 2:
            PersonajesCompletos()  # Llamamos a la clase directamente

        # Opción 3: Salir del programa
        elif usuario == 3:
            print("Gracias por visitarnos, vuelve cuando quieras. ¡Que la Fuerza te acompañe!")
            break  # Salimos del bucle y terminamos el programa

        # Manejo de opciones fuera del rango 1-3
        else:
            print("Ingresa una opción válida en el rango de 1-3.")

    # Manejo del error si el usuario ingresa un valor no numérico
    except ValueError:
        print("⚠️ Error: Ingresa un número válido.")

    # Captura de cualquier otro error inesperado
    except Exception as error:
        print(f"Error en el programa: {error}.")
