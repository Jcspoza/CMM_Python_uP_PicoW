# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 11 - 2
# Goal : Manejar HW a traves de Servicio IoT de Adafruit
# Learning Target : Wifi -> to serve a web page & control Hardware
# Ref : https://youtu.be/Hee9fIwVGFs?si=wMQRjphmhOLLPLtp

# Informative block - start
p_ucontroler = "Pico W only"
p_keyOhw = " NTC on ADC0 + RGB 4pin led common catode, r pin15, g pin13, b pin 14 + LCD i2c 20x4"
p_project = "HW contorl example w. Adafruit IoT - control RGB led & NTC show Temp"
p_version = "2.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

from machine import Pin
from math import log # para calculos del sensor NTC
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from secrets import *
from do_connect import *
import time
import network
import urequests as requests
import ujson

# 0- Crea objetos HW
ESPERA = 60
# 0.1 - Crea el objeto ADC para el sensor NTC: salida sensor a adc0 = gpio 26
# Los otros 2 pines a +3.3 y 0 volt respectivamente
NTC_ADC = 0 # es el ADC0
Rserie = 4700
ntcR0 = 10000
BETA = 3950
ntcRserie = machine.ADC(NTC_ADC)
FACTOR_CONVERSION = 3.3 / (65535)

# 0.2- Crea el objeto rgb led y como es catodo comun lo pone a (-)
red=machine.Pin(15,machine.Pin.OUT)
red.off()
green=machine.Pin(13,machine.Pin.OUT)
green.off()
blue=machine.Pin(14,machine.Pin.OUT)
blue.off()
RGBvalores = {'rgbred': 'OFF', 'rgbgreen': 'OFF', 'rgbblue': 'OFF'}
RGBled = {'rgbred': red, 'rgbgreen': green, 'rgbblue': blue}
# RGBled representa el estado del RGB, las claves son los nombres de los feed de Adafruit

# 0.3 - Constantes para Adafruit IoT
# 'AFIOT_USERNAME' was imported with secrets in module do_connect, use secrets['AFIOT_USERNAME']
# 'AFIOT_KEY' was imported with secrets in module do_connect, use secrets['AFIOT_KEY']
ENCABEZADO = {'X-AIO-Key': secrets['AFIOT_KEY'], 'Content-Type': 'application/json'}

# 0.4-Crea objeto LCD i2c
# Mejor usa las configuraciones por defecto
# I2C0  I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
# I2C1  I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)
i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4), freq=400_000)

# I2C debug block - if all ok comment all lines of block
# i2cDevices = i2c.scan() # this returns a list of devices
# device_count = len(i2cDevices)
# if device_count == 0:
#     print('No i2c devices found.')
#     machine.reset()
# else:
#     print(device_count, 'devices found.')
#     print("I2C Configuration: "+str(i2c))                   # Display I2C config
#     for i2cdevice in i2cDevices:
#         print('I2C address:', i2cdevice, ", Hex address: ", hex(i2cdevice))
# I2C debug block - if all ok comment all lines of block

lcd = I2cLcd(i2c, 0x3E, 4, 20)

# Start function definition -----------------
# las funciones necestan que los objetos como LED RGB o LCD esten creados.
# F.1 
def Temperatura(comentar = False):
    """ Output: temperature float
        Parameter : optional, if comentar = True, it shows debug messages
    """
    voltRserie = ntcRserie.read_u16() * FACTOR_CONVERSION
    ntcResNow = (3.3 - voltRserie) / voltRserie * Rserie
    TempSensor = 1 /(log(ntcResNow/ntcR0)/ BETA + 1/(25+273.15)) -273.15
    # Primero leemos voltaje de punto intermedio de 2 resitencias NTC y R0
    # Segundo hallamos resistencia de NTC
    # Tercero con el valor de resistencia NTC -> temperatura
    
    if comentar :
        print(f"Voltios leidos en sensor NTC (r47K) = {voltRserie:.3f} voltios")
        print(f"Resistencia NTC leida = {ntcResNow:.3f} ohmios")
        print(f"Temperatura leida en NTC = {TempSensor:.2f} grados ºC")
        
    return TempSensor

# F.2 - 
def ComponeURL(nombre_feed, get = True):
    if get:
        urlfinal = "/data/last"
    else:
        urlfinal = "/data"
    
    url = "https://io.adafruit.com/api/v2/" + secrets['AFIOT_USERNAME'] + "/feeds/" + nombre_feed + urlfinal
    return url
# END functions definition -----------------

# 1- (Programa principal) - Presentacion en LCD
lcd.clear()
lcd.move_to(0,0)
lcd.putstr("AdafIoT NTC+RGB"+p_version)

# 2- Bucle principal
try:
    # 2.1- Intenta conexion
    ip=do_connect()
    # conexion STA OK, mostramos ip
    lcd.move_to(0,1)
    lcd.putstr(f"ip {ip}")
    print(ip)
    while True:
        # 2.2 Leer controles HW de Adafruit & Actualizar HW conectadoa PICO
        for lcolor in RGBvalores.keys():
            respuesta = requests.get(ComponeURL(lcolor), headers = ENCABEZADO)
            parsed = ujson.loads(respuesta.text)
            valor = parsed['value']
            RGBvalores[lcolor] = valor
            print(lcolor, valor)
            # Actualizar HW conectado a Pico con lectura de controles
            RGBled[lcolor].value(valor == 'ON')
                            
        print(RGBvalores)
        lcd.move_to(0,2)
        LedState = "R=" + RGBvalores['rgbred'] + "/G=" + RGBvalores['rgbgreen'] + "/B=" + RGBvalores['rgbblue']
        lcd.putstr(LedState)
                
        # 2.3 Escribir Sensores en Adafruit
        Temp2d = {'value': round(Temperatura(), 2)}
        lcd.move_to(0,3)
        lcd.putstr("Temp " + str(Temp2d['value']) +" C")
        print("Temperatura ="+ str(Temp2d['value']) +" C")
        respuesta2 = requests.post(ComponeURL(nombre_feed = 'temperatura', get = False), headers= ENCABEZADO, data=ujson.dumps(Temp2d))
        print(respuesta2.text)
        
        # 2. 4 Bucle de espera con puntos
        for _ in range(ESPERA):
            print('.', end='')
            time.sleep(1)
        print('New round')
        
except KeyboardInterrupt:
    # 3- si CTRL+C se presiona
    lcd.clear()
    machine.reset()

