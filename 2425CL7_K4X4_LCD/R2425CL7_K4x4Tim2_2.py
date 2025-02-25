# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase 7
# Programa: Test hw basico de teclado 4 x 4, con  timer y repeticion
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Version : usar un timer
# Ref https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_keypad.html
# Librerias : NINGUNA
# Ref librerias: 
# Fecha JCSP 2025 02 05
# Licencia : CC BY-NC-SA 4.0

# Informative block - start
from os import uname
p_keyOhw = "Teclado 4x4,fpines = [6,7,8,9] cpines = [10,11,12,13]"
p_project = "Test HW basico de Teclado 4 x4 com timer"
p_version = "Timer 2.2"
p_library =  "NINGUNA"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin, Timer
from time import sleep, ticks_ms, ticks_diff

# 0 Inicializamos
# CONSTANTS
TIMEREPEAT = 700 # ms 1/2 second

caracteres = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

fpines = [6,7,8,9] # numero de GPIOS de filas
cpines = [10,11,12,13] # numero sde GPIOS de columnsa

# Mejora 1 : set pins for rows as outputs
filaPines = [Pin(fpin, mode=Pin.OUT) for fpin in fpines] 

# set pins for cols as inputs with pull-down
colPines = [Pin(cpin, mode=Pin.IN, pull=Pin.PULL_DOWN) for cpin in cpines]

# 1- Definicion funciones
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
    
def scan4x4K(timer):
    global ultimasTeclas, last_time
    
    if ticks_diff(ticks_ms(), last_time) > TIMEREPEAT:
        ultimasTeclas = None
        last_time = ticks_ms()
        
    actualTeclas = readKeys()
    if actualTeclas == ultimasTeclas:
        pass # no hace nada , solo hace hueco, para que el codigo sea igual a 2_2
    else:
        ultimasTeclas = actualTeclas
        last_time = ticks_ms() # si tecla nueva re-inicio tiempo repeticion
        if actualTeclas != None:
            # print(actualTeclas)
            teclas = "".join(actualTeclas) # Mej3 cambia lista a cadena para print
            print(teclas , '|', len(teclas))

  
# Inicializaciones 2da parte
init4x4()
ultimasTeclas = None
last_time = ticks_ms()  # Inicializo temporizador de repeticion
timPul = Timer() # creamos una instancia de timer
    
print("Empezamos 4 x 4 Keyboard con Timer")
timPul.init(freq=10, mode=Timer.PERIODIC, callback=scan4x4K)

# Bucle principal
cuenta = 0
while True:
    try:
        print('Hago cosas #',cuenta)
        cuenta += 1
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break

# Deshago el timer
timPul.deinit()
print("Terminado.")