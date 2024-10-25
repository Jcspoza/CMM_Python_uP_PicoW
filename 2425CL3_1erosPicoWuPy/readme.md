# CL3 - Pico y Pico W primeros pasos - PyR 2024_25 CMM BML

## Clase 3 - Indice - 90 minutos

- Consideraciones Generales sobre el Tutorial de Raspbery Pi Foundation 
  
  - [Getting started with Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)

- Hacer el tutorial paso a paso - 60 minutos
  
  - Led Interno
  
  - Led externo con pulsador / interruptor
  
  - Led externo con intensidad pulsante
  
  - Led controlado con potenciómetro
  
  - Como ejecutar programas 'dentro' de  Pico y Pico W sin conexión a PC

- Conceptos cubiertos en este capitulo

- Preguntas sobre la Clase 1 - 10 minutos

## Tutoriales y Programas que vamos a seguir

### Tutoriales resumen

[Getting started with Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)

### Tabla resumen de programas

| Programa                           | Leng. | HW si Robotica y/o Notas          | Objetivo de Aprendizaje                                                                |
| ---------------------------------- | ----- | --------------------------------- | -------------------------------------------------------------------------------------- |
| [R_2425CL3_blinkNude.py](R_2425CL3_blinkNude.py)            | uPy   |                                   | 1er programa uP                                                                        |
| [R_2425CL3_blinkSimple_v1_0.py](R_2425CL3_blinkSimple_v1_0.py)      | uPy   |                                   | igual que blinkNude pero copn comentario sy bloque informativo                         |
| [R_2425CL3_blinkTry_v1_0.py](R_2425CL3_blinkTry_v1_0.py)         | uPy   |                                   | Incluye Try-Except para manejar la excepción de interrupción de teclado                |
| [R_2425CL3_blinkTimer_v1_0.py](R_2425CL3_blinkTimer_v1_0.py)      | uPy   |                                   | Usa un timer para cambiar el estado del led y asi el programa puede hacer otras cosas  |
| [R_2425CL3_blinkTimer_v2_0.py](R_2425CL3_blinkTimer_v2_0.py)       | uPy   |                                   | Añadimos un asalida con Try-Except + hacemos otras cosas mientras esta activo el timer |
| [R_2425CL3_blinkExled_v1_2.py](R_2425CL3_blinkExled_v1_2.py)       |       | in GPIO16 -> R220ohm -> LED anodo |                                                                                        |
| [R_2425CL3_blinkExledTimer_v1_0.py](R_2425CL3_blinkExledTimer_v1_0.py) |       |                                   |                                                                                        |
| [R_2425CL3_ExtLedPWMupdown_v1_0.py](R_2425CL3_ExtLedPWMupdown_v1_0.py)  |       |                                   |                                                                                        |
| [R_2425CL3_ADCSimple_v1_0.py](R_2425CL3_ADCSimple_v1_0.py)        |       |                                   |                                                                                        |
| [R_2425CL3_ExtLedPWMadcpot_v1_0.py](R_2425CL3_ExtLedPWMadcpot_v1_0.py)  |       |                                   |                                                                                        |

### Recomendaciones de estudio despues de la clase

Nada

---

## Consideraciones generales sobre el tutorial Getting .. Pico– 10 minutos

1- La mejor forma de **empezar con los microcontroladores Pico** es realizar completo el tutorial 

[Getting started with Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)

y si es posible, aprovechar cada paso para:

- Ver distintas alternativas de los programas

- ver tensiones, formas de onda

- Alternativas de alimentación

- ... 

2- El tutorial es **valido tanto para Pico como Pico W**

A parte de la diferencia obvia de disponer o no de Wifi, se puede decir de forma general que un **programa hecho para Pico debería ejecutarse sin problemas en un Pico W**

La similitud mas notoria entre Pico y Pico W, es que los **pines externos son idénticos**, con idénticas funciones. Para profundizar mira 

