# Taller Programación y Robótica en CMM BML – 2023 - Clase 20
# Resumen: Usar los API´s que normlmente vienen como JSON - ejemplo tipos simple Python a JSON
# Topicos nuevos: libreria json
# Ref Tuytorial JSON sencillo : https://www.freecodecamp.org/espanol/news/python-leer-archivo-json-como-cargar-json-desde-un-archivo-y-procesar-dumps/
# Fecha inicio 2024 03 11
# Licencia : CC BY-NC-SA 4.0
# Version 1.0


# IMPORTAR modulo que maneja JSON
import json

# 1- Tipo : Dicionario y Conversion a JSON
print('==== Diccionarios ====')
clienteDict = {
    "nombre": "Jose",
    "edad": 60,
    "notas": None
    }
print(clienteDict)
print('== conversion a JSON ==')
clienteDict_JSON = json.dumps(clienteDict, indent=4)
print(clienteDict_JSON)
print('== vuelta a Python ==')
clienteDict_vuelta = json.loads(clienteDict_JSON)
print(type(clienteDict_vuelta))
print(clienteDict_vuelta)

# 2- Tipo : Lista  y Conversion a JSON
print()
print('==== Lista ====')
clienteList = ['Jose', 60, True, False, None]
print(clienteList)
print('== conversion a JSON ==')
clienteList_JSON = json.dumps(clienteList, indent=4)
print(clienteList_JSON)
print('== vuelta a Python ==')
clienteList_vuelta = json.loads(clienteList_JSON)
print(type(clienteList_vuelta))
print(clienteList_vuelta)

# 3- Tipo : Tuplas  y Conversion a JSON
print('==== Tuplas ====')
clienteTupla = ('Jose', 60, None)
print(clienteTupla)
print('== conversion a JSON ==')
clienteTupla_JSON = json.dumps(clienteTupla, indent=4)
print(clienteTupla_JSON)
print('== vuelta a Python ==')
clienteTupla_vuelta = json.loads(clienteTupla_JSON)
print(type(clienteTupla_vuelta))
print(clienteTupla_vuelta)

# 4- Tipo : String  y Conversion a JSON
print('==== String ====')
clienteStr = 'Jose'
print(clienteStr)
print('== conversion a JSON ==')
clienteStr_JSON = json.dumps(clienteStr)
print(clienteStr_JSON)

# 5- Tipo : Int  y Conversion a JSON
print('==== Int ====')
clienteInt = 60
print(clienteInt)
print('== conversion a JSON ==')
clienteInt_JSON = json.dumps(clienteInt)
print(clienteInt_JSON)

# 6- Tipo : Real  y Conversion a JSON
print('==== Real ====')
tempReal = 22.3
print(tempReal)
print('== conversion a JSON ==')
tempReal_JSON = json.dumps(tempReal)
print(tempReal_JSON, type(tempReal_JSON))

# 7- Tipo : boolean  y Conversion a JSON
print('==== Boolean ====')
t = True
print(t)
f = False
print(f)
print('== conversion a JSON ==')
t_JSON = json.dumps(t)
print(t_JSON, type(t_JSON))
f_JSON = json.dumps(f)
print(f_JSON, type(f_JSON))