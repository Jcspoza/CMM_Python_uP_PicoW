# import the required libraries

from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

LCD_ADDR = 0x3F
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16
FREQ = 400_000   # Try lowering this value in case of "Errno 5"
CH_SMILE = [0x00, 0x11, 0x00, 0x04, 0x04, 0x11, 0x0E, 0x00]

# Mejor usa las configuraciones por defecto
# I2C0  I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
# I2C1  I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)
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

print('Test HW Pico_&W: LCD i2c 16x2 3F')
lcd.custom_char(0, CH_SMILE)
lcd.move_to(0,0)
lcd.putstr("Test HW Pico_&W")
lcd.move_to(0,1)
linea1 = chr(0)+'LCDi2c16x2 3F '+chr(0)
lcd.putstr(linea1)

