# Spanish
En esta clase terminamos la serie de 4 clases, de primeros pasos con internet con Pico W
He querido hacer en esta serie los progrmas que ofrecen una panoramica de lo que se puede hacer de lo mas sencillo: un progrma que escanee redes wifi a hacer web servers

# Contenido CL21

[R] 1- Conexión Pico W modo STA - Web server local - 1ros pasos#4
[R] Modos de conexión de un uC y capas OSI - 5’
[R] Pico W modo STA - servidor TCP/IP con sockets
Web botones  para control Led + información cambiante: temperatura Pico-5’
[R] 2- Conexión Pico W modo STA - Web server global con Adafruit IoT 
[R] 3- Usar Displays #1 -> solo texto: LCD I2C ( si da tiempo) 

En 1- Pico W modo STA - Web server loca hacemso el ejemplo de Sunfounder un servidor web en la red local de la red WIFI, que controla el color de un led RGB de 4 pines, y visualiza un sensor NTC. 
¿ Por que este montaje? Porque combina el control de HW conectado a la pico, con mostrar datos de un sensor conectado a la pico. Estos dos opciones cubren todas las posibilidades de un Hw de domótica.
El problema es que no se puede controlar ni visualizar fuera de la red local.

Solucion: en 2- Pico W modo STA - Web server global con Adafruit IoT, con exactamente el mismo HW usaremos un servicio de IoT para hacer exactamente lo mismo, pero con acceso desde cualquier ip de internet.

En 3- si da tiempo empezaremso una serie de progrmas de control basico de Displays. Empezaremos con el dispaly de LCD por I2C, que ya estamos usando de facto.
Hay otros HW´s que tambien se p ueden considerar displays , ver tutoriales de Sunfounder si se necesita
