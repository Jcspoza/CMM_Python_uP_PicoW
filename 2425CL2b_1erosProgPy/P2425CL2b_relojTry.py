# Taller Programación y Robótica CMM BML – 2024 -2025 - Clase 2
# Nombre de programa : P2425CL2b_relojTry.py
# Resumen: muestra un reloj que corree en segundos, separa con cmtrl-C y limpia 
# Creditos : creacion de JCSP 
# Fecha JCSP 2025 01 07
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

from time import sleep
import datetime # estan aqui todas las librerias relacionadas con fecha y hora

# 0- poner en hora
ahora = datetime.datetime.now()
h = ahora.hour
m = ahora.minute
s = ahora.second

# 1- Bucle infinito cada segundo
try: # MANEJO DE EVENTOS Y EXCEPCIONES en Python
    while True:
        s = s + 1
        if s == 60:
            s = s % 60
            m = m + 1
            if m == 60:
                m = m % 60
                h = h + 1
                if h == 24:
                    h = h % 24            
        print(f"Hora = {h:02d}:{m:02d}:{s:02d}", end='\r')
        # el parametro end= '\r' (retorno de carro) hace que el cursor vuelva al inicio SIN saltar
        sleep(1)
        
except KeyboardInterrupt: # Salgo del bucle con un Control+C
    print('Salgo por peticion del usuario')

finally:
    print()
    print(f"{' Parada del reloj ':*^40s}")
