# Taller Programación y Robótica en CMM BML – 2023 - Clase 20
# Resumen: Usos de API´s simples con requests
# Topicos nuevos: Python con Internet- libreria request
# Fecha JCSP 2023 09 27
# Licencia : CC BY-NC-SA 4.0
# Version 1.0


# IMPORTAR modulo que maneja HTTP 
import requests

url = "https://datos.madrid.es/egob/catalogo/200337-0-centros-mayores.json?distrito_nombre=CENTRO" 
endPoint = url
respuesta = requests.get(endPoint) 

print(respuesta.text) # Devuelve una cadena de texto de los datos devueltos
#print(respuesta.content())  # Return the raw bytes of the data payload
print(respuesta.json())     # This method is convenient when the API returns JSON
