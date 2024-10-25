import machine
from machine import Pin, Timer

intled = machine.Pin(16, machine.Pin.OUT)
tim = Timer()
def tick(timer):
    intled.toggle()
    print('External LED ',intled.value())
    
tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)