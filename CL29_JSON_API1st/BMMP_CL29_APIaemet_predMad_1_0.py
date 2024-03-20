# Taller Programación y Robótica en CMM BML – 2024 - Clase 29
# Resumen: Consumo de API´s 
# Topicos nuevos: Python con Internet- libreria request + libreria json
# Fecha JCSP 2024 03 05
# Licencia : CC BY-NC-SA 4.0
# Version 1.0

# IMPORTAR modulo que maneja HTTP y el que maneja JSON
import requests
import json

# Informative block - start
p_topic = "Working with JSON - 2- Test AEMET"
p_project = "Prediccion Madrid capital"
p_ref = "https://opendata.aemet.es/dist/index.html?"
p_version = "1.0"
p_keyLib = "request & json"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0 - Datos prediccion madrid
url =  "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/28079"

headers = {
    'accept': "application/json",
    'api_key': "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqY3Nwb3phQGdtYWlsLmNvbSIsImp0aSI6IjAyZGJmMGE0LWE2YmItNGI4Ni04ZDA1LTFmZDliNTMxNjliZiIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNjg5MjQ2Njg1LCJ1c2VySWQiOiIwMmRiZjBhNC1hNmJiLTRiODYtOGQwNS0xZmQ5YjUzMTY5YmYiLCJyb2xlIjoiIn0.uTM_G_sodQuXRX83njJvqnKOuTQwQOCveabI1Z9Ygfo"
    }

# 1- Primera peticion
print('==== Primera Peticion ====')
print("Para obtener la informacion buscada, hay que hacer un 'request' adicional en 'datos'")
# response = requests.request("GET", url, headers=headers)
respuesta1 = requests.get(url, headers=headers)
print(json.dumps(respuesta1.json(), indent=4))

print('==== Segunda Peticion ====')
print("Sobre respuesta1.json()['datos']")
# r2 = requests.request("GET", response.json()['datos'])
respuesta2 = requests.get(respuesta1.json()['datos'])

print("Volcado de Respuesta 2 , formatado")
print(json.dumps(respuesta2.json(), indent=4))

print("==== Muestra una estructura muy compleja ====")
print("Volcamos a un objeto Python")
previstoMad = json.loads(respuesta2.text)
print("Es una lista , de 1 solo miembro, que es un diccionario con las siguientes claves")
print(previstoMad[0].keys())
print("Nos centramos en ['prediccion']['dia'][0].keys())")
print(previstoMad[0]['prediccion']['dia'][0].keys())
print("y por fin solo en temperatura ['prediccion']['dia'][0]['fecha']")
print()
print(previstoMad[0]['prediccion']['dia'][0]['fecha'], previstoMad[0]['prediccion']['dia'][0]['temperatura'])