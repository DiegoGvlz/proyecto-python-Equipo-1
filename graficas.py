import matplotlib.pyplot as plt

#Gráfica 1: Cantidad de cada tipo de pokemón.
def graficar_tipos(conteo_tipos): 
    """Genera y guarda la gráfica de barras de Pokemónes por tipo con sus respectivos colores."""

    resultados = sorted(
        conteo_tipos.items(),
        key=lambda elemento: elemento[1],
        reverse=True
    )
 
    tipos = [resultado[0] for resultado in resultados]
    cantidades = [resultado[1] for resultado in resultados]

    #Asigno colores a cada tipo de Pokemón
    colores_tipos = {
      "normal": "gray",
      "fire": "red", 
      "water": "blue",
      "electric": "gold",
      "grass": "green",
      "ice": "cyan", 
      "fighting": "brown",
      "poison": "purple",
      "ground": "saddlebrown",
      "flying": "skyblue",
      "psychic": "hotpink",
      "bug": "yellowgreen",
      "rock": "dimgray",
      "ghost": "indigo",
      "dragon": "darkorange",
      "dark": "black", 
      "steel": "silver",
      "fairy": "pink"
    }

    #Obtenemos el color correspondiente de cada tipo.
    colores = [
        colores_tipos.get(tipo, "gray")
        for tipo in tipos
    ]
     
    plt.figure(figsize=(10, 6))
    plt.bar(tipos, cantidades, color=colores)
    plt.title("Cantidad de Pokemónes por tipo")
    plt.xlabel("Tipos de Pokemón")
    plt.ylabel("Cantidad de Pokemón")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafica1.png")
    plt.show()


#Gráfica 2: Comparación de peso entre pokemónes.
def graficar_peso(pokemon_organizados):
    """Genera y guarda la gráfica de barras con la comparación de peso de los Pokémon analizados."""
    ordenados = sorted(pokemon_organizados, key=lambda x: x["peso"], reverse=True)
    nombres = [p["nombre"] for p in ordenados]
    pesos = [p["peso"] for p in ordenados]

    colores_peso = [
        "darkorange", "chocolate", "sienna", "indianred", "crimson", 
        "saddlebrown", "coral", "firebrick", "sandybrown", "goldenrod",
        "darkkhaki", "peru", "burlywood", "tan", "rosybrown"
    ]
    colores = [colores_peso[i % len(colores_peso)] for i in range(len(nombres))]

    plt.figure(figsize=(10, 5))
    plt.bar(nombres, pesos, color=colores, edgecolor="black")
    plt.title("Comparación de Peso de los Pokémon")
    plt.xlabel("Pokémon")
    plt.ylabel("Peso (kg)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("grafica2.png")
    plt.show()


#Gráfica 3: Alturas de los pokemón.
def graficar_altura(pokemon_organizados):
    """Genera y guarda la gráfica de barras con la comparación de altura de los Pokémon analizados."""
    ordenados = sorted(pokemon_organizados, key=lambda x: x["altura"], reverse=True)
    nombres = [p["nombre"] for p in ordenados]
    alturas = [p["altura"] for p in ordenados]

    colores_altura = [
        "steelblue", "deepskyblue", "teal", "cadetblue", "cornflowerblue",
        "mediumturquoise", "dodgerblue", "lightseagreen", "darkcyan", "royalblue",
        "skyblue", "mediumseagreen", "darkturquoise", "powderblue", "mediumslateblue"
    ]
    colores = [colores_altura[i % len(colores_altura)] for i in range(len(nombres))]

    plt.figure(figsize=(10, 5))
    plt.bar(nombres, alturas, color=colores, edgecolor="navy")
    plt.title("Comparación de Altura de los Pokémon")
    plt.xlabel("Pokémon")
    plt.ylabel("Altura (m)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("grafica3.png")
    plt.show()


#Gráfica 4: Estadísticas base de un Pokémon específico.
def graficar_estadisticas_pokemon(datos_pokemon):
    """
    Genera y guarda una gráfica de barras con las estadísticas base 
    (HP, Ataque, Defensa, etc.) de un Pokémon específico consultado por su ID.
    """
    nombres_stats = []
    valores_stats = []
    
    # Recorremos la lista de estadísticas para extraer sus nombres y valores base
    for item in datos_pokemon.get("stats", []):
        stat_nombre = item["stat"]["name"].replace("-", " ").capitalize()
        stat_valor = item["base_stat"]
        nombres_stats.append(stat_nombre)
        valores_stats.append(stat_valor)
        
    nombre_pkmn = datos_pokemon.get("name", "Pokémon").capitalize()

    plt.figure(figsize=(10, 6))
    plt.bar(nombres_stats, valores_stats, color="mediumseagreen", edgecolor="black", alpha=0.8)
    plt.title(f"Estadísticas Base de {nombre_pkmn}")
    plt.xlabel("Estadísticas")
    plt.ylabel("Valor Base")
    plt.ylim(0, max(valores_stats) + 20)
    plt.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafica4.png")
    plt.show()
