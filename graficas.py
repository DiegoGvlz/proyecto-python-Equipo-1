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
      "Normal": "gray",
      "Fuego": "red", 
      "Agua": "blue",
      "Eléctrico": "gold",
      "Planta": "green",
      "Hielo": "cyan", 
      "Lucha": "brown",
      "Veneno": "purple",
      "Tierra": "saddlebrown",
      "Volador": "skyblue",
      "Psíquico": "hotpink",
      "bicho": "yellowgreen",
      "Roca": "dimgray",
      "Fantasma": "indigo",
      "Dragón": "darkorange",
      "Siniestro": "black", 
      "Acero": "silver",
      "Hada": "pink"
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
#Gráfica 3: Alturas de los pokemón.
