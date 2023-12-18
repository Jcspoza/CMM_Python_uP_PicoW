# Hardware platform: Pico W & Pico_
# Author : JC Santamaria 
# Date : 2023 - 9 - 8
# Goal : CL20 Enviar un email de alarma si hay un intruso
# Learning Target : Ver como funciona un sensor PIR basico
# Ref : https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_pir.html
# Ref2: https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/3.ifttt_mail.html

# Informative block - start
p_ucontroler = "Pico W only"
p_keyOhw = " PIR 3.3 volt on GPIO17"
# tiempo de bloqueo 2 segundos , tiempo de retardo 2 segundos
p_project = "PIR alarm basic HW test - interruptions & counter"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

import machine
import utime

pir_sensor = machine.Pin(17, machine.Pin.IN)
contador = 0

def motion_detected(pin):
    global contador
    contador += 1
    print(f"Hay alguien fuera! Contador de intrusos {contador}")
    
pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)