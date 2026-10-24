import api_conexion 
import procesamiento 

datos = api_conexion.obtener_datos() 
resultado = procesamiento.procesar(datos) 
print(resultado)
