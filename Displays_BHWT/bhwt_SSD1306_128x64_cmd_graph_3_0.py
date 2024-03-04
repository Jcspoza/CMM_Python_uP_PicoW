# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 4 - 21
# Goal : Show graphic commnads I2C oled ssd1306 & framebuffer library
# Add Learning topics : Design a progrma to mange a menu + use functions as objets
# Ref: https://www.coderdojotc.org/micropython/displays/graph/03-basic-drawing/
# Ref 2 : https://www.esploradores.com/oled_ssd1306/
# Ref 3 : https://docs.micropython.org/en/latest/library/framebuf.html
# 1.0 -> 2.0 cambio mensajes menu + limpiar oled si ctrl+C + manejo excepciones
# 2.0 -> 3.0 + figuras

# CONEXIONES
# PICO							DISPLAY
# Pin N		Logic pin			Logic pin
#  8		GND					GND
#  9		GPIO6-SDA1			SDA
# 10		GPIO7-SCL1			SCL
#  5		3.3 volt			VCC

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import array # necesario para coor de poligonos 
from utime import sleep_ms

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "SSD1306 I2c1 SDA pin6, SCL pin7, VCC3.3volt"
p_project = "Graphic commands show - ssd1306 Pico_&W i2c 1 - default pins"
p_version = "3.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0.0 - Constates y varaibles globales
WIDTH =128 
HEIGHT= 64

def show_rect():
    """Display in oled a rectangule 20 x 16"""
    oled.rect(WIDTH//2 - 10, HEIGHT//2 - 8, 20, 16, 1) # x0, y0, size hor, size vert , color
    return "Rectangulo 20x16"

def show_Frect():
    """Display in oled a filled rectangule 20 x 16"""
    oled.fill_rect(WIDTH//2 - 10, HEIGHT//2 - 8, 20, 16, 1) # x0, y0, size hor, size vert , color
    return "Rect Lleno 20x16"

def show_invert():
    """Invert Display """
    oled.fill_rect(WIDTH//2 - 10, HEIGHT//2 - 8, 20, 16, 1) # x0, y0, size hor, size vert , color
    oled.invert(1)
    return "Invierte oled"

def show_normal():
    """Display in normal mode (not inverted)"""
    oled.fill_rect(WIDTH//2 - 10, HEIGHT//2 - 8, 20, 16, 1) # x0, y0, size hor, size vert , color
    oled.invert(0)
    return "Normal oled"
    
def show_circ():
    """Display in oled a circule r= 20"""
    oled.ellipse(WIDTH//2, HEIGHT//2, 20, 20, 1) # x0, y0, radius, color
    return "Circulo r=30"

def show_ellipse():
    """Display in oled an ellipse rx= 40, ry=20"""
    oled.ellipse(WIDTH//2, HEIGHT//2, 40, 20, 1) # x0, y0, radius X, radius Y, color
    return "Ellipse (40,20)"

def show_QFellipse():
    """Display in oled a 1/4 ellipse rx= 40, ry=20"""
    oled.ellipse(WIDTH//2, HEIGHT//2, 40, 20, 1, True, 10) # x0, y0, radius X, radius Y, color, filled
    # last param is quarter ellipse indicator 1bit last 4
    # 0001 top right
    # 0010 top left
    # 0100 bottom left
    # 1000 bottom right
    return "Ellip 2q (40,20)"

def show_triangle():
    """Display in oled a triangle """
    cor = array.array('h',[60, 0, 30, 40, 90, 40])
    oled.poly(0, 10, cor, 1) 
    return "Triangle (63,10)"

def show_pentagono():
    """Display in oled a pentagono """
    cor = array.array('h',[60, 0, 15, 20, 30, 40, 90, 40, 105, 20])
    oled.poly(0, 10, cor, 1) # x0, y0, coor[x0,y0, x1,y1, x2, y2...], color
    return "Pentagon (63,10)"

      
def show_options():
    """Display Options for drawing in display """
    print('\nTeclas:')
    print('R o r, para Rectangulo')
    print('C o c, para Circulo')
    print('E o e, para Elipse')
    print('T o t, para Triangulo')
    print('P o p, para Pentagono Iregular')
    print('F o f, para Rectangulo relleno')
    print('Q o q, para 2/4 de Elipse rellena')
    print('I o i, invierte display (repetir)')
    print('N o n, display NO invertido')
    print('?    Muestra opciones de nuevo\n')
    oled.text("Menu en teclado",0,0,1)
    return "Menu en PC"
    
MENU = {"R": show_rect,
        "C": show_circ,
        "E": show_ellipse,
        "T": show_triangle,
        "P": show_pentagono,
        "F": show_Frect,
        "Q": show_QFellipse,
        "I": show_invert,
        "N": show_normal,
        "?": show_options
        }


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
oled.text("de", (WIDTH - len("de")*8) // 2, 16)
oled.text("Comand Graficos", (WIDTH - len("Comand Graficos")*8) // 2, 32)
oled.text("version " + p_version, 0, 48)
oled.show()
sleep_ms(3000)
oled.fill(0)
oled.show()

# 2- try - except para salir con cntr+C
try:  
    while True: # 3- Bucle principal
        oled.fill(0)
        oled.show()
        show_options() # 3.1 - limpia pantalla -> Muestra menu + input opcion menu
        oled.show()
        k = input('Opcion del menu ').upper()[0]
        try:
            orden = MENU[k] # 3.2 Ejecuta la opcion de menu, las funciones son objetos en Python
            msgL8 = orden()
            oled.text(msgL8, (WIDTH - len(msgL8)*8) // 2, 55, 1)
            oled.show()
            sleep_ms(5000)
            
        except KeyError: # 3.3 Gestiona error de opcion de menu
            print("Opcion de menu NO Valida, prueba de nuevo")
            oled.text("Opcion NO valida", 0, 55, 1)
            oled.show()
            sleep_ms(5000)
        
except KeyboardInterrupt: #  4- si CTRL+C se presiona - > limpiar display
    oled.fill(0)
    oled.show()

