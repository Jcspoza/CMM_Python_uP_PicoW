# Spanish

En esta clase terminamos la serie de 4: **Primeros pasos con internet con Pico W**
He querido hacer en esta serie los programas que ofrecen una panorámica de lo que se puede hacer, desde lo mas sencillo: un programa que escanee redes wifi, a hacer web servers para controlar HW de la Pico W.

# Contenido CL21

1. [R] Conexión Pico W modo STA - Web server local - 1ros pasos#4 - 30'
   
   1. [R] Modos de conexión de un uC y capas OSI 
   
   2. [R] Pico W modo STA - servidor TCP/IP con sockets Web botones  para control Led + información cambiante: temperatura Pico-5’

2. [R] Conexión Pico W modo STA - Web server global con Adafruit IoT - 45'

3. [R] Usar Displays #1 -> solo texto: LCD I2C ( si da tiempo) 

En **1- Pico W modo STA - Web server local** hacemos el [ejemplo de Sunfounder](https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/7.web_page.html) un servidor web en la red local de la red WIFI, que controla el color de un led RGB de 4 pines, y visualiza un sensor NTC. 
<mark>¿ Por qué este montaje?</mark> Porque combina el control de HW conectado a la pico, con mostrar datos de un sensor conectado a la pico. Estos dos opciones cubren todas las posibilidades de un Hw de domótica.
El problema es que no se puede controlar ni visualizar fuera de la red local.

**Solucion: en 2- Pico W modo STA - Web server global con Adafruit IoT,** con exactamente el mismo HW usaremos un servicio de IoT para hacer exactamente lo mismo, pero con acceso desde cualquier ip de internet.

En **3- Display LCD I2C**, <mark>si da tiempo</mark> empezaremos una serie de programas de control básico de Displays. Empezaremos con el display de LCD por I2C o Character LCD, que ya estamos usando de facto.
Hay otros HW´s que también se pueden considerar displays:

- 7 Segment Display

- 10 Bar LEDs

- 8x8 LED Matrix

- 4 Digit LED
  
  ver [tutoriales de MicroPython for Kids](https://www.coderdojotc.org/micropython/displays/non-graph/01-intro/) si se necesita
