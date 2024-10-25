# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase 3
# Clase : Primeros pasos con Pico y Pico W
# Programa: R_2425CL3_ExtLedPWMADC_v1_0.py
# Objetivo : 
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Ref : https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

from machine import Pin, PWM
from utime import sleep
from os import uname

# Informative block - start
p_keyOhw = "Led en GPIO16"
p_project = "Escribe Led con PWM Up -> Down"
p_version = "1.0"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")

print('Inicio de inicializacion ...', end='')
EXTERNAL_LED_PIN = 16
pwmled = PWM(EXTERNAL_LED_PIN)
pwmled.freq(1000)
print("Fin de inicializacion")
sleep(1)

while True:
    print('Arriba ^')
    for valorDuty in range(0b1111_1111_1111_1111): # 0b1111_1111_1111_1111 = 65535
        pwmled.duty_u16(valorDuty)
        # print(valorDuty)
        sleep(0.00001)
    
    print('Abajo v')
    for valorDuty in range(0b1111_1111_1111_1111, 0 , -1):
        pwmled.duty_u16(valorDuty)
        # print(valorDuty)
        sleep(0.00001)
    
