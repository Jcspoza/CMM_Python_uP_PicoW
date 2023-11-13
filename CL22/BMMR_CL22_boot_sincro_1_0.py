# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 7 - 26
# Goal : Boot de conexion a wifi y sincronizacion de RTC + desconexion de wifi

#
# COMO USAR 
# 1- salvar como boot.py
#

import network, time, ntptime
from secrets import *
from machine import RTC

# 0- Constates y Variables globales + Objetos
TIMEZONE = 1 # sPAIN IS gmt +1
ntptime.host = 'ntp.roa.es' # servidor NTP de España,
# pero no hace falta se pude usar servidor por defecto
ssid = secrets['ssid']
psk = secrets['password']
comment = False

# F- funciones
# F.2 - Set time con Time zone y DST
# There's currently no timezone support in MicroPython, and the RTC is set in UTC time.
def setLtime():
    """ Set RTC date and time synchronised with NTP server. Manages Time zone and DST
        Fork of settime in ntptime library
    """
    t = ntptime.time() # obtain time from NTP server
    tm = time.gmtime(t) # conversion to tupla 
    if (tm[1] > 3) and (tm[1] < 11): # aproximation to DST calculus, valid except max 7 days
        dst = 1 # if month is april, ......october +1
    else:
        dst = 0
    
    RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3] + TIMEZONE + dst, tm[4], tm[5], 0))
    # order of tuplan in time and RTC is different
    # RTC : (year, month, day, weekday, hour, minute, second, ??)
    # micropython RTC port : Deliberately ignore the weekday argument and compute the proper value
    # time : (year, month, mday, hour, minute, second, weekday, yearday) weekday is 0-6 for Mon-Sun

# F- funciones

wStatusDef = {-3:'ERROR_WRONG_PASSWORD',
              -2:'ERROR_NO_AP_FOUND',
              -1:'ERROR_CONNECT_FAIL',
              1:'STAT_CONNECTING',
              0:'STAT_IDLE',
              2:'STAT_NO_IP',
              3:'STAT_Connected'}


# Set country to avoid possible errors
network.country('ES')
if comment:
    print('"do_connect" function version = 1.9')
    print('Country set to =', network.country())
    print('Connecting to WiFi Network Name:', secrets['ssid'])

# 1- Crea un objeto wireless local area network en modo estacion
wlan = network.WLAN(network.STA_IF)

# 2- Activa el circuito wifi - tarda unos segundos
wlan.active(True)
wlan.config(pm = 0xa11140) # Desactiva el modo de bajo consumo

# 3- se conecta a la red wifi SSID con la clave PASSWORD,
wlan.connect(ssid, psk)    

# 4 - hacer un maximo de 10 intentos de conexionm con una espera de 1 seg
wait = 10
wStatus = wlan.status()
while wait > 0 and (wStatus >= 0 and wStatus < 3):
    # 3 posibilidades de salir del bucle: 1->numero de intentos O
    # 2->por error wStatus = -3, -2 o -1
    # 3-> conexion con exito que es wStatus = 3
    wStatus = wlan.status()
    wait -= 1
    if comment:
        print(secrets['ssid'] + ' Wlan Status = '+ wStatusDef[wStatus])
    
    time.sleep(1)

# 4 Compruebo si salio por error, es decir wStatus distinto de 3              
if wStatus != 3:
    raise RuntimeError('Wifi connection failed-'+ wStatusDef[wStatus])
else:
    # Conexion exitosa!!
    print('CONNECTED-'+wStatusDef[wStatus])
    ip=wlan.ifconfig()[0] # extrae la direccion ip de PICO W, util para conectar
    print(ip)
                    
    if comment:
        print('Wlan param ip add, mask, gateway & DNS server:', wlan.ifconfig())
        print('id net =', wlan.config('ssid'))
        print('channel =', wlan.config('channel'))
        print('TX power =', wlan.config('txpower'))
        a = wlan.config('mac')
        # MAC Addresses are unique 48-bit hardware number, or 6 bytes
        # MAC is commonly represented as 12 hex digitts
        # To make that conversion consider 'a' as string -> extrtact ead char -> repesent char code in hex
        print(f"Physical-mac add {a[0]:02x}:{a[1]:02x}:{a[2]:02x}:{a[3]:02x}:{a[4]:02x}:{a[5]:02x}")
        print('OUI = 28:CD:C1 => Raspberry Pi Trading Ltd')   

# 5 - Sincronizacion con ntp
try:
    # sincroniza RTC con hora Local
    setLtime()
    print("Sincronizacion de RTC a hora local")
except:
    #Error NTP
    print("Error NTP")

# 6- Desconectar del router
wlan.disconnect()
print("Desconexion del router")

# 7- Desconectar el HW WIFI
wlan.active(False)
print("Desactivar wifi PICO w")