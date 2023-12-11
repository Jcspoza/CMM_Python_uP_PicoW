# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 21
# Goal : Graphic draw HW test Pico and display I2C oled ssd1306
# Learning Target : Hacerlo a mi manera desde cero
# Ref: https://controlautomaticoeducacion.com/micropython/display-oled-raspberry-pi-pico-esp8266/
# 

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from utime import sleep_ms

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "SSD1306 I2c1 SDA GPIO06, SCL GPIO07, VCC3.3volt + potenciopnmeter GPIO26 - ADC0"
p_project = "Draw a Volts - parte 1 solo texto arriba"
p_version = "p.1"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0- Constantes y variables globales
WIDTH =128 # anchura display
HEIGHT= 64 # altura display
W1CHAR = 8
H1CHAR = 8
ADCtoVolt = 3.3 / (65535) # Factor conversion ADC -> voltios

# Division en Zonas del display
# Hay una zona top solo para texto
# En la zona debajo de la top, tenemos a la izq zona Left + zona grafica
# la zona grafica tien Eje Y , zona de dibujo , abajo del todo Eje X

DZTOP = [0, 0, WIDTH-1, H1CHAR+1] # Zone top SOLO texto x e y (top left) y ancho x alto

# Fin division en zonas del display

TIMEREAD = 100 # Tiempo entre lecturas en msegundos

# ---------------- START FUNCTIONS -----------------
    
# ---------------- END FUNCTIONS -----------------
# 1 - Creacion de objetos , i2c, oled y potenciometro sobre ADC
# I2C - Usa las configuraciones por defecto I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000, timeout=50000)
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)

oled = SSD1306_I2C(WIDTH,HEIGHT,i2c) # constructor OLED - I2C direccion 3C por defecto
pot = ADC(26) # constructor de potenciometro sobre ADC0

# 2- Limpia pantalla
oled.fill(0) # clear screen
oled.show()

# 3- Presentacion inicial
oled.fill(0)
oled.text("Zero Base- Test", 0, 0)
oled.text(" de Dibujar ", 16, 20)
oled.text("un grafico" + "/" + p_version, 0, 40)
oled.show()
sleep_ms(3000)
oled.fill(0) # borrar pantalla
oled.show()

#4.x Bucle inicial propiamente 
while True:
    
    # 4.x Leer voltios
    volts = pot.read_u16() * ADCtoVolt
    # print(f"Voltios leidos = {volts} volttios")
    
    # 4.5 Escritura en zona TOP de los voltios leidos y version del progrma
    oled.fill_rect(DZTOP[0], DZTOP[1], DZTOP[2], DZTOP[3], 0) # borra el area de texto superior 120 ancho y 10 alto
    ltop = "Volts=" + str(round(volts,1)) + " /" + p_version
    oled.text(ltop, DZTOP[0], DZTOP[1])
          
    oled.show() # 4.7 dibujo Zona Top 
    
    sleep_ms(TIMEREAD)

