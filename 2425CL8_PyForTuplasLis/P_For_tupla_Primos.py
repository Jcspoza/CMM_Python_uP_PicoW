# Taller Programación y Robótica en Colegio Santo Domingo – 2024 -2025 - Clase 5
# Resumen: uso de for para mostrar tuplas numero primos guardados en una tupla
# Aprendizajes : formatos F-string basico + uso de for 
# Autor y y Fecha JCSP 2024 10 08
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

primosTupla = (2, 3, 5, 7, 11,
               13, 17, 19, 23, 29,
               31, 37, 41, 43, 47,
               53, 59, 61, 67, 71,
               73, 79, 83, 89, 97,
               101, 103, 107, 109, 113,
               127, 131, 137, 139, 149)

for unprimo in primosTupla:
    print(F'Es primo el numero {unprimo:>3d}')
    
print('Fin lista de primos hasta 150')
