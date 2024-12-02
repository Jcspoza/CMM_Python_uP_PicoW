# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase xx
# Programa: Test hw basico de LCD I2C 16 x 2 - Mostrar todos los caracteres
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : lcd_api.py + pico_i2c_lcd.py
# Ref librerias: https://github.com/T-622/RPI-PICO-I2C-LCD
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0

from os import uname
# Informative block - start
p_keyOhw = "LCD I2C en GPIO 4&5 = SDA0 & SCL0 / Vcc +5v"
p_project = "Todos los characteres en LCDi2c 16x2"
p_version = "1.0"
p_library = "github.com/T-622/RPI-PICO-I2C-LCD"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print()
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")
print('---------------- ==== ----------------')

# import rest of required libraries
import utime
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

LCD_ADDR = 0x3F
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16
FREQ = 400_000   # Try lowering this value in case of "Errno 5"

i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)
lcd = I2cLcd(i2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

print("Llenar display con todos los caracteres")
lcd.clear()
string = ""

for setStart in range(32, 256, 32):
    print(f'Set de 32 caracteres que comienzan en {setStart}')
    if setStart ==128:
        print('  ->Salto el set de caracteres que comienzan en 128')
        continue
    
    for x in range(setStart , setStart + LCD_NUM_ROWS * LCD_NUM_COLS):
        string += chr(x)
        
    lcd.putstr(string)
    utime.sleep(5)
    lcd.clear()
    string = ""