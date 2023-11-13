# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 5 - 11
# Goal : Internal temperature sensor reading & logging in a file
# Learning Target : Analog digital converter basic + file handling IMPROVED
# Ref : Get started with MicroPython on Raspberry Pi Pico, cap 9 Data logger IMPROVED
# 1.1. -> 2.0 file open with "with"+ + led internal on->off when writing file
# 2.0 --> 3.0 : time stamp with internal clock RTC +
# ATETTION : RTC is well initialised by Thonny, but badly if pico runs independently

# Im- Import the required libraries
from machine import ADC, RTC, Pin
from time import sleep

# IB- Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "None"
p_project = "Internal Temperature & logging with timestamp - file well handling "
p_version = "3.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# START FUNCTIONS -----------
# F.1 - Stores in a file 1 sensor reading + a timestamp
def log_sensor1(timeFormated, sensReading):
    """Guarda añadiendo en un fichero el valor leido de un sensor + una marca de tiempo
        Parametros:
            timeFormated : Marca de tiempo ya formatada
            sensReading : lectura del sensor ya formatada         
        Retorno: Nada            
    """
    tt = f"{timeFormated},{sensReading}"
    # print(tt)
    with open("log_temp.log", "at", encoding="utf-8") as f:
        f.write(tt + "\n")
        
# END FUNCTIONS -----------

# 0- Constates y Variables globales + Objetos
# 0.1- Crea el objeto sensor de temperatura asociado al ADC interno 4 = CORE_TEMP
SensorTemp = ADC(ADC.CORE_TEMP)
DE_U16_aVOLTIOS = 3.3 / (65535)

# 0.2- Crea el objeto Contador en tiempo real con el RTC interno del Pico,
# Thonny lo inicializa con el reloj del PC , sino inicializado mal a 2021
rtc = RTC()

# 0.3- Crea el objeto Led interno para hacer un breve parpadeo al escribir un registro
led = Pin('LED', Pin.OUT)
led.off()


# 1- Bucle infinito de lectura y escritura en fichero
while True:
    voltios = SensorTemp.read_u16() * DE_U16_aVOLTIOS
    temperatura = 27 - (voltios - 0.706)/0.001721 # 1.1 obtiene la temperatura
    
    tsf =rtc.datetime() # 1.2 obtine el tiempo en este momento y lo formatea
    tiempoFormato = "%04d-%02d-%02d,%02d:%02d:%02d"%(tsf[0:3]+tsf[4:7])
    
    print(f"Tiempo: {tiempoFormato} , Temperatura leida = {temperatura:.2f} ºC")
    
    # 1.3 Graba la temperatura con una marca de tiempo
    log_sensor1(tiempoFormato, f"{temperatura:.2f}")
    led.on() # 1.4 visualiza con un breve flash con la escritura de un registro en fichero log
    sleep(0.05)
    led.off()
    
    # 1.5 espera 10 segundos hasta la siguiente lectura
    sleep(10)
    
