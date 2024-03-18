# Taller Programación y Robótica en CMM BML – 2023 - Clase 20
# Resumen: Usar los API´s que normlmente vienen como JSON - ejemplo 2
# Topicos nuevos: libreria json
# Ref Tuytorial JSON sencillo : https://www.freecodecamp.org/espanol/news/python-leer-archivo-json-como-cargar-json-desde-un-archivo-y-procesar-dumps/
# Fecha inicio 2024 03 11
# Licencia : CC BY-NC-SA 4.0
# Version 1.0


# IMPORTAR modulo que maneja JSON
import json

# 0 - Diccionario en Python usado como ejemplo
cliente = {
    "nombre": "Nora",
    "edad": 56,
    "id": "45355",
    "color_ojos": "verdes",
    "usa_lentes": False
}

# 1- Mostrar Dicionario original
print('==== Diccionario original ====')
print(cliente)
print('==== Recorrido del Diccionario original ====')
for clave in cliente:
    print(clave, cliente[clave])

# 2- Conversion a JSON
print('==== Conversion a JSON ====')
cliente_JSON = json.dumps(cliente)
clientei_JSON = json.dumps(cliente, indent=4)
clienteoi_JSON = json.dumps(cliente, indent=4, sort_keys=True)
print(cliente_JSON)
print(f'Tipo de datos de la variable a la que hemos convertido el Diccionario es: {type(cliente_JSON)}')
print('Ahora la conversion a JSON con indentacion')
print(clientei_JSON)
print('Ahora la conversion a JSON con indentacion y con las claves ordenadas')
print(clienteoi_JSON)
