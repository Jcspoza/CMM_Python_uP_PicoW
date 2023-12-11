# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 21
# Goal : Basic HW test display I2C oled ssd1306 ONLY text
# Learning Target :
# Ref: Electrocredible.com, Language: MicroPython

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "SSD1306 I2c1 SDA pin6, SCL pin7, VCC3.3volt"
p_project = "BHWT text only + scroll - ssd1306 Pico_&W i2c 1 - default pins"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0.0 - Constates y varaibles globales
WIDTH =128 
HEIGHT= 64

# 0.1 Objeto I2C y LCD
# Mejor usa las configuraciones por defecto
# i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)

print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c) # constructor - I2C direccion 3C por defecto

# 1- Programa Principal
oled.fill(0) # clear screen

# 2- los chr son 8x8 es decir puedo pensar en lineas de 8 pixeles en vertical
for l in range (0,8):
    oled.text('Linea ' + str(l), l * 10, l * 8, 1)

oled.show()

# 3- Scroll horizontal derecha y luego a izquierda
for _ in range(0, WIDTH//2):
    oled.scroll(1,0)
    oled.show()
    utime.sleep(0.1)
    
for _ in range(0, WIDTH//2):
    oled.scroll(-1,0)
    oled.show()
    utime.sleep(0.1)
    
# 4 redibuja la pantall
oled.fill(0) # clear screen
for l in range (0,8):
    oled.text('Linea ' + str(l), l * 10, l * 8, 1)
oled.show()

# 5- Scroll vertical arriba y abajo
for _ in range(0, HEIGHT//2):
    oled.scroll(0,1)
    oled.show()
    utime.sleep(0.1)
    
for _ in range(0, HEIGHT//2):
    oled.scroll(0,-1)
    oled.show()
    utime.sleep(0.1)
    
