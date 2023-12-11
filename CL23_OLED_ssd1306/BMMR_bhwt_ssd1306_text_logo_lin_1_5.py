# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 21
# Goal : Basic HW test Pico and display I2C oled ssd1306
# Learning Target :
# Ref: Electrocredible.com, Language: MicroPython

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "SSD1306 I2c1 SDA pin6, SCL pin7, VCC3.3volt"
p_project = "BHWT ssd1306 Pico_&W i2c 1 - default pins"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

WIDTH =128 
HEIGHT= 64
# Mejor usa las configuraciones por defecto
# i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)

print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c) # constructor - I2C direccion 3C por defecto

oled.fill(0) # clear screen
# Micropython logo
oled.fill_rect(0, 0, 32, 32, 1)
oled.fill_rect(2, 2, 28, 28, 0)
oled.vline(9, 8, 22, 1)
oled.vline(16, 2, 22, 1)
oled.vline(23, 8, 22, 1)
oled.fill_rect(26, 24, 2, 4, 1)

oled.text('BM Makers', 40, 0, 1)
oled.text('Pico W &', 40, 12, 1)
oled.text('OLED 128x64', 40, 24, 1)
oled.text('JC Santamaria', 6, 34, 1)
oled.text('30 Septiemb 2023', 0, 44, 1)
oled.show()
