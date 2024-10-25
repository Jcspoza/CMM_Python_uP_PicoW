# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase 3
# Clase : Primeros pasos con Pico y Pico W
# Programa: External LED toggle 2sec
# Objetivo : Blink external 2xLED: in GPIO16 -> R220ohm -> LED1 catodo y LED2 anodo
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Ref : https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico
# Ref : https://www.coderdojotc.org/micropython/basics/03-blink/
# Fecha JCSP 2023 - 2 - 17
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

from machine import Pin # Get the Pin function from the machine module.
from utime import sleep # Get the sleep library from the time module.

# Informative block - start
p_ucontroler = "Pico _&W"
p_keyOhw = "Led + resistor on GPIO16"
p_project = "External LED toggle 2sec"
p_version = "1.2"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# -> 1.2 uso de toggle
# Informative block - end

print("Hello, Raspberry Pi Pico!")
sleep(1)

EXTERNAL_LED2_PIN = 16
ext_led = Pin(EXTERNAL_LED2_PIN, Pin.OUT)

while (True):
    ext_led.toggle()
    print("External LEDs - gpio16 = ",ext_led.value())
    sleep(1)