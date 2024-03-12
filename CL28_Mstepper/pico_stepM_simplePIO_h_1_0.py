# Hardware platform: Pico _ & W
# Author : JC Santamaria 
# Start mP Date : 2024 - 3 - 3
# Goal : Stepper simple - check motor with conservative parameters - Half s
# To do : 
# Ref1 : https://www.youtube.com/watch?v=UJ4JjeCLuaI
# Ref1 git hub : https://github.com/tinkertechtrove/pico-pi-playing/tree/main/pio-steppers
# 1.0 
# Instrucciones - to be added


from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep
import sys

# Informative block - start
p_ucontroler = "Pico _ & W"
p_project = "Stepper simple using PIO - check motor with conservative parameter HALF"
p_keyOhw = "28BYJ-48 pines + ULN2003 in1-GPIO10 ... IN4-GPIO13  "
p_keyLib = "None"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# PIO - Define function for state machine
@asm_pio(set_init=(PIO.OUT_LOW,) * 4)
def prog():
    wrap_target()
    set(pins, 8) [31] # [1,0,0,0]
    nop() [31]
    nop() [31]
    nop() [31]
    set(pins, 12) [31] # [1,1,0,0]
    nop() [31]
    nop() [31]
    nop() [31]
    set(pins, 4) [31] # [0,1,0,0]
    nop() [31]
    nop() [31]
    nop() [31]
    set(pins, 6) [31] # [0,1, 1, 0]
    nop() [31]
    nop() [31]
    nop() [31]
    set(pins, 2) [31] # [0,0,1,0]
    nop() [31]
    nop() [31]
    nop() [31]
    set(pins, 3) [31] # [0,0,1,1]
    nop() [31]
    nop() [31]
    nop() [31]
    set(pins, 1) [31] # [0,0,0,1]
    nop() [31]
    nop() [31]
    nop() [31]
    set(pins, 9) [31] # [1,0, 0, 1]
    nop() [31]
    nop() [31]
    nop() [31]
    wrap()
    
# END PIO    

sm = StateMachine(0, prog, freq=140000, set_base=Pin(10))
# Freq -> 7.14 usec machine cycle- Maximun speed
# Each stepp takes 32 * 4 = 128 cycles, so it takes usec = 0.9 mili sec

print('1- Activate state machine on pins 10, 11, 12, and 13')
sm.active(1)
print('2- Do nothing by 5 seconds')
sleep(5)
print('... and 3- stop state machine and clear pins')
sm.active(0)
sm.exec("set(pins,0)")