# Hardware platform: Pico _ & W
# Author : JC Santamaria 
# Start mP Date : 2024 - 3 - 3
# Goal : Stepper simple - check motor with conservative parameters
# To do : 
# Ref : https://microcontrollerslab.com/28byj-48-stepper-motor-esp32-micropython/
# 1.0 
# Instrucciones - to be added


# I- Import the required libraries
from machine import Pin
import utime

# Informative block - start
p_ucontroler = "Pico _ & W"
p_project = "Stepper simple - check motor with conservative parameter"
p_keyOhw = "28BYJ-48 pines + ULN2003 in1-GPIO10 ... IN4-GPIO13  "
p_keyLib = "None"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0- Create objet pins to comprise the 4 piness neede to control steeper motor
pins = [
    Pin(10,Pin.OUT), # IN1 AZUL GPIO5 (D1)
    Pin(11,Pin.OUT), # IN2 ROSA GPIO4 (D2)
    Pin(12,Pin.OUT), # IN3 GRIS- GPIO14 (D5)
    Pin(13,Pin.OUT), # IN4 BLANCO GPIO12 (D6)
    ]
for i in range(len(pins)):
    pins[i].off()

DELAYuSEC = 2000 #defines de delay in sequence, 500 usecons could be the minimun, play with a conservative number

# 1- Define activation sequence in mode Half step
half_step_sequence = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1],
    ]

modo = 'half_step_sequence'
print(f"Modo steper: {modo}")
print(f"Delay in each steep in sequence : {DELAYuSEC}")

while True:
    for step in half_step_sequence:
        for i in range(len(pins)):
            pins[i].value(step[i])
            utime.sleep_us(DELAYuSEC) # crtitical parameter
            
