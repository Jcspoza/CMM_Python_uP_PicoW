# Taller Programación y Robótica CMM BML – 2024 -2025 - Clase 2
# Nombre de programa : P2425CL2b_divideTry.py
# Resumen: Divide mal sin prever division por cero 
# Creditos : creacion de JCSP 
# Fecha JCSP 2025 01 07
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

print('¡Hola clase! Dime 2 números y los dividiré')

a = float(input('Dime el dividendo (decimal): ')) # input da como salida literales, hay que convertir a numero
b = int(input('Dime el divisor (entero): ')) # int convierte a entero / float a numero en coma flotante o decimal

try:
    print('La multiplicación es = ', a / b)
except ZeroDivisionError:
    print('No se puede dividir por cero')
    

