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

    # Recorre la lista de Pokemón obtenida de la API.
    resultados = datos.get("results", [])
    
    for pokemon in resultados:
        # Consulta la dirección individual de cada Pokemón.
        respuesta = requests.get(pokemon["url"], timeout=10)
        respuesta.raise_for_status()
        datos_pokemon = respuesta.json()

        # Guarda todos los tipos que tiene el Pokemón.
        tipos = []
        for tipo in datos_pokemon.get("types", []):
            tipos.append(tipo["type"]["name"])

        # Guarda los datos organizados en un diccionario.
        pokemon_organizados.append({
            "nombre": datos_pokemon.get("name", "").capitalize(), 
            "tipos": tipos, +
            # La API proporciona el peso en hectogramos, asi que lo convertimos a kilogramos. 
            "peso": datos_pokemon.get("weight", 0) / 10,
            # La API proporciona la altura en decímetros, asi que lo convertimos a metros. 
            "altura": datos_pokemon.get("height", 0) / 10
        })

    return pokemon_organizados


def contar_tipos(pokemon_organizados):
    """Cuenta cuántos pokemón pertenecen a cada tipo."""
    conteo_tipos = {}

    for pokemon in pokemon_organizados: 
        for tipo in pokemon["tipos"]:
            # Si el tipo todavía no existe, comienza su contador en cero. 
            if tipo not in conteo_tipos:
                conteo_tipos[tipo] = 0
            # Aumenta el contador del tipo correspondiente. 
            conteo_tipos[tipo] += 1
    return conteo_tipos

