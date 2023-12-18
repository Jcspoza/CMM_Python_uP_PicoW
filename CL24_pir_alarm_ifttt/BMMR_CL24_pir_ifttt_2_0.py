# Hardware platform: Pico W & Pico_
# Author : JC Santamaria 
# Date : 2023 - 9 -16
# Goal : CL24 Enviar un email de alarma si hay un intruso
# Learning Target : Ver la integracion con IFTTT webhooks
# Ref : https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_pir.html
# Ref2: https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/3.ifttt_mail.html
# sunfounder version -> 1.1 : re-armado de la alarma y no un simple reset + visualuzacion de texto de respuesta
# 1.1 -> 2.1 incluir valor de identificacion de PIR en value1

# Informative block - start
p_ucontroler = "Pico W only"
p_keyOhw = " PIR 3.3 volt on GPIO17 + buzzer GPIO16 + reset button GPIO18"
# tiempo de bloqueo 2 segundos , tiempo de retardo 2 segundos
p_project = "PIR+buzzer -> by IFTTT send a mail+ 1 value"
p_version = "2.1"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

import machine
import utime
import urequests
from secrets import *
from do_connect import *

# Conecto al wifi
do_connect()

# Declaro los pines que tiene funciones & inicializo valiable global manejada por irq
pir_sensor = machine.Pin(17, machine.Pin.IN)
alarm = machine.Pin(18, machine.Pin.OUT)
boton_reset=machine.Pin(16,machine.Pin.IN)

# inicializo valiable global manejada por irq + el mensaje de la API IFTTT
event='CMM_PIR_alarma'
message=f"https://maker.ifttt.com/trigger/{event}/with/key/{secrets['webhooks_key']}"
warn_flag=False

# Un pitido al inicio, para indicar inici
alarm.high()
utime.sleep_ms(50)
alarm.low()

# START FUNCTION DEFINITION 
def movimiento_detectado(pin):
    # respuesta = urequests.post(message)
    val1 = 'PIR15'
    messagev = message + '?value1=' + val1
    respuesta = urequests.get(messagev) # da igual GET o POST
    print(respuesta.reason, respuesta.text)
    global warn_flag
    warn_flag=True
    pir_sensor.irq(handler=None) # DESACTIVA LA INTERRUPCION UNA VEZ SATADA LA ALARMA
    
def reset_alarma(pin):
    global warn_flag
    warn_flag=False
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=movimiento_detectado) # ARMA LA ALARMA DE NUEVO
    print("Alarma re-armada")

# END FUNCTION DEFINITION

# DEFINO LAS INTERRUPCIONES DE pir Y BOTON DE RESET
boton_reset.irq(trigger=machine.Pin.IRQ_RISING, handler=reset_alarma) 
pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=movimiento_detectado)

while True:
    if warn_flag==True:
        alarm.toggle()
        utime.sleep_ms(50)
        alarm.toggle()
    else:
        alarm.off()
        