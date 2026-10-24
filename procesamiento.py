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
