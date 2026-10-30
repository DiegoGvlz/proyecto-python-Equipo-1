import matplotlib.pyplot as plt

#Gráfica 1: Cantidad de cada tipo de pokemón.
def graficar_tipos(conteo_tipos): 
    """Genera y guarda la gráfica de Pokemónes por tipo."""

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
    """Genera y guarda la gráfica de comparación de peso de los Pokémon."""
    ordenados = sorted(pokemon_organizados, key=lambda x: x["peso"], reverse=True)
    nombres = [p["nombre"] for p in ordenados]
    pesos = [p["peso"] for p in ordenados]

    # Paleta de colores variados en tonos cálidos/tierra para el peso
    colores_peso = [
        "darkorange", "chocolate", "sienna", "indianred", "crimson", 
        "saddlebrown", "coral", "firebrick", "sandybrown", "goldenrod",
        "darkkhaki", "peru", "burlywood", "tan", "rosybrown"
    ]
    # Asigna colores repetidos de la lista si hay más de 15 pokémon
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
    """Genera y guarda la gráfica de comparación de altura de los Pokémon."""
    ordenados = sorted(pokemon_organizados, key=lambda x: x["altura"], reverse=True)
    nombres = [p["nombre"] for p in ordenados]
    alturas = [p["altura"] for p in ordenados]

    # Paleta de colores variados en tonos fríos/azules para la altura
    colores_altura = [
        "steelblue", "deepskyblue", "teal", "cadetblue", "cornflowerblue",
        "mediumturquoise", "dodgerblue", "lightseagreen", "darkcyan", "royalblue",
        "skyblue", "mediumseagreen", "darkturquoise", "powderblue", "mediumslateblue"
    ]
    # Asigna colores repetidos de la lista si hay más de 15 pokémon
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
