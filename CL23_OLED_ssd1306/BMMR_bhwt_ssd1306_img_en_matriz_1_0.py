# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 21
# Goal : ADVANCED HW test Pico and display I2C oled ssd1306
# Learning Target :
# Ref: https://controlautomaticoeducacion.com/micropython/display-oled-raspberry-pi-pico-esp8266/

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from utime import sleep_ms

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "SSD1306 I2c1 SDA pin6, SCL pin7, VCC3.3volt"
p_project = "Test Imagen en Matriz - ssd1306 Pico_&W i2c 1 - default pins"
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

# 1- Programa Principal - Presentacion
oled.fill(0) # clear screen
oled.show()

oled.fill(0)
oled.text("Test", (WIDTH - len("Test")*8) // 2, 0)
oled.text("de", (WIDTH - len("de")*8) // 2, 20)
oled.text("Imagen en Matriz", (WIDTH - len("Imagen en Matriz")*8) // 2, 40)
oled.show()
sleep_ms(3000)
oled.fill(0)
oled.show()

## 2- Imagen de un corazon en formato Matriz
ICONO = [                              # Matriz 10 x 10  de puntos 1=color, 0= sin color
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [ 0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [ 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [ 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [ 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [ 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

for i in range(0,60,10):
    xi = yi = i
    for y, fila in enumerate(ICONO):       # Dibuja los puntos de la matriz  
        for x, c in enumerate(fila):
            oled.pixel(xi + x, yi + y, c)
            
oled.show()                            # Muestra el resultado