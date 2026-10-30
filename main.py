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

    # 4. Generar y guardar las 3 gráficas
    graficas.graficar_tipos(conteo_tipos)
    graficas.graficar_peso(pokemon_organizados)
    graficas.graficar_altura(pokemon_organizados)

if __name__ == "__main__":
    main()
