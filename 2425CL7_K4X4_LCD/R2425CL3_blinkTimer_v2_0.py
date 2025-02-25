# Hardware platform: Pico _ & W
# Author : JC Santamaria 
# Date : 2023 - 2 - 17
# Goal : Blink with timer internal led
# Ref : 

# Informative block - start
p_ucontroler = "Pico _&W"
p_keyOhw = "Nothing"
p_project = "Internal LED toggle 2sec with TIMER + hago cosas"
p_version = "2.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")

import machine
from machine import Pin, Timer
from utime import sleep

intled = machine.Pin("LED", machine.Pin.OUT)
tim = Timer()
def tick(timer):
    intled.toggle()
    print('Internal LED ',intled.value())
    
tim.init(freq=0.5, mode=Timer.PERIODIC, callback=tick)

cuenta = 0
while True:
    try:
        print('Hago cosas #',cuenta)
        cuenta += 1
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break

# Deshago el timer
tim.deinit()
intled.off()
print("Finished.")