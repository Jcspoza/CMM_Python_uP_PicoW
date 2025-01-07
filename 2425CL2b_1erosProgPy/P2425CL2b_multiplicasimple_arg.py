# Taller Programación y Robótica CMM BML – 2024 -2025 - Clase 2
# Nombre de programa : P2425CL2b_multiplicasimple.py
# Resumen: Multiplica simple - paso argumentos (sin fumciones y sin formatos en print) 
# Creditos : creacion de JCSP 
# Fecha JCSP 2024 09 25
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

from sys import argv
print('Multiplica 2 numeros dados comoa argumentos del scrip')

a = float(argv[1]) # input da como salida literales, hay que convertir a numero
b = int(argv[2]) # int convierte a entero / float a numero en coma flotante o decimal

print('La multiplicación es = ', a * b)
