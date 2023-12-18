# Hardware platform: Pico W & Pico_
# Author : JC Santamaria 
# Date : 2023 - 9 -12
# Goal : PoC de alarma PIR con sonido y luz si intruso + boton de reset
# Learning Target : sensor PIR con interrupcion
# Ref : https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_pir.html
# Ref2: https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/3.ifttt_mail.html

# Informative block - start
p_ucontroler = "Pico W only"
p_keyOhw = " PIR 3.3 volt on GPIO17 + buzzer GPIO16"
# tiempo de bloqueo 2 segundos , tiempo de retardo 2 segundos
p_project = "PoC PIR alarm buzzer/led + rest button - using interruptions"
p_version = "1.3"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

import machine
import utime

# 0- Creamos 3 objetos PIN : PIR, botón, Buzzer ( +led)
pir_sensor = machine.Pin(17, machine.Pin.IN)
alarm = machine.Pin(18, machine.Pin.OUT)
boton_reset=machine.Pin(16,machine.Pin.IN)

# 0.1 Inicializacion de variables
warn_flag=False
alarm.high() # Un pitido al inicio
utime.sleep_ms(50)
alarm.low()

# F.1 Int-handler -Función si salta PIR => flag alarma YES 

def movimiento_detectado(pin):
    global warn_flag
    warn_flag=True
    print('¡Intruso!!')
    pir_sensor.irq(handler=None) # reset interrup PIR Alarma

# F.2 Int-handler Función reset Alarma => flag alarma NO
def reset_alarma(pin):
    global warn_flag
    warn_flag=False
    print('Reset alarma PIR')
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=movimiento_detectado) # e-arma interrup PIR-Alarma

# 1 - Set interrupción PIR & Set interrupción Boton reset 
boton_reset.irq(trigger=machine.Pin.IRQ_RISING, handler=reset_alarma) 
pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=movimiento_detectado)

# 2- Bucle infinito
while True:
    if warn_flag==True: # 2.1 Si flag Alarma YES => PIN  buzzer = 1 => Sonar buzzer Lucir LED
        alarm.toggle()
        utime.sleep_ms(50)
        alarm.toggle()
    else:
        alarm.off() # 2.1 Si flag Alarma NO => PIN  buzzer = 0
