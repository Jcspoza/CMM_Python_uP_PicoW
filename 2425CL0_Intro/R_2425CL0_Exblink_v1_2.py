# Hardware platform: Pico _ & W
# Author : JC Santamaria 
# Date : 2023 - 2 - 17
# Goal : Blink external 2xLED: in GPIO16 -> R220ohm -> LED1 catodo y LED2 anodo
# Ref : https://www.coderdojotc.org/micropython/basics/03-blink/

from machine import Pin # Get the Pin function from the machine module.
from utime import sleep # Get the sleep library from the time module.

# Informative block - start
p_ucontroler = "Pico _&W"
p_keyOhw = "Led + resistor on GPIO15"
p_project = "External LED toggle 2sec"
p_version = "1.2"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# -> 1.2 uso de toggle
# Informative block - end

EXTERNAL_LED_PIN = 16
ext_led = Pin(EXTERNAL_LED_PIN, Pin.OUT)

while (True):
    ext_led.toggle()
    print("External LED - gpio16 = ",ext_led.value())
    sleep(2)