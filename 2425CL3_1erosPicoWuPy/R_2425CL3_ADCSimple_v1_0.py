# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase 3
# Clase : Primeros pasos con Pico y Pico W
# Programa: 
# Objetivo : 
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Ref : https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

from machine import Pin, ADC
from utime import sleep
from os import uname

# Informative block - start
p_keyOhw = "Potenciometro en ADC0 - GPIO26"
p_project = "Lectura Analogica de potenciometro"
p_version = "1.0"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")

adc = ADC(Pin(26))

while True:
    print(adc.read_u16())
    sleep(1)
    
