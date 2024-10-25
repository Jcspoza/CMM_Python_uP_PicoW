# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase 3
# Clase : Primeros pasos con Pico y Pico W
# Programa: Blink: Internal LED toggle 1sec-Simple
# Objetivo : Blink Led interno de la forma mas simple
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Ref : https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

from machine import Pin, unique_id
from utime import sleep
from os import uname

# Informative block - start
p_keyOhw = "Nothing"
p_project = "Blink: Internal LED toggle 1sec-Simple"
p_version = "1.0"
ui = machine.unique_id()
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW : {p_keyOhw}")
uis = f'{ui[0]:02x}{ui[1]:02x}{ui[2]:02x}{ui[3]:02x}{ui[4]:02x}{ui[5]:02x}{ui[6]:02x}{ui[7]:02x}'
print("Pico id: ", uis)
print(f"Program: {p_project} - Version: {p_version}")

pin = Pin("LED", Pin.OUT) # Funciona igual en Pico o en Pico W
print('Configuracion de led interno', pin)

print("LED starts flashing...")
while True:
    pin.toggle() # alterna el estado si 1 -> 0 y si 0 -> 1
    sleep(1) # sleep 1sec
