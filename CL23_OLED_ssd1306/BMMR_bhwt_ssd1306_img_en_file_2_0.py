# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 21
# Goal : ADVANCED HW test Pico and display I2C oled ssd1306
# Learning Target :
# Ref: https://controlautomaticoeducacion.com/micropython/display-oled-raspberry-pi-pico-esp8266/

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from utime import sleep_ms
import framebuf

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "SSD1306 I2c1 SDA pin6, SCL pin7, VCC3.3volt"
p_project = "Test Imagen en FILE - ssd1306 Pico_&W i2c 1 - default pins"
p_version = "2.0"
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

# 0.2 Imagen desde fichero 128 * 64 bits = list of 1024 bytes
with open('cab90gmono2.pbm', 'rb') as f:   # Abre el fichero para lectura en modo binario
    f.readline()                                # Salta la línea del identificador mágico
    f.readline()                                # Salta la línea de comentario (descomentar si existe)
    # f.readline()                                # Salta la línea de las dimensiones de la imagen
    data = bytearray(f.read())                  # Lee los datos de la imagen
fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)   # Datos y tamaño de la imagen...

# 1- Programa Principal - Presentacion
oled.fill(0) # clear screen
oled.show()

oled.fill(0)
oled.text("Test", (WIDTH - len("Test")*8) // 2, 0)
oled.text("de", (WIDTH - len("de")*8) // 2, 20)
oled.text("Imagen en FILE2", (WIDTH - len("Imagen en FILE2")*8) // 2, 40)
oled.show()
sleep_ms(3000)
oled.fill(0)
oled.show()

## 2- Muestra Imagen
oled.fill(0)
oled.blit(fbuf,0,0)
oled.show()
# sleep_ms(3000)
# oled.fill(0)
# oled.show()
