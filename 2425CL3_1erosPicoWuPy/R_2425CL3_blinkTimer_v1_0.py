# Hardware platform: Pico _ & W
# Author : JC Santamaria 
# Date : 2023 - 2 - 17
# Goal : Blink with timer external LED: in GPIO16 -> R220ohm -> LED1 catodo y LED2 anodo
# Ref : 

# Informative block - start
p_ucontroler = "Pico _&W"
p_keyOhw = "Led + resistor on GPIO16"
p_project = "External LED toggle 2sec with TIMER"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")

import machine
from machine import Pin, Timer

intled = machine.Pin(16, machine.Pin.OUT)
tim = Timer()
def tick(timer):
    intled.toggle()
    print('External LED ',intled.value())
    
tim.init(freq=0.5, mode=Timer.PERIODIC, callback=tick)