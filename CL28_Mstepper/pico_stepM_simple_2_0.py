# Hardware platform: Pico _ & W
# Author : JC Santamaria 
# Start mP Date : 2024 - 3 - 3
# Goal : Stepper simple - check spin
# To do : 
# Ref : https://microcontrollerslab.com/28byj-48-stepper-motor-esp32-micropython/
# 1.0 
# Instrucciones - to be added


# I- Import the required libraries
from machine import Pin
import utime

# Informative block - start
p_ucontroler = "Pico _ & W"
p_project = "Stepper simple - check ALL modes and delays by manual input"
p_keyOhw = "28BYJ-48 pines + ULN2003 iN1-GPIO10 ... IN4-GPIO13  "
p_keyLib = "None"
p_version = "2.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0- Create object pins to comprise the 4 piness needed to control steeper motor
pins = [
    Pin(10,Pin.OUT), # IN1 AZUL GPIO5 (D1)
    Pin(11,Pin.OUT), # IN2 ROSA GPIO4 (D2)
    Pin(12,Pin.OUT), # IN3 GRIS- GPIO14 (D5)
    Pin(13,Pin.OUT), # IN4 BLANCO GPIO12 (D6)
    ]
for i in range(len(pins)):
    pins[i].off()

DELAYSEQ = 500 #  defines de delay in sequence in microsecons, 500 usecons could be the minimun

# 1- Define 3 types of sequence CW + 3 CCW
SeqMode = {'FULL1S': [[1,0,0,0], # Clock Wise - 1 bobina excitada cada paso
                      [0,1,0,0],
                      [0,0,1,0],
                      [0,0,0,1]],
           'FULL1Sr': [[0,0,0,1], # Counter clock wise
                       [0,0,1,0],
                       [0,1,0,0],
                       [1,0,0,0]],
            'FULL2S': [[1,1,0,0], # CW - 2 bobinas excitadas cada paso => + Par y + consumo
                       [0,1,1,0],
                       [0,0,1,1],
                       [1,0,0,1]],
            'FULL2Sr': [[1,0,0,1], # CCW
                        [0,0,1,1],
                        [0,1,1,0],
                        [1,1,0,0]],
            'HALF' : [[1,0,0,0], # CW 
                      [1,1,0,0],
                      [0,1,0,0],
                      [0,1,1,0],
                      [0,0,1,0],
                      [0,0,1,1],
                      [0,0,0,1],
                      [1,0,0,1]],
            'HALFr' : [[1,0,0,1], # CCW
                       [0,0,0,1],
                       [0,0,1,1],
                       [0,0,1,0],
                       [0,1,1,0],
                       [0,1,0,0],
                       [1,1,0,0],
                       [1,0,0,0]] 
            }        
           
modesList = [keymode for keymode in SeqMode]

for i in range(len(modesList)):
    print(f'Selecciona {i} para el modo {modesList[i]}')

m = (int(input('Modo = '))) % len(modesList)
print(m)

modo = modesList[m]
print(f"Stepper motor mode : {modo}")
delayseq = int(input("Delay beetwen steeps in micro seconds (400/180 min in full/half modes)= "))
# print(f"Delay in each steep in sequence : {delayseq}")

while True:
    for step in SeqMode[modo]:
        for i in range(len(pins)):
            pins[i].value(step[i])
            utime.sleep_us(delayseq) # es un parametro critico, calibrar limite
            
