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
p_topic = "Working with JSON - 1- Test Ayuntamiento Madrid"
p_project = "Centros de Mayores - zona Centro"
p_ref = "https://opendata.aemet.es/dist/index.html?"
p_version = "1.0"
p_keyLib = "request & json"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0 - Datos 
url = "https://datos.madrid.es/egob/catalogo/200337-0-centros-mayores.json?distrito_nombre=CENTRO" 
endPoint = url

# 1- Primera peticion
print('==== Primera Peticion ====')
respuesta1 = requests.get(endPoint) 
print("Usando el tratamiento JSON de request se pueden hacer pocas cosas")
print(respuesta1.text) # Devuelve una cadena de texto de los datos devueltos
# print(respuesta.content())  # Return the raw bytes of the data payload
print(respuesta1.json())     # This method is convenient when the API returns JSON
print()
print("Usando la libreria JSON se pueden hacer mas cosas")
print(json.dumps(respuesta1.json(), indent=4, sort_keys=True))

print("==== Muestra una estructura compleja ====")
print("Volcamos a un objeto Python")
cmmCentro = json.loads(respuesta1.text)
print(f'El objeto devuelto es de tipo {type(cmmCentro)}')
print(cmmCentro.keys())
print('La informacion parece estar en @graph, veamos el tipo dentro de graft')
cmmCentroInfo = cmmCentro['@graph']
print(f'Dentro de @graph es de tipo {type(cmmCentroInfo)} de longitud {len(cmmCentroInfo)}')
print('Veamos uno de esos 4 , el [1]')
print(cmmCentroInfo[1])
print("Para obtener la informacion buscada, hay que hacer un 'request' adicional en '@id'")
print('==== Segunda Peticion ====')
print("Sobre cmmCentroInfo[1]['@id']")
respuesta2 = requests.get(cmmCentroInfo[1]['@id'])
print("Volcado de Respuesta 2 , formatado")
print(json.dumps(respuesta2.json(), indent=4))
