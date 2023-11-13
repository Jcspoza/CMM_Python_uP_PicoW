# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 7 - 10
# Goal : Reloj en LCD sincronizaco por NTP
# Ref 

# Im- Import the required libraries
from machine import Pin, I2C, RTC
import utime, ntptime
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from do_connect import *

# IB- Informative block - start
p_ucontroler = "Pico W ONLY"
p_keyOhw = "LCD I2c 20x4 - sda=GPIO0, scl=GPIO1 & vcc lcd on VBUS"
p_project = "LCD Clock sinchronised by NTP"
p_version = "4.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0- Constates y Variables globales + Objetos
TIMEZONE = 1 # sPAIN IS gmt +1
LCD_ADDR = 0x3E
LCD_NUM_ROWS = 4
LCD_NUM_COLS = 20
FREQ = 400_000   # Try lowering this value in case of "Errno 5"
CH_SMILE = [0x00, 0x00, 0x11, 0x04, 0x04, 0x11, 0x0E, 0x00]
ntptime.host = 'ntp.roa.es' # servidor NTP de España,
# pero no hace falta se pude usar servidor por defecto

# 0.1 LCD
# Usa las configuraciones por defecto I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=FREQ)
lcd = I2cLcd(i2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

# F- funciones
# F.1 - Settime con Time zone y DST
# There's currently no timezone support in MicroPython, and the RTC is set in UTC time.
def setLtime():
    """ Set RTC date and time sinchronised with NTP server. Manages Time zone and DST
        Fork of settime in ntptime library
    """
    t = ntptime.time() # obtain time from NTP server
    tm = utime.gmtime(t) # conversion to tupla 
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

# 1- Mensajes de inicio en LCD y consola
print("Mensaje de Inicio")
lcd.clear()
lcd.custom_char(0, CH_SMILE)
linea0 = chr(0)+' BM Makers '+chr(0)
lcd.move_to((LCD_NUM_COLS - len(linea0))//2, 0) # centra la cadena de claracteres
lcd.putstr(linea0)
lcd.move_to(0,1)
lcd.putstr("PicoW+LCD->"+str(hex(LCD_ADDR)))
lcd.move_to(0,2)
lcd.putstr("Reloj sinc NTP v" + p_version)
lcd.move_to(0,3)
lcd.putstr("Connec. wifi=")
try: # 2- Conexion a internet
    do_connect()
    lcd.putstr("OK")
except RuntimeError as et:
    print(et)
    ets = str(et)
    lcd.putstr("NOK")
    lcd.move_to(0,2)
    lcd.putstr(ets.split('-')[1])
    
    
utime.sleep(4)

# 3- Mensajes de hora inicial
lcd.clear()
lcd.putstr("BMmk clock al Inicio")
lcd.move_to(0,1)
Itime = utime.localtime()
lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}"
           .format(year=Itime[0], month=Itime[1],day=Itime[2],
                   HH=Itime[3], MM=Itime[4]))
print ("Hora inicial: ", Itime)

try: # 4- sincroniza RTC con hora GMT
    setLtime()
    
except:  #Error NTP
    print("Error NTP")
    lcd.clear()
    lcd.putstr("Error NTP")
    
# 5- Mensajes de hora Sincronizada
lcd.move_to(0,2)
lcd.putstr("BMmk clock sinc. Local")
lcd.move_to(0,3)
Ltime = utime.localtime()
lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}"
           .format(year=Ltime[0], month=Ltime[1],day=Ltime[2],
                   HH=Ltime[3], MM=Ltime[4]))
print ("Hora sincronizada Local: ", Ltime)
