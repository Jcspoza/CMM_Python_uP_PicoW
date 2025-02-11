# Taller Programación y Robótica en Colegio Santo Domingo – 2024 -2025 - Clase 11
# Nombre programa : P_ejercitaSumasv2.py
# Resumen: Juego de enseñar a sumar con puntos
# Version : 2.0 + generacion de ejercicios aleatoria
# Topicos nuevos: Listas, estructura de juego, 
# Creditos : creacion propia  de JCSP 
# Fecha JCSP 2025 01 16
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

# 0- IMPORTACION Y FUNCIONES
import random

def GeneraEjerSum(maxint):
    """ Genera ejecicios de tipo suma con sumandos de 0 a maxint"""
    
    sum1 = random.randint(0, maxint)
    sum2 = random.randint(0, maxint)
    cadenaEjer = str(sum1) + ' + ' + str(sum2) + ' ='
    solucion = sum1 + sum2
    return [cadenaEjer, solucion]

# 1- INICIO
# 1.1 inicializacion de constantes y variables
NUMEJER = 10
MAXIMONUMaSUMAR = 15
EjerciciosSumas =[]
Puntos = 0

# 1.2 Generacion Aleatoria de ejercicios
for _ in range(0,NUMEJER):
    EjerciciosSumas.append(GeneraEjerSum(MAXIMONUMaSUMAR))

# 1.3 Instrucciones
print(f'Te voy a mostrar {len(EjerciciosSumas)} ejercicios de SUMAS para que los resuelvas')
print(f'El maximo numero a SUMAR es {MAXIMONUMaSUMAR}')

# 2- Bucle ejercicios
for ejercicio in EjerciciosSumas:
    respuesta = int(input('Cual es la suma de '+ ejercicio[0]))
    if respuesta == ejercicio[1]:
        Puntos += 1
        print(f'Respuesta CORRECTA, tu puntoacion actual es {Puntos}')
    else:
        print(f'Respuesta INCORRECTA, {ejercicio[0]} {ejercicio[1]}')

# 3- Mostrar Resultado
print('='*20)      
print(f'Terminaste el ejercicio con {Puntos} puntos de un maximo de {len(EjerciciosSumas)}')
