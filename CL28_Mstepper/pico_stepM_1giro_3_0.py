# Hardware platform: Pico _ & W
# Author : JC Santamaria 
# Start mP Date : 2024 - 3 - 3
# Goal : Stepper simple - check spin
# To do : 
# Ref : https://microcontrollerslab.com/28byj-48-stepper-motor-esp32-micropython/
# -> 3.0 input 3 parameyter mode, direction and delay
# Instrucciones - to be added


# I- Import the required libraries
from machine import Pin
import utime

# Informative block - start
p_ucontroler = "Pico _ & W"
p_project = "Stepper 1 x 360 º in 3 param -> meassure lap time & number stepps per lap"
p_keyOhw = "28BYJ-48 pines + ULN2003 iN1-GPIO10 ... IN4-GPIO13  "
p_keyLib = "None"
p_version = "3.0"
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

# 1- Define 3 types of sequence CW
SeqMode = {'FULL1S': [[1,0,0,0], # Clock Wise - 1 bobina excitada cada paso
                      [0,1,0,0],
                      [0,0,1,0],
                      [0,0,0,1]],        
            'FULL2S': [[1,1,0,0], # CW - 2 bobinas excitadas cada paso => + Par y + consumo
                       [0,1,1,0],
                       [0,0,1,1],
                       [1,0,0,1]],            
            'HALF' : [[1,0,0,0], # CW 
                      [1,1,0,0],
                      [0,1,0,0],
                      [0,1,1,0],
                      [0,0,1,0],
                      [0,0,1,1],
                      [0,0,0,1],
                      [1,0,0,1]]
            }        

# 2- Input Mode and Delay
# 2.1 Input mode 
# Extract model list by list comprehension
modesList = [keymode for keymode in SeqMode]
# Show modes menu & input mode ( & it assures index is in range)
for i in range(len(modesList)):
    print(f'Selecciona {i} para el modo {modesList[i]}')

m = (int(input('Modo = '))) % len(modesList)
mode = modesList[m]
print(f"Stepper Sequence Mode : {mode}")

# 2.2 Input delay beetwen secuences
delayseq = int(input("Delay beetwen steep (micro sec)= "))
print(f"Delay in each steep in sequence : {delayseq}")

# 2.3 Input CC or CCW
seqStepp = SeqMode[mode]
wmode = input("Clock Wise CW or Counter Clok wise CCW = ").upper()
if wmode == 'CCW':
    seqStepp.reverse()
    print(f"Spin in Counter Clock Wise direction")
else:
    print(f"Spin in Clock Wise direction")
    # else is CW mode

counter = 0
startT = utime.ticks_us()
for _ in range(64*8): 
    for step in seqStepp:
        counter += 1
        for i in range(len(pins)):
            pins[i].value(step[i])
            utime.sleep_us(delayseq) # es un parametro critico, calibrar limite

endT = utime.ticks_us()
lapT = utime.ticks_diff(endT, startT) / 1000000
print(f'Stepps done per lap = {counter }')
print(f'Time per lap {lapT:02.2f} sec, RPM = {60/lapT:02.2f}')
