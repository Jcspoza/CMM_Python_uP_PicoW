# Taller Programación y Robótica en CMM BML – 2023 - Clase 20
# Resumen: Usar los API´s que normlmente vienen como JSON - ejemplo 4
# Topicos nuevos: libreria json
# Ref Tuytorial JSON sencillo : https://www.freecodecamp.org/espanol/news/python-leer-archivo-json-como-cargar-json-desde-un-archivo-y-procesar-dumps/
# Fecha inicio 2024 03 11
# Licencia : CC BY-NC-SA 4.0
# Version 1.0

# IMPORTAR modulo que maneja JSON
import json

# 1 - Abrimos el fichero JSON y lo volcamos a variable 'datosDict' como diccionario
with open("ordenes.json") as f:
    datosDict = json.load(f)
    
print('==== Mostrar la Conversion a Diccionario del fiechro JSON ====')
print(datosDict)
print()

# 2- Modificar el diccionario, quitando el informacion de cliente
print('==== Manipular Diccionario ====')
print(f'Tipo del contenido clave "ordenes": {type(datosDict["ordenes"])}')
print('Vamos a quitar la informacion de cliente de todas las ordenes')
for orden in datosDict["ordenes"]:
    del orden["cliente"]

print('== Mostrar el diccionario modificado ==')
print(f"Numero de ordenes = {len(datosDict['ordenes'])}")
for orden in datosDict['ordenes']:
    print(orden)
    print()

# 3- Abir (o crear) un archivo ordenes_nuevo.json y guardar la nueva versión de la información
print('==== Volcar dicionario Modificado a nuevo fichero JSON con indentacion ====')
with open("ordenes_nuevo.json", 'w') as archivo_nuevo:
    json.dump(datosDict, archivo_nuevo, indent = 4)
    
# 4 - Abrimos el fichero nuevo sin tocaer nada 
with open("ordenes_nuevo.json") as f:
    datosNuevo = f.read()
print('==== Fichero Nuevo  leido como str ====')
print(datosNuevo)