# Taller Programación y Robótica en CMM BML – 2023 - Clase 20
# Resumen: Usar los API´s que normalmente vienen como JSON - ejemplo 1
# Topicos nuevos: libreria json
# Ref Tuytorial JSON sencillo : https://www.freecodecamp.org/espanol/news/python-leer-archivo-json-como-cargar-json-desde-un-archivo-y-procesar-dumps/
# Fecha inicio 2024 03 11
# Licencia : CC BY-NC-SA 4.0
# Version 1.0

# IMPORTAR modulo que maneja JSON
import json

# 0- Cadena de caracteres en el formato JSON usada como ejemplo
datos_JSON =  """
{
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "queso extra", "pepperoni", "albahaca"],
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": "455-344-234",
		"correo": "janedoe@email.com"
	}
}
"""

# 1- Convertir cadena de caracteres JSON a un diccionario
datos_diccionario = json.loads(datos_JSON)

# 2- Mostrar resultado
print('==== Cadena JSON original ====')
print(datos_JSON + '\n')
print('==== Visualizar resultado de conversion a Diccionario ====')
print(datos_diccionario)
print()

print('==== Recorrido del Diccionario clave a clave ====')
for clave in datos_diccionario:
    print(f'Valor de la clave: {clave} - Tipo del contenido: {type(datos_diccionario[clave])}')
    print(f'Contenido: {datos_diccionario[clave]}')
    
