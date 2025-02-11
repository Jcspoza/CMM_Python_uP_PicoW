# Taller Programación y Robótica en Colegio Santo Domingo – 2024 -2025 - Clase 11
# Nombre programa : P_ejercita Sumas.py
# Resumen: Juego de enseñar a sumar con puntos
# Version : 1.0 ejecicios fijos
# Topicos nuevos: Listas, estructura de juegoS
# Creditos : creacion propia de JCSP 
# Fecha JCSP 2025 01 16
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

# 1- Inicio
# 1.1 inicializacion de variables
EjerciciosSumas = [['3 + 5 =', 8], # lista de listas, lista puede guardar tipos datos distintos
                   ['3 + 9 =', 12], # primero la cadena con la exresion y 2do el resultado correcto
                   ['6 + 7 =', 13],
                   ['2 + 5 =', 7],
                   ['3 + 2 =', 5],
                   ['4 + 1 =', 5],
                   ['0 + 5 =', 5],
                   ['9 + 8 =', 17]
                   ]
Puntos = 0

# 1.2 Instrucciones
print(f'Te voy a mostrar {len(EjerciciosSumas)} ejercicios de SUMAS para que los resuelvas')


# 2- BUCLE DE EJERCICIOS
for ejercicio in EjerciciosSumas:
    respuesta = int(input('Cual es la suma de '+ ejercicio[0]))
    if respuesta == ejercicio[1]:
        Puntos += 1
        print(f'Respuesta CORRECTA, tu puntoacion actual es {Puntos}')
    else:
        print(f'Respuesta INCORRECTA, {ejercicio[0]} {ejercicio[1]}')

# 3- MOSTRAR RESULTADO
print('='*20)      
print(f'Terminaste el ejercicio con {Puntos} puntos de un maximo de {len(EjerciciosSumas)}')
      
    