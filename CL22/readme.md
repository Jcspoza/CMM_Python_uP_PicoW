# Spanish

En esta clase, vamos por un lado a empezar le estudio de los **Displays,** que se usan en la mayoría de los proyectos "de verdad" dado que no estaremos conectados al PC por USB, y necesitaremos una forma de mostrar información. Por otro lado, vamos a resolver un problema importante que dejamos pendiente en la clase 12, **sincronizar la Pico W** y así poder marcar lecturas de sensores o de eventos con marcas de tiempo ("timestamps") fiables

# Contenido CL22

1. [R-HW] Usar Displays #1 – 35’
   
   1. Presentación serie Displays
   
   2. -> solo texto: LCD I2C 20x4

2. [R] – Sincronización reloj PICO W con NTP – 55’
   
   1. Recordar problema CL12 temperatura con “timestamp”
   
   2. Añadir LCD a temperatura con “timestamp”
   
   3. RTC interno ¿qué es? y porque esta desincronizado
   
   4. NTP: Sincronización del RTC interno con NTC -> Reloj LCD
   
   5. Solución de sincronización #1 : Boot_wifi_sincro

## 1- Display LCD I2C

En **1- Display LCD I2C**, empezaremos una serie de programas de control básico de Displays. Veremos 

1. LCD 16x2 o 20x4 i2C : solo caracteres
2. SSD1306 I2C - Graphic : 0.96”  128 x64 1 color
3. TFT ST7735r SPI Graphic:  1.8” 128x160 RGB 64K
4. TFT SPI- ST7789VW Graphic: 1.14” 240 × 135, RGB 64K
5. TFT SPI ILI9341  Graphic: 2.8” or 3.2"· 320 x 240, RGB 64K + touch screen XPT2046 + SD card

Empezaremos con el display #1 - LCD 16x2 o 20x4 i2C : solo caracteres o Character LCD, que ya estamos usando de facto. Veremos:

- Librería: no hay una standard en este caso

- Montaje

- Comandos de la librería

- 2 ejemplos de test básicos : conviene tenerlos a mano , por si en algun programa mas complejo el display no funcionara, poder descartar una fuente de error

- [ ]     **BMMR_bhwt_lcd20x4_I2C.py** 

- [ ]     **BMMR_bhwt_lcd20x4_I2C_v2.py**

![image](https://github.com/Jcspoza/CMM_Python_uP_PicoW/assets/28370801/a8f9912c-ecb3-49a2-8d28-0b5a6629bda6)

![image](https://github.com/Jcspoza/CMM_Python_uP_PicoW/assets/28370801/14af6816-78e3-4cc6-95e0-f9430b4d15db)


Hay otros HW´s no vamos a ver y que que también se pueden considerar displays:

- 7 Segment Display

- 10 Bar LEDs

- 8x8 LED Matrix

- 4 Digit LED
  
  ver [tutoriales de MicroPython for Kids](https://www.coderdojotc.org/micropython/displays/non-graph/01-intro/) si se necesita



## 2- Sincronización reloj PICO W con NTP – 55’

En la parte 2, Sincronización reloj PICO W con NTP, vamos primero a recordar el problema de la sincronización que vimos en CL12: la Pico y Pico W tiene un módulo interno de reloj **RTC**, pero 

1. Hay que inicializarlo, porque de otro modo se inicializa a 1-1-2021

2. No tiene alimentación independiente

Thony, el IDE que usamos, tiene un efecto *oculto* de sincronizar la Pico al conectarla. pero en usos reales **aislados** tenemos que sincronizarla de alguna forma.

- [ ] **BMMR_CL22_ADC_temp_file3_0.py**



En 2.2 modificaremos el programa para que muestre info en el display LCD

- [ ] **BMMR_CL22_ADC_temp_LCD_file_4_0.py**

Ahora podemos ver el caso de alimentar le circuito con una power bank (el display LCD necesita 5volt). El tiempo se inicia a 2021-1-1



#### Servicio NTP

Veremos como se puede usar un reloj especial de internet para sincronizar la Pico W : servicio NTP, con un ejemplo de reloj con el display 20x4

- [ ] **BMMR_CL22_lcd20x4_clock_4_0.py**



#### Solución de sincronización con Boot

La solución será añadir un fichero "boot.py" que se ejecuta antes de main.py.

Tomaremos do_connect version 1.9 para añadirle sincronización por NTP del RTC de la Pico W. Una vez hecho desconectaremos del route y deshabilitaremos el circuito wifi para ahorrar energía.

- [ ] **BMMR_CL22_boot_sincro_1_0.py**
