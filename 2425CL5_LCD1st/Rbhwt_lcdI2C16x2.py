# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase xx
# Programa: Test hw basico de LCD I2C 16 x 2
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : lcd_api.py + pico_i2c_lcd.py
# Ref librerias: https://github.com/T-622/RPI-PICO-I2C-LCD
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0
# char REf https://maxpromer.github.io/LCD-Character-Creator/

from os import uname
# Informative block - start
p_keyOhw = "LCD I2C en GPIO 4&5 = SDA0 & SCL0 / Vcc +5v"
p_project = "Test HW basico de LCDi2c 16x2"
p_version = "1.0"
p_library = "github.com/T-622/RPI-PICO-I2C-LCD"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

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

lcdPresente = False

print('Scanning I2C bus.')
devices = i2c.scan() # this returns a list of devices
device_count = len(devices)
if device_count == 0:
    print('No i2c device found.')
else:
    print(device_count, 'devices found.')
for device in devices:
    print('Decimal address:', device, ", Hex address: ", hex(device))
    lcdPresente = (device == LCD_ADDR) or lcdPresente
print('------------------')
if lcdPresente:
    lcd = I2cLcd(i2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)
    print('Test HW LCD i2c 16x2 Direccion 0x3F/ gipo SDA & SCL 4 & 5')
    lcd.custom_char(0, CH_SMILE)
    lcd.move_to(0,0)
    lcd.putstr("Test HW LCD16i2c")
    lcd.move_to(0,1)
    linea1 = 'd=0x3F/gpio 4&5'+chr(0)
    lcd.putstr(linea1)
else:
    print(lcdPresente)
    print(f'Dispositivo LCD no encontrado en la direccion {LCD_ADDR}')

