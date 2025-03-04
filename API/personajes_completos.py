import requests  # Importamos la librería requests para hacer solicitudes HTTP

class PersonajesCompletos:
    def __init__(self):
        try:
            # URL base para obtener la lista de personajes
            self.url = "https://swapi.dev/api/people"
            url_actual = self.url  # Variable para controlar la paginación

            # Bucle para recorrer todas las páginas de resultados
            while url_actual:
                respuesta = requests.get(url_actual)  # Realizamos la solicitud a la API
                peticion_json = respuesta.json()  # Convertimos la respuesta en formato JSON

                # Iteramos sobre los personajes de la página actual e imprimimos sus nombres
                for personajes in peticion_json["results"]:
                    print(personajes["name"])

                # Obtenemos la URL de la siguiente página (si existe)
                url_actual = peticion_json["next"]

        # Capturamos cualquier error inesperado durante la ejecución
        except Exception as error:
            print(f"⚠️ Error en el programa: {error}.")
