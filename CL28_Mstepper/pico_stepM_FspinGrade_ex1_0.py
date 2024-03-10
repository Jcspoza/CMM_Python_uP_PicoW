# Hardware platform: Pico _ & W
# Author : JC Santamaria 
# Start mP Date : 2024 - 3 - 3
# Goal : Stepper Motor manged by a function with all parameters- Example"
# To do : 
# Ref : https://microcontrollerslab.com/28byj-48-stepper-motor-esp32-micropython/
# -> 1.0 input 4 parameter mode, direction delay & grades
# Instrucciones - to be added


# I- Import the required libraries
from machine import Pin
import utime

# Informative block - start
p_ucontroler = "Pico _ & W"
p_project = "Stepper Motor manged by a function with all parameters- Example"
p_keyOhw = "28BYJ-48 pines + ULN2003 iN1-GPIO10 ... IN4-GPIO13  "
p_keyLib = "None"
p_version = "3.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0- Define 3 types of sequence CW
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

minDelay = {'FULL1S': 500, 'FULL2S': 450, 'HALF': 200}

# F- Funtions
def SpinGrad(pinlist, grad, modStep, vel=100, CCW = False, Debug = False):
    """ Function to move Stepper Motor
    Parameters
        @ pinlist : lis ot pins must be x 4
        @ grad : grades in 0- 360 system
        @ modStep : mode FULL1S, FULL2S, HALF (str)
        @ vel : spin speed 100 means maximun or minimum delay beetewn steps
        @ CCW : direction of spin if True counter clock wise, 
        @ Debug : shows debug info
    
    Return : None - movement of stepper motor
    """
    nSeqs = round((grad * 512 ) / 360) # number of complete sequences
    seqStepp = SeqMode[modStep].copy() # to make modifications without affecting global var
    print(f"Stepper Sequence Mode : {modStep}")
    delayCalus = round((100 / (vel % 101)) * minDelay[modStep])
    
    if CCW:
        seqStepp.reverse()
        print(f"Spin in Counter Clock Wise direction")
        print(seqStepp)
    else:
        print(f"Spin in Clok Wise direction")
        print(seqStepp)
        
        
    if Debug:
        print('Number of compete sequences', nSeqs)
        print(f"Stepper Sequence Mode : {modStep}")
        print('Delay ', delayCalus)
        if CCW:
            print(f"Spin in Counter Clock Wise direction")
        else:
            print(f"Spin in Clok Wise direction")       
  
    for _ in range(nSeqs): 
        for step in seqStepp:
            for i in range(len(pinlist)):
                pins[i].value(step[i])
                utime.sleep_us(delayCalus) # es un parametro critico, calibrar limite


# 0- Create object pins to comprise the 4 piness needed to control steeper motor
pins = [
    Pin(10,Pin.OUT), # IN1 AZUL GPIO5 (D1)
    Pin(11,Pin.OUT), # IN2 ROSA GPIO4 (D2)
    Pin(12,Pin.OUT), # IN3 GRIS- GPIO14 (D5)
    Pin(13,Pin.OUT), # IN4 BLANCO GPIO12 (D6)
    ]
for i in range(len(pins)):
    pins[i].off()


# 2- Input Mode and Delay- Clycle
while True:
    print('============= New query =============')
    # 2.1 Input mode 
    # Extract model list by list comprehension
    modesList = [keymode for keymode in SeqMode]
    # Show modes menu & input mode ( & it assures index is in range)
    for i in range(len(modesList)):
        print(f'Selecciona {i} para el modo {modesList[i]}')

    m = (int(input('Modo = '))) % len(modesList)
    mode = modesList[m]

    # 2.2 Input delay beetwen secuences
    speedpc = int(input("Speed 0 - 100 = "))
    print(f"Spped ( 100 means maximun)  : {speedpc}")

    # 2.3 Input CC or CCW
    Wmode = input("Clock Wise CW or Counter Clok wise 'CCW' = ").upper() == 'CCW'
    
    # 2.4 Number of grades in 360º mode
    grades = int(input("Number of grades in 360º system (grades can be > 360) = "))

    SpinGrad(pins, grades, mode, speedpc, Wmode, Debug = False)