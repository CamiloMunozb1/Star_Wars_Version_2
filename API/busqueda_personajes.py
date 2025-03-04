import requests  # Importamos la librería requests para hacer peticiones a la API

class BusquedaPersonaje:
    def __init__(self):
        try:
            # Solicitamos al usuario el ID del personaje (de 1 a 83)
            usuario_busqueda = str(input("Ingresa el ID del personaje que quieras consultar (1-83): "))

            # Construimos la URL con el ID ingresado por el usuario
            self.url = f"https://swapi.dev/api/people/{usuario_busqueda}"

            # Realizamos la solicitud a la API
            respuesta = requests.get(self.url)

            # Convertimos la respuesta en formato JSON
            peticion_json = respuesta.json()

            # Definimos las claves que queremos mostrar al usuario
            claves_deseadas = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender']

            # Iteramos sobre las claves deseadas para mostrar la información relevante
            for personaje in claves_deseadas:
                if personaje in peticion_json:
                    print(f"{personaje}: {peticion_json[personaje]}.")
                else:
                    print("Error: No se encontró el personaje, revisa nuevamente el ID ingresado.")

        # Capturamos cualquier error inesperado en la ejecución del código
        except Exception as error:
            print(f"Error en el programa: {error}.")
