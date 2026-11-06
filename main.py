import api_conexion
import procesamiento
import graficas

def main():
    # 1. Obtener datos crudos de la API
    datos = api_conexion.obtener_datos()
    
    # 2. Mantener la parte clásica (procesar e imprimir resultado)
    resultado = procesamiento.procesar(datos)
    print("Resultado del procesamiento:", resultado)

    # 3. Organizar los datos y contar tipos específicamente para las gráficas
    pokemon_organizados = procesamiento.organizar_datos(datos)
    conteo_tipos = procesamiento.contar_tipos(pokemon_organizados)

    # 4. Generar y guardar las 3 gráficas principales
    graficas.graficar_tipos(conteo_tipos)
    graficas.graficar_peso(pokemon_organizados)
    graficas.graficar_altura(pokemon_organizados)

    # 5. Generar la gráfica de estadísticas de un Pokémon específico (fijo en el código)
    pokemon_elegido = "charizard"  # Puedes cambiar el nombre aquí por el que prefieras (ej. "pikachu", "mewtwo")
    print(f"\n Generando gráfica de estadísticas de : {pokemon_elegido.capitalize()} ")
    
    datos_individuales = api_conexion.obtener_estadisticas_pokemon(pokemon_elegido)
    if datos_individuales:
        graficas.graficar_estadisticas_pokemon(datos_individuales)

if __name__ == "__main__":
    main()
