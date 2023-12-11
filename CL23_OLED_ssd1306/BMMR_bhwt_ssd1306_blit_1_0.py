# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 21
# Goal : Basic HW test display I2C oled ssd1306 ONLY text
# Learning Target :
# Ref: Electrocredible.com, Language: MicroPython

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "SSD1306 I2c1 SDA pin6, SCL pin7, VCC3.3volt"
p_project = "BHWT blit 1 - ssd1306 Pico_&W i2c 1 - default pins"
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
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c) # constructor - I2C direccion 3C por defecto

# 1- Programa Principal - clear screen
oled.fill(0)

# 2- Crea un frame buffer de 8 x 8 mono color vertical bit menos significatico
fbuf = framebuf.FrameBuffer(bytearray(8 * 1 * 1), 8, 8, framebuf.MONO_VLSB)

# 3 - Dibuja una X en el bufer 8 x 8
fbuf.line(0, 0, 7, 7, 1)
fbuf.line(0, 7, 7, 0, 1)

# 4- Dibuja el buffer 6 veces diagonal / key=0 significa que valores 0 no se dibujan
for i in range(0,60,10):
    oled.blit(fbuf, i, i, 0)

# 5 - Muestra
oled.show()
