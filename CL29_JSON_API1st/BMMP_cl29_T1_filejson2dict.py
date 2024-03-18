# Taller Programación y Robótica en CMM BML – 2023 - Clase 20
# Resumen: Usar los API´s que normlmente vienen como JSON - ejemplo 3
# Topicos nuevos: libreria json
# Ref Tuytorial JSON sencillo : https://www.freecodecamp.org/espanol/news/python-leer-archivo-json-como-cargar-json-desde-un-archivo-y-procesar-dumps/
# Fecha inicio 2024 03 11
# Licencia : CC BY-NC-SA 4.0
# Version 1.0

# IMPORTAR modulo que maneja JSON
import json

# 0- Abrimos el fichero sin tocaer nada 
with open("ordenes.json") as f:
    datosOrg = f.read()
print('==== Fichero original ====')
print(datosOrg)
print()

# 1 - Abrimos el fichero JSON y lo volcamos a variable 'datosDict' como diccionario
with open("ordenes.json") as f:
    datosDict = json.load(f)
    
 
print('==== Conversion a Diccionario ====')
print(datosDict)
print()

print('==== Recorrido del Diccionario ====')
for clave in datosDict:
    print(clave, datosDict[clave])
    print()
    
print('==== Recorrido del Diccionario clave a clave ====')
for clave in datosDict:
    print(f'Valor de la clave: {clave} - Tipo del contenido: {type(datosDict[clave])}')
    print(f'Contenido: {datosDict[clave]}')
    
print('==== Recorrido de las ordenes ====')
print(f"Numero de ordenes = {len(datosDict['ordenes'])}")

for orden in datosDict['ordenes']:
    print(orden)
    print()
    
    
