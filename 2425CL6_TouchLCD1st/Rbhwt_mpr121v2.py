# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase 6
# Programa: Test hw basico de sensor tactil MPR121
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : Mike Causer
# Ref librerias: https://github.com/mcauser/micropython-mpr121/tree/master
# Author : JC Santamaria 
# Date : 2024 - 2 - 18
# Goal : Comprender sensor capacitivo MPR121
# Licencia : CC BY-NC-SA 4.0
# Ref : https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_mpr121.html
# # CONEXIONES
# Pin N		Logic pin		MPR121
# 10		GPIO03			IRQ
# 11		GPIO04-SDA0		SDA
# 12		GPIO05-SCL0		SCL
# 13		GND				GND
# 5			3.3v			3.3 v
# v 2.0 : comprueba que las teclas son 'nuevas'


# I- Import the required libraries
from MPR121mc_LIB import MPR121
from machine import Pin, I2C
import time, os

# Informative block - start
p_ucontroler = "Pico _ & W"
p_keyOhw = "MPR121 on i2c0 GPIO04&05"
p_keyLib = "MPR121 Mike Causer"
p_project = "1st test MPR121- change in keys- No IRQ"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
#print sys info
print(os.uname())
print()
# Informative block - end

# 0- Creo objetos I2C y MPR121
FREQ = 400_000   # Try lowering this value in case of "Errno 5"
TIMEREPms = 300
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)

mpr = MPR121(i2c)

# 1- check all keys
print("Toca la punta de uno de los 12 sensores capacitivos-> aparecera listado")
prev_value = None
startRep = time.ticks_ms
while True:
    value = mpr.get_all_states()
    if (len(value) != 0) and (prev_value != value):
        print(value)
        prev_value = value
        startRep = time.ticks_ms()
    
    time.sleep_ms(100)
    if time.ticks_diff(time.ticks_ms(), startRep) > TIMEREPms:
        prev_value = None
