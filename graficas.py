import matplotlib.pyplot as plt

#Gráfica 1: Cantidad de cada tipo de pokemón.
def graficar_tipos(conteo_tipos): 
  """Genera y guarda la gráfica de Pokemón por tipo."""
    tipos = list(conteo_tipos.keys())
    cantidades = list(conteo_tipos.values())

    plt.figure(figsize=(10, 6))
    plt.bar(tipos, cantidades)
    plt.title("Cantidad de Pokemón por tipo")
    plt.xlabel("Tipo de Pokemón")
    plt.ylabel("Cantidad de Pokemón")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafica1.png")
    plt.show()
#Gráfica 2: Comparación de peso entre pokemónes.
#Gráfica 3: Alturas de los pokemón.
