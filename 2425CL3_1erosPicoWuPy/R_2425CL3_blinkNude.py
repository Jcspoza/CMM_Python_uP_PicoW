from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT) # Funciona igual en Pico o en Pico W

print("LED starts flashing...")
while True:
    pin.toggle() # alterna el estado si 1 -> 0 y si 0 -> 1
    sleep(1) # sleep 1sec
