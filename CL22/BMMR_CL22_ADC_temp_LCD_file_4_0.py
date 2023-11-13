# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 5 - 11
# Goal : Internal temperature sensor reading & logging in a file
# Learning Target : Analog digital converter basic + file handling IMPROVED
# Ref : Get started with MicroPython on Raspberry Pi Pico, cap 9 Data logger IMPROVED
# 1.1. -> 2.0 file open with "with"+ + led internal on->off when writing file
# 2.0 --> 3.0 : time stamp with internal clock RTC +
# 4.0 -> add LCD
# ATETTION : RTC is well initialised by Thonny, but badly if pico runs independently
# TO DO´s
# a- Funcionado de forma aislada añadir pulsador para hacer un efecto = ctrl+C
# b- puede haber un pequeño error en el cambio de fecha si ocurre en lin3
# b-> incluir el bucle for escritura de lin1,2 y 3 en cada lectura + almacenar las 2 ultimas lecturas 

# Im- Import the required libraries
from machine import ADC, RTC, Pin, I2C
from time import sleep
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# IB- Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "None"
p_project = "Internal Temperature show & LCD + logging with timestamp in a file"
p_version = "4.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0- Creacion de Objetos
# 0.1- Crea el objeto sensor de temperatura asociado al ADC interno 4 = CORE_TEMP
SensorTemp = ADC(ADC.CORE_TEMP)
DE_U16_aVOLTIOS = 3.3 / (65535)

# 0.2- Crea el objeto Contador en tiempo real con el RTC interno del Pico,
# Thonny lo inicializa con el reloj del PC , sino inicializado mal a 2021
rtc = RTC()

# 0.3- Crea el objeto Led interno para hacer un breve parpadeo al escribir un registro
led = Pin('LED', Pin.OUT)
led.off()

# 0.4- Crea el objeto LCD
# Usa las configuraciones por defecto I2C0  I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
lcd = I2cLcd(i2c, 0x3E, 4, 20)

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

# 1- (Programa principal) - Presentacion en LCD
lcd.clear()
lcd.move_to(0,0)
lcd.putstr("Int Temp file+LCD"+p_version)

# 2- Try - Except : 
try:
    while True: # -3 Bucle de lectura y escritura en fichero
        tsf = rtc.datetime() # -3.1 obtine la fecha + la escribe en LCD lin1
        fechaFormato = f"Fecha :{tsf[0]:04d}-{tsf[1]:02d}-{tsf[2]:02d}"
        lcd.move_to(0,1)
        lcd.putstr(fechaFormato)
        for l in range(2,4): # -3.2 bucle for para scroll de las 2 ultimas lineas LCD
            voltios = SensorTemp.read_u16() * DE_U16_aVOLTIOS
            temperatura = 27 - (voltios - 0.706)/0.001721 # obtiene la temperatura
            tsf =rtc.datetime() # -3.2.1 obtine hora en este momento+escribe en LCD
            lcd.move_to(0,l)
            lcd.putstr(f"{tsf[4]:02d}:{tsf[5]:02d}:{tsf[6]:02d} T= {temperatura:.2f}")
            tiempoFormato = f"{tsf[0]:04d}-{tsf[1]:02d}-{tsf[2]:02d},{tsf[4]:02d}:{tsf[5]:02d}:{tsf[6]:02d}"
            print(f"Tiempo: {tiempoFormato} , Temperatura leida = {temperatura:.2f} ºC")
            
            # -3.2.2 Graba la temperatura con una marca de tiempo
            log_sensor1(tiempoFormato, f"{temperatura:02.02f}")
            led.on() # -3.2.4 visualiza con un breve flash con la escritura de un registro en fichero log
            sleep(0.05)
            led.off()
                        
            # -3.2.5 espera 10 segundos hasta la siguiente lectura
            sleep(10)
    
except KeyboardInterrupt: # -2.2 si CTRL+C se presiona - > limpiar display
    lcd.clear()