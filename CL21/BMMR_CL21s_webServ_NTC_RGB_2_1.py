# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 10 - 31
# Goal : Manejar HW a traves de una pagina web (intranet)
# Learning Target : Wifi -> to serve a web page & control Hardware
# Ref : https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/7.web_page.html
# 1.0 -> 1.1 pasar a catodo comun ejemplo de sunfounder
# -> 2.0 añadir LCD
# -> 2.1 linea en pagina web con estado del led

import machine
import socket
from math import log # para calculos del sensor NTC
from secrets import *
from do_connect import *
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Informative block - start
p_ucontroler = "Pico W only"
p_keyOhw = " NTC on ADC0 + RGB 4pin led common catode, r pin15, g pin13, b pin 14 + LCD i2c 20x4"
p_project = "Web Server STA mode - control REGB led & NTC show Temp"
p_version = "2.1"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0- Crea objetos HW
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

# 0.3-Crea objeto LCD i2c
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
# F.1 - 
def temperature(comentar = False):
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
def CreaWebpage2(TempValue, ledStateString):
    """ Output: web page in html languaje, string
        Parameter : mandatory, Temperature value to include in web page
    """
    html = f"""
            <!DOCTYPE html>
            <html>
            <body>
            <h1>Control de Ledx3 y visualiza temperatura-CMM Benito Martin Makers</h1>
            <p>Presiona uno de los 4 botones para cambiar el color del led</p>
            <form action="./red">
            <input type="submit" value="red " />
            </form>
            <form action="./green">
            <input type="submit" value="green" />
            </form>
            <form action="./blue">
            <input type="submit" value="blue" />
            </form>
            <form action="./off">
            <input type="submit" value="off" />
            </form>
            <p>Temperatura es de {TempValue} grados Celsius</p>
            <p>Estado del led RGB: {ledStateString} </p>
            </body>
            </html>
            """
    return html

# F.3 - 
def open_socket(ip):
    """ Handling all TCP/IP server initial actions
        Output: Server socket after .listen(..) 
        Parameter : ip address of Pico W to be the server´s IP
    """
    address = (ip, 80) # prepara la tupla de direccion TCP/IP (ip, port)
    # la implementacion de upython en pico permite uso de tupla directamente en bind
    SerSocket = socket.socket() # Server socket
    # default TCP/IP socket = socket.socket(af=AF_INET, type=SOCK_STREAM)¶
    SerSocket.bind(address)
    SerSocket.listen(1)
    print(SerSocket)
    return(SerSocket)

# F.4 - 
def serve(Ssocket):
    """ Server logic in endless loop. 
        Parameter : Server socket after .listen(..) 
    """
    while True:
        ClientSocket = Ssocket.accept()[0]
        ClientAnswerBin = ClientSocket.recv(1024)
        ClientSocket.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n') #respuesta HTTP
        # Nota avanzada: si no se envia el '200 ok' las paginas web se muestran con desfase
        # en algun navegador
        ClientAnswer = str(ClientAnswerBin)
        print(ClientAnswer) # trace 
        try:
            ClientAnswerLedOrder = ClientAnswer.split()[1]      
            print(ClientAnswerLedOrder)
            lcd.move_to(0,2)
            if ClientAnswerLedOrder == '/off?':
                red.low()
                green.low()
                blue.low()
                LedState = "TODOS los led off   "
            elif ClientAnswerLedOrder == '/red?':
                red.high()
                green.low()
                blue.low()
                LedState = "RED on, resto off   "
            elif ClientAnswerLedOrder == '/green?':
                red.low()
                green.high()
                blue.low()
                LedState = "GREEN on, resto off "
            elif ClientAnswerLedOrder == '/blue?':
                red.low()
                green.low()
                blue.high()
                LedState = "BLUE on, resto off  "
            elif ClientAnswerLedOrder == '/': # 1st connection
                red.low()
                green.low()
                blue.low()
                LedState = "                    "
            
            lcd.putstr(LedState)
            Tvalue='%.2f'%temperature()
            lcd.move_to(0,3)
            lcd.putstr(f"Temp " + Tvalue +" C")
            html=CreaWebpage2(Tvalue, LedState)
            ClientSocket.send(html)
            ClientSocket.close()
        
        except IndexError:
            print("Index Error in Answer from client")

# END functions definition -----------------
# 1- (Programa principal) - Presentacion en LCD
lcd.clear()
lcd.move_to(0,0)
lcd.putstr("ServerSTA NTC+RGB"+p_version)

# 2- Bucle principal
try:
    # 2.1- Intenta conexion
    ip=do_connect()
    # conexion STA OK, mostramos mensaje
    lcd.move_to(0,1)
    lcd.putstr(f"ip {ip}")
    print(ip)
    if ip is not None:
        # 2.2- Si conex exitoosa con IP, crea socket Server
        ServerSocket=open_socket(ip)
        lcd.move_to(0,2)
        lcd.putstr("Server waiting-1 max")
        # 2.3- Bucle de servidor WEB
        serve(ServerSocket)
except KeyboardInterrupt:
    # ERROR - si CTRL+C se presiona
    lcd.clear()
    machine.reset()

