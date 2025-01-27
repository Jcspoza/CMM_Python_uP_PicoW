# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase 7
# Programa: Test hw basico de teclado 4 x 4 
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Version : basado en tutorial de Sunfounder + mejorado
# Ref https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_keypad.html
# Librerias : NINGUNA
# Ref librerias: 
# Fecha JCSP 2024 10 03
# Licencia : CC BY-NC-SA 4.0

# Informative block - start
from os import uname
p_keyOhw = "Teclado 4x4,fpines = [6,7,8,9] cpines = [10,11,12,13]"
p_project = "Test HW basico de Teclado 4 x4"
p_version = "SF 2.2"
p_library =  "NINGUNA"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin
from time import sleep, ticks_ms, ticks_diff

# CONSTANTS
TIMEREPEAT = 700 # ms 1/2 second

# 0 Inicializamos
caracteres = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

fpines = [6,7,8,9] # numero de GPIOS de filas
cpines = [10,11,12,13] # numero sde GPIOS de columnsa

# Mejora 1 : set pins for rows as outputs
filaPines = [Pin(fpin, mode=Pin.OUT) for fpin in fpines] 

# set pins for cols as inputs with pull-down
colPines = [Pin(cpin, mode=Pin.IN, pull=Pin.PULL_DOWN) for cpin in cpines]

def init4x4():
    for f in range(0,4):
        filaPines[f].low()

def readKeys():
    """ scan the keypad - todas las teclas cada vez > devuelve varios valores"""
    key = []
    for i in range(4):
        filaPines[i].high()
        for j in range(4):
            if(colPines[j].value() == 1):
                key.append(caracteres[i][j])
        filaPines[i].low()
    if key == [] :
        return None
    else:
        return key

# Fin Definicion Funciones
print("Empezamos")
# Todas las filas a '0'
init4x4()

ultimasTeclas = None

last_time = ticks_ms()  # Inicializo temporizador de repeticion

while True:
    if ticks_diff(ticks_ms(), last_time) > TIMEREPEAT:
        ultimasTeclas = None
        last_time = ticks_ms()
        
    actualTeclas = readKeys()
    if actualTeclas == ultimasTeclas:
        sleep(0.01)
    else:
        ultimasTeclas = actualTeclas
        if actualTeclas != None: # Mej3 cambia lista a cadena para print
            # print(actualTeclas)
            teclas = "".join(actualTeclas)
            print(teclas , '|', len(teclas))
        # print()
        sleep(0.01)
    
    