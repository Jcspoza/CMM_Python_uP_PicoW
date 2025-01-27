# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase 7
# Programa: Test hw basico de teclado 4 x 4 
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Version : basado en tutorial de Sunfounder cambios de pines y pull-dow interno
# Ref https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_keypad.html
# Librerias : NINGUNA
# Ref librerias: 
# Fecha JCSP 2024 10 03
# Licencia : CC BY-NC-SA 4.0

# Informative block - start
from os import uname
p_keyOhw = "Teclado 4x4,fpines = [6,7,8,9] cpines = [10,11,12,13]"
p_project = "Test HW basico de Teclado 4 x4"
p_version = "SF 1.0"
p_library =  "NINGUNA"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin
from time import sleep

# 0 Inicializamos creando los objetos pines x 8 = 4 de salida(filas) y 4 de entrada (columnas)
caracteres = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

fpines = [6,7,8,9] # numeros de identificacion de GPIOS de filas, NO son objetos pines, solo numeros
cpines = [10,11,12,13] # numeros identificacion de GPIOS de columnsa

filaPines = [None, None, None, None] # esto crea un alista vacio de 4 elementos
colPines = [None, None, None, None] # idem
for i in range(4): # creacion de los objetos pines x 4 x 2
    filaPines[i] = Pin(fpines[i], Pin.OUT) # las filas inyectan 0 o 1
    colPines[i] = Pin(cpines[i], Pin.IN, Pin.PULL_DOWN) # en las columnas leemos 0 o 1,
    # pull-dow activado es decir por defecto leeremos '0'

def readKey():
    """ scan the keypad - todas las teclas cada vez > devuelve varios valores"""
    key = []
    for i in range(4):
        filaPines[i].high() # inyecta un '1' por cada fila y lle las columnas
        for j in range(4):
            if(colPines[j].value() == 1):
                key.append(caracteres[i][j]) # usa un alsita añadiendo, permite devolver varias teclas
        filaPines[i].low() # volvemso a poner un '0'
    if key == [] :
        return None # si vacio devuelve none
    else:
        return key

# Fin Definicion Funciones

print("Empezamos")

last_key = None
while True:
    current_key = readKey()
    if current_key == last_key: # misma/s tecla/s
        continue # salta este ciclo del while, nose ejecutan las siguientes instrucciones
    
    # ya nse que no es la misma tecla que el ciclo anterior
    last_key = current_key # inicializo para ciclo siguiente
    if current_key != None: # si es none , siginifica que he levantado el dedo
        print(current_key) # si no es none, hay tecla/s nuevas pulsada/s
    sleep(0.1) # recorro cada decima de segundo, arbitrario
    
    