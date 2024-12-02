# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase xx
# Programa: Test hw basico de LCD I2C 16 x 2 - Mostrar Reloj cada segundo
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : lcd_api.py + pico_i2c_lcd.py
# Ref librerias: https://github.com/T-622/RPI-PICO-I2C-LCD
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0

from os import uname
# Informative block - start
p_keyOhw = "LCD I2C en GPIO 4&5 = SDA0 & SCL0 / Vcc +5v"
p_project = "Reloj digital +1seg en LCDi2c 16x2"
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

print("Reloj digital de incremento 1 segundo")

lcd.clear()
lcd.putstr("LCDi2c Reloj +1s")

while True:
    try:
        lcd.move_to(0,1)
        time = utime.localtime()
        horastr = f'{time[2]:>02d}de {time[1]:>02d}>{time[3]:>02d}:{time[4]:>02d}:{time[5]:>02d}'
        lcd.putstr(horastr)
        utime.sleep(1)
    except KeyboardInterrupt:
        lcd.clear()
        lcd.putstr('Fin de programa')
        print('Fin de programa - por interrupcion de teclado')
        utime.sleep(2)
        lcd.clear()
        break
    
