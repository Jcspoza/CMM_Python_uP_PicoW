# Taller Programación y Robótica en CMM BML – 2024 - Clase 28
# Resumen: Consumo de API´s 
# Topicos nuevos: Python con Internet- libreria request + libreria json
# Fecha JCSP 2024 03 05
# Licencia : CC BY-NC-SA 4.0
# Version 1.0


# IMPORTAR modulo que maneja HTTP 
import requests
import json

# 1- Conseguir la informacion
url = "https://datos.madrid.es/egob/catalogo/200337-0-centros-mayores.json?distrito_nombre=CENTRO" 
endPoint = url
respuesta = requests.get(endPoint) 

print(respuesta.text) # Devuelve una cadena de texto de los datos devueltos
print(respuesta.content())  # Return the raw bytes of the data payload
print(respuesta.json())     # This method is convenient when the API returns JSON

print(json.dumps(respuesta.json(), indent=4))