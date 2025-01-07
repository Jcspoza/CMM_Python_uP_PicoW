# Taller Programación y Robótica CMM BML – 2024 -2025 - Clase 2
# Nombre de programa : P2425CL2_parimparWTrueMAL.py
# Resumen: Halla si un numero es par o impar 1 vez (sin fumciones y sin formatos en print)  
# Creditos : creacion de JCSP 
# Fecha JCSP 2024 09 25
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

print('¡Hola clase! Dime un numero entero y te dire si es Par o Impar')

while True:
    numero = int(input('Dime el número : ')) # input da como salida literales, hay que convertir a numero

    if (numero % 2) == 0: # el operador % da el resto de la division entera
        print(f'El numero {numero} es Par')
        
    if (numero % 2) == 1:
        print(f'El numero {numero} es Impar')
    


