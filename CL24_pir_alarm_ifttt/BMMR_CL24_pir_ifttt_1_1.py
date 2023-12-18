# Hardware platform: Pico W & Pico_
# Author : JC Santamaria 
# Date : 2023 - 9 -16
# Goal : CL24 Enviar un email de alarma si hay un intruso
# Learning Target : Ver la integracion con IFTTT webhooks
# Ref : https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_pir.html
# Ref2: https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/3.ifttt_mail.html
# sunfounder version -> 1.1 : re-armado de la alarma y no un simple reset + visualuzacion de texto de respuesta

# Informative block - start
p_ucontroler = "Pico W only"
p_keyOhw = " PIR 3.3 volt on GPIO17 + buzzer GPIO16 + reset button GPIO18"
# tiempo de bloqueo 2 segundos , tiempo de retardo 2 segundos
p_project = "PIR+buzzer -> by IFTTT send an e-mail"
p_version = "1.1"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

import machine
import utime
import urequests
from secrets import *
from do_connect import *

# 0- Creamos 3 objetos PIN : PIR, botón, Buzzer ( +led)
# Declaro los pines que tiene funciones & inicializo valiable global manejada por irq
pir_sensor = machine.Pin(17, machine.Pin.IN)
alarm = machine.Pin(18, machine.Pin.OUT)
boton_reset=machine.Pin(16,machine.Pin.IN)

# 0.1 Inicializacion de variables
# inicializo valiable global manejada por irq + el mensaje de la API IFTTT
event='CMM_PIR_alarma'
message=f"https://maker.ifttt.com/trigger/{event}/with/key/{secrets['webhooks_key']}"
warn_flag=False

alarm.high() # Un pitido al inicio, para indicar inicio
utime.sleep_ms(50)
alarm.low()

# 0.2 Conecto al wifi
do_connect()

# START FUNCTION DEFINITION
# F.1 Int-handler -Función si salta PIR => flag alarma YES 
def movimiento_detectado(pin):
    # respuesta = urequests.post(message) da igual GET o POST
    respuesta = urequests.get(message) # dispara el webhook
    print(respuesta.reason, respuesta.text)
    global warn_flag
    warn_flag=True
    print('¡Intruso!!')
    pir_sensor.irq(handler=None) # DESACTIVA LA INTERRUPCION UNA VEZ SATADA LA ALARMA
    
# F.2 Int-handler Función reset Alarma => flag alarma NO
def reset_alarma(pin):
    global warn_flag
    warn_flag=False
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=movimiento_detectado) # ARMA LA ALARMA DE NUEVO
    print("Alarma re-armada")

# END FUNCTION DEFINITION

# 1 - Set interrupción PIR & Set interrupción Boton reset 
# DEFINO LAS INTERRUPCIONES DE pir Y BOTON DE RESET
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
        