import requests

def obtener_datos():
    """Descarga y retorna los datos JSON de la API."""
    url = "https://pokeapi.co/api/v2/pokemon/"
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos


def obtener_estadisticas_pokemon(id_o_nombre):
    """
    Consulta la PokéAPI para obtener los datos detallados y 
    estadísticas base de un Pokémon específico usando su ID o nombre exacto.
    """
    # Si le pasas un número (ej. 6), lo convierte a texto de forma segura
    url = f"https://pokeapi.co/api/v2/pokemon/{str(id_o_nombre).lower().strip()}"
    respuesta = requests.get(url, timeout=10)
    
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        print(f"No se encontró al Pokémon '{id_o_nombre}'.")
        return None


if __name__ == "__main__":
    datos = obtener_datos()
    print(datos)
