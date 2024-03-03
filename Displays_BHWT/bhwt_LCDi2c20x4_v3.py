# import the required libraries
import utime
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

LCD_ADDR = 0x3E
LCD_NUM_ROWS = 4
LCD_NUM_COLS = 20
FREQ = 400_000   # Try lowering this value in case of "Errno 5"
CH_SMILE = [0x00, 0x11, 0x00, 0x04, 0x04, 0x11, 0x0E, 0x00]

i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)

print('Scanning I2C bus.')
devices = i2c.scan() # this returns a list of devices
device_count = len(devices)
if device_count == 0:
    print('No i2c device found.')
else:
    print(device_count, 'devices found.')
for device in devices:
    print('Decimal address:', device, ", Hex address: ", hex(device))

lcd = I2cLcd(i2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

# - Presentacion test
linea0 = 'Test3 HW LCD20x4 i2c'
lcd.putstr(linea0)
utime.sleep(3)

print("Llenar display con todos los caracteres")
lcd.clear()
string = ""
for x in range(32, 32+LCD_NUM_ROWS * LCD_NUM_COLS):
    string += chr(x)
lcd.putstr(string)
utime.sleep(3)

lcd.clear()
string = ""
for x in range(112, 112+LCD_NUM_ROWS * LCD_NUM_COLS):
    string += chr(x)
lcd.putstr(string)
utime.sleep(3)

lcd.clear()
string = ""
for x in range(192, 256):
    string += chr(x)
lcd.putstr(string)
utime.sleep(3)

print("Llenar display con mensaje de prueba")
lcd.clear()
lcd.custom_char(0, CH_SMILE)
linea0 = chr(0)+' BM Makers '+chr(0)
lcd.move_to((LCD_NUM_COLS - len(linea0))//2, 0) # centra la cadena de claracteres
lcd.putstr(linea0)
lcd.move_to(0,1)
lcd.putstr("Raspberry Pi Pico W")
lcd.move_to(0,2)
lcd.putstr("LCD i2c 20x4 dir0x3E")
lcd.move_to(0,3)
time = utime.localtime()
lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}:{SS:>02d}"
           .format(year=time[0], month=time[1],day=time[2],
                   HH=time[3], MM=time[4], SS=time[5]))
