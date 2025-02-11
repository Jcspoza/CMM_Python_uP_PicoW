# Taller Programación y Robótica en Colegio Santo Domingo – 2024 -2025 - Clase 11
# Nombre programa : P_ejercitaRestasAleav1.py
# Resumen: Juego de enseñar a restar con puntos + generacion aleatoria de restas
# Version : 1.0 con generacion aleatoria de restas
# Topicos nuevos: Listas, estructura de juego, 
# Creditos : creacion propia  de JCSP 
# Fecha JCSP 2025 01 16
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

# 0- funciones
import random

def GeneraEjerResta(maxint):
    """ Genera ejecicios de tipo resta con sumandos de 0 a maxint, resultado NO negativo"""
    
    RnumMay = random.randint(0, maxint)
    RnumMenor = random.randint(0, RnumMay)
    
    cadenaEjer = str(RnumMay) + ' - ' + str(RnumMenor) + ' ='
    solucion = RnumMay - RnumMenor
    return [cadenaEjer, solucion]

# 1- INICIO
# 1.1 inicializacion de constantes y variables
NUMEJER = 10
MAXIMONUMaRESTAR = 15
EjerciciosResta =[]
Puntos = 0

# 1.2 Generacion Aleatoria de ejercicios
for _ in range(0,NUMEJER):
    EjerciciosResta.append(GeneraEjerResta((MAXIMONUMaRESTAR)))

# 1.3 Instrucciones
print(f'Te voy a mostrar {len(EjerciciosResta)} ejercicios de RESTAS para que los resuelvas')
print(f'El maximo numero en las RESTAS es {MAXIMONUMaRESTAR}')

# 2- BUCLE DE EJERCICIOS
for ejercicio in EjerciciosResta:
    respuesta = int(input('Cual es la resta de '+ ejercicio[0]))
    if respuesta == ejercicio[1]:
        Puntos += 1
        print(f'Respuesta CORRECTA, tu puntoacion actual es {Puntos}')
    else:
        print(f'Respuesta INCORRECTA, {ejercicio[0]} {ejercicio[1]}')

# 3- MOSTRAR RESULTADOS
print('='*20)      
print(f'Terminaste el ejercicio con {Puntos} puntos de un maximo de {len(EjerciciosResta)}')

