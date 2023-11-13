# Spanish

En esta clase terminamos la serie de 4: **Primeros pasos con internet con Pico W**
He querido hacer en esta serie los programas que ofrecen una panorámica de lo que se puede hacer, desde lo mas sencillo: un programa que escanee redes wifi, a hacer web servers para controlar HW de la Pico W.

# Contenido CL21

[R] 1- Conexión Pico W modo STA - Web server local - 1ros pasos#4 - 30'

1. [R] Modos de conexión de un uC y capas OSI 

2. [R] Pico W modo STA - servidor TCP/IP con sockets Web botones  para control Led + información cambiante: temperatura Pico-5’

[R] 2- Conexión Pico W modo STA - Web server global con Adafruit IoT - 45

En **1- Pico W modo STA - Web server local** hacemos el [ejemplo de Sunfounder](https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/7.web_page.html) un servidor web en la red local de la red WIFI, que controla el color de un led RGB de 4 pines, y visualiza un sensor NTC. 
<mark>¿ Por qué este montaje?</mark> Porque combina el control de HW conectado a la pico, con mostrar datos de un sensor conectado a la pico. Estos dos opciones cubren todas las posibilidades de un Hw de domótica.
El problema es que no se puede controlar ni visualizar fuera de la red local.



**Solucion: en 2- Pico W modo STA - Web server global con [Adafruit IoT](https://io.adafruit.com/),** con exactamente el mismo HW usaremos un servicio de IoT para hacer exactamente lo mismo, pero con acceso desde cualquier ip de internet.



### Programas:

1- .2 **BMMR_CL21s_webServ_NTC_RGB_2_1.py**

Ejemplo servidor LOCAL web TCP/IP : se conecta en modo STA, y sirve una pagina web con 4 botones que encienden/ apagan en un LED RGB de cátodo común , el led rojo, verde o el azul . Ademas muestra Temperatura de un NTC y el estado de los leds

![image](https://github.com/Jcspoza/CMM_Python_uP_PicoW/assets/28370801/a25037b7-baa8-4bf1-8247-837a9643e36f)


2- **BMMR_CL21s_AfIoT_NTC_RGB_2_0.py**

Ejemplo de servidor web para controlar HW de la Pico W, con acceso global a través de un servicio IoT de Adafruit. Usa mismo HW que 1.2

Los "switch" sirven para cambiar los led. Tienen un cierto "lag"

El grafico circulo para mostrar temperatura de NTC

![image](https://github.com/Jcspoza/CMM_Python_uP_PicoW/assets/28370801/f56a19a9-4d4e-4f2b-888c-b24f461d428a)


### Tutoriales de interes

- Tutorial en castellano, ver el hasta que cuenta el codigo, que es para un neopixel

[Raspberry Pi Pico W con](https://youtu.be/Hee9fIwVGFs?si=nDDjqIZfNCCiUJM4) [Adafruit](https://youtu.be/Hee9fIwVGFs?si=nDDjqIZfNCCiUJM4) [IO control de](https://youtu.be/Hee9fIwVGFs?si=nDDjqIZfNCCiUJM4) [Neopixel](https://youtu.be/Hee9fIwVGFs?si=nDDjqIZfNCCiUJM4) [- Proyecto IOT- Código
en](https://youtu.be/Hee9fIwVGFs?si=nDDjqIZfNCCiUJM4) [MicroPython](https://youtu.be/Hee9fIwVGFs?si=nDDjqIZfNCCiUJM4)



- Tutorial sobre NTC´s

[https://youtu.be/obLccs8dRdg](https://youtu.be/obLccs8dRdg)
