# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 21
# Goal : Graphic draw HW test Pico and display I2C oled ssd1306
# Learning Target :
# Ref: https://controlautomaticoeducacion.com/micropython/display-oled-raspberry-pi-pico-esp8266/
# 3_0 -> 3.1 comentarios

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from utime import sleep_ms
import framebuf


# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "SSD1306 I2c1 SDA GPIO06, SCL GPIO07, VCC3.3volt + potenciopnmeter GPIO26 - ADC0"
p_project = "Draw a Volts- graphic Test ssd1306 Pico_&W i2c 1 - default pins"
p_version = "3.1"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# ---------------- START FUNCTIONS -----------------
def plot_time(yp, t, x, y, var = [0.0,3.3], vpts=[25, 16, 40], hpts = [25, 55, 112]):
    """"
    Graph function of the Cartesian plane in relation to time:
    by: Sergio Andres Castaño Giraldo
    
    plot_time(yp, t, x, y, var = [0.0,3.3], vpts=[25, 16, 40], hpts = [25, 55, 112]):

    yp: dependent variable
    t: time (used while the Cartesian plane is not complete)
    x: List of two positions of variable x, x[0] is the position in past x and x[1] position of current x.
    y: List of two positions of the variable y, y[0] is the position in past and y[1] position of current x.
    var = [0.0,3.3]: Magnitude of the variable (default voltage)
    vpts = [25, 16, 40]: points on the vertical y axis.
    hpts = [25, 55, 112]: points on the vertical x axis.

    Example:
    #Global Variables
    t = 0
    y = [55, 55]
    x = [25, 25]
    #Function:
    volts = pot.read_u16 () * FACTOR
    t, x, y = plot_time (volts, t, x, y)
    sleep_ms (500)
    """
    #Axis
    oled.vline(vpts[0], vpts[1], vpts[2], 1) #x, y, h - dibuja eje vertical
    oled.hline(hpts[0], hpts[1], hpts[2], 1) #x, y, w - dibuja eje horizontal
    oled.text(str(round(var[0],1)), vpts[0]-25, hpts[1]-5)
    oled.text(str(round(var[1],1)), vpts[0]-25, vpts[1])
    #y - axis
    y[1] = int((yp-var[0])/(var[1]-var[0]) * (vpts[1]-hpts[1]) + hpts[1]) #Interpolation
    if t < hpts[2] - hpts[0]: 
        x[1] = x[0]+1
        print(t, x[1])
    else:
        x[1] = hpts[2]
        # print(t, x[1])
        
    
    #Plot the line
    oled.line(x[0],y[0],x[1],y[1],1)
    oled.show()
    
    #Update past values
    y[0] = y[1]
    x[0] = x[1]
    
    #If you have already reached the end of the graph then ...
    if t > hpts[2] - hpts[0]:
        #Erases the first few pixels of the graph and the y-axis.
        oled.fill_rect(vpts[0],vpts[1],2,vpts[2],0)
        #Clears the entire y-axis scale
        oled.fill_rect(vpts[0]-25, vpts[1],vpts[0],vpts[2]+5,0)
        #shifts the graph one pixel to the left
        oled.scroll(-1,0)
        #Axis
        oled.vline(vpts[0], vpts[1], vpts[2], 1) #x, y, h
        oled.hline(hpts[0], hpts[1], hpts[2], 1) #x, y, w
        oled.text(str(round(var[0],1)), vpts[0]-25, hpts[1]-5)
        oled.text(str(round(var[1],1)), vpts[0]-25, vpts[1])
    else:
        t += 1
    
    return t,x,y
# ---------------- END FUNCTIONS -----------------
# 0- Constantes y variables globales
WIDTH =128 # anchura display
HEIGHT= 64 # altura display
FACTOR = 3.3 / (65535) # Factor conversion ADC -> voltios
#Global Variables
t = 0
y = [55, 55]
x = [25, 25]

# 1 - Creacion de objetos , i2c, oled y potenciometro sobre ADC
# Mejor usa las configuraciones por defecto
# i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400_000)
# i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000, timeout=50000)
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400_000)

print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display 1st i2c device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SSD1306_I2C(WIDTH,HEIGHT,i2c) # constructor - I2C direccion 3C por defecto
pot = ADC(26) # constructor de potenciometro sobre ADC0

# 2- Limpia pantalla y escribe mensaje inicial
# oled.fill(0) # clear screen
# oled.show()
oled.fill(0)
oled.text("Test de ", 35, 0)
oled.text("Dibujar ", 20, 20)
oled.text("un grafico", 25, 40)
oled.show()

# espera 3 segundos y limpia oled
sleep_ms(3000)
oled.fill(0)
oled.show()

# 4 - Bucle de repticion
while True:
    # 4.1 Lee los voltios y los mustra en texto
    oled.fill_rect(0,0,120,15,0) # borra el area de texto superior 120 ancho y 15 alto, desde 0,0 arriba izq
    volts = pot.read_u16() * FACTOR
    oled.text("Volts: ", 0, 0)
    oled.text(str(round(volts,1)), 52, 0) # 1 decimal, en posicion x=52 y = 0
    
    # 4.2 Dibuja en un grafico los voltios leidos + hace scroll + salida nuevos valores de t,x,e y
    t,x,y = plot_time(volts,t,x,y)
    
    # 4.3 Muestra los dibujado en memoria a display
    oled.show()
    sleep_ms(100) # repeticion cada 0.1 segundos
