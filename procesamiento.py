import requests

#Se define la funcion llamada procesar, recibe un parametro (datos)
def procesar(datos):
    """Limpieza y organizacion de datos API."""
    nombres_procesados = []
    
    # Extrae la lista de pokemons de la llave 'results'
    resultados = datos.get('results', [])
    
    for pokemon in resultados:
        # se obtiene el nombre y se le aplica strip y capitalize (Strip elimina espacios y pone la primera letra en mayúscula y capitalize 
        # pone la primera letra en mayúscula y el resto en minúscula)
        nombre = pokemon.get('name', '')
        nombres_procesados.append(nombre.strip().capitalize())
    
    return nombres_procesados


def organizar_datos(datos):
    """Obtiene y organiza los datos individuales de cada pokemón."""
    pokemon_organizados = []
    resultados = datos.get("results", [])
    
    for pokemon in resultados:
        respuesta = requests.get(pokemon["url"], timeout=10)
        respuesta.raise_for_status()
        datos_pokemon = respuesta.json()

        tipos = []
        for tipo in datos_pokemon.get("types", []):
            tipos.append(tipo["type"]["name"])

        pokemon_organizados.append({
            "nombre": datos_pokemon.get("name", "").capitalize(), 
            "tipos": tipos, 
            "peso": datos_pokemon.get("weight", 0) / 10,
            "altura": datos_pokemon.get("height", 0) / 10
        })

        return pokemon_organizados

