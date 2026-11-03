import requests

def obtener_datos():
    """Descarga y retorna los datos JSON de la API."""

    # Url de la API que contiene la lista de Pokémon. 
    url = "https://pokeapi.co/api/v2/pokemon/"

    # Realiza la solicitud y establece un limite de espera de 10 segundos. 
    respuesta = requests.get(url, timeout=10)
    
    # Comprueba si la solitud fue exitosa. 
    respuesta.raise_for_status()

    # Convierte la respuesta JSON en datos que python puede utilizar. 
    datos = respuesta.json()
    return datos

# Linea que permite probar el archivo de manera independiente. 
if __name__ == "__main__":
    datos = obtener_datos()
    print(datos)
