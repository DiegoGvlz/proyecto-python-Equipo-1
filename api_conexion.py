import requests

def obtener_datos():
    """Descarga y retorna los datos JSON de la API."""
    
    url = "https://pokeapi.co/api/v2/pokemon/"
    
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos

if __name__ == "__main__":
    datos = obtener_datos()
    print(datos)