[Raspberry Pi Pico W vs. Pico | What's the difference?](https://core-electronics.com.au/guides/raspberry-pi-pico-w-vs-pico-whats-the-difference/)

Entrando en detalles, la diferencia está en que en el Pico W  los **pines intern**os numerados como **23, 24, 25 y 29** se usan para la interfaz con el modulo WIFI, por lo que si se usan en un programa, funcionara en Pico y no en Pico W

<u>Diagrama de pines de Pico</u>

![pico-pinout.svg](./doc/pico-pinout.svg)

<u>Diagrama de pines de Pico W</u>

![picow-pinout.svg](./doc/picow-pinout.svg)

3- ¿ Por que en este curso **se ha decidido programar los Pico/ Pico W con micropython**? 

Los lenguajes con los que se puede programar un microcontrolador son 3 principalmente, y los Pico no son una excepcion:

- Arduino IDE 

- C/C++

- Micropython o CircuitPython

<u>Micropython Pros:</u>

- Simplicidad y legibilidad

- Rapidez en la creación de de los prototipos

- Amplia documentación, tutoriales y foros de consulta

- Beneficio mutuo de aprender Python

- Portable de un microcontrolador a otro con pocos cambios

<u>Micropython Contras</u>

- Es lento respecto a Arduino y C, pero razonablemente rápido para la mayoría de los proyectos caseros

4- **¿Por que Thonny?**

En la revisión algo antigua 

[Eligiendo un IDE para programar | profe Tolocka](https://www.profetolocka.com.ar/2021/01/05/micropython-eligiendo-un-ide-para-programar/)

se revisan alternativas a Thonny y se opina que es la mejor alternativa para micropython

## Hacer el tutorial -1- Carga de FW de micropython

Lo mas sencillo es hacerlo con Thonny => **HACER**

Explicar como es hacerlo SIN Thonny

## 2- Blink led interno

### 2.1 Blink Nude

El programa **'blink" = hacer parpadear un led incluido en la tarjeta del microcontrolado**r, es un programa con el que se empieza a programar los microcontroladores desde Arduino UNO

Es un programa muy sencillo que lo único que hace es que uno de sus pines tenga alternativamente el valor de +3,3 voltios o el de 0 voltios, que corresponden a los valores lógicos '1' y '0'. Estos pines se suelen llamar en los uC , GPIO : pines digitales de propósito general de entrada y salida.

Diagrama de pines Pico y Pico W

Como se ve el LED INCLUIDO esta conectado a distintos pines en Pico y PicoW. Solucion : usar en nuestro porgrama la palabra "LED" que se traducirá por el interprete uP de diferente forma. 

==> Ejecutar en el interprete 

`machine.Pin("LED", machine.Pin.OUT)`

y veras que lo que imprime es diferente

Blink Nude ==> HACER

<u>Diagrama de pines de Pico

### 2.2. Blink Simple con Comentarios y Bloque informativo

Comentar bloque de comentarios y bloque informativo ==> COMENTAR

### 2.2 Blink con Try-Excep

Manejo de errores y excepciones en Python ==> COMENTAR

Blink con Try-Excep == > HACER

### 2.3 Blink con Timer

Hacer que una tarea se ejecute periódicamente ==> COMENTAR

Blink con Timer v 1.0 == > HACER

#### Mejoremos el programa blink con Timer en v 2.0

1. Añadamos Try-Except para manejar excepción de teclado

2. Veamos como el programa principal puede hacer cosas mientras el timer esta ejecutándose

3. Cuando salgo por excepción de teclado ponemos el led a off y cancelamos el timer

### 2.4 Como ejecutar programas 'dentro' de Pico y Pico W sin conexión a PC

1. Copiar dentro de la Pico / Pico w un programa blink como 'main.py' 

2. Desconectar del PC

3. ALIMENTAR la Pico o Pico W, 
   
   hay 2 formas que son las mas sencillas de alimentar una Pico:
   
   * con un powerbank al USB / alimentador USB al micro-USB de la pico
   
   * Con baterías o pilas de entre 1.8 a 5.5 volt a los pines
     
     * VSYS : positivo de alimentación
     
     * GND : negativo de alimentación
       
       ¡CUIDADO, alimentar simultáneamente por USB y VSYS salvo que se use un diodo o similar!
   
   ==> HACER

## 3- Blink led Externo

¿Por qué una resistencia? ==> COMENTAR

[Ver las 2 transparencias sobre circuitos led](./CircuitosLed.pdf)

- Voltaje en directo de Led

- Intensidad en directo de Led

- Circuito Rled + Led 

- Distintos Vf según los leds

Conexiones ==> HACER

Cambios en blink interno ==> HACER

## 4- Led Externo Variando de intensidad

### 4.1 PWM

Como hacer que una salida digital varíe de intensidad eficaz  ==> MULTIMETRO + OSCILOSCOPIO

### 4.2 Led Externo Variando de intensidad Arriba y Abajo

==> HACER

### 4.3 ADC

#### 4.3.1 DAC y ADC un poco de teoría

#### 4.3.2 Leer los ADC de la Pico

==> HACER

### 4.4 Led Externo Variando de intensidad con Potenciómetro

==> HACER

## Conceptos cubiertos en este clase - 5'

En esta clase hemos cubierto los siguientes conceptos: 

- Conocer un poco los Pico

- Crear y ejecutar programas sencillos

- Bucles infinitos while True

- Documentación de programas

- Try-Except - Básico

- Timer - Básico

- Alimentación Pico/ Pico W

## Preguntas sobre la Clase 3 - 10 minutos

Sección para que los alumnos pregunten sus dudas durante la clase

---

TO DO : 

* Led externo con pulsador / interruptor

* R_2425CL3_blinkPIO_v1_0.py

* R_2425CL3_blinkPIO_v2_0.py
