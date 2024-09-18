# CL0 - Presentación Taller PyR 2024 y 2025 en CMM Benito Martin Lozano

## Clase 0 - Indice - 90 minutos

- Presentación curso y profesor – 10 minutos

- Enfoque: ¿Por qué Programación y Robotica simultáneamente? – 10 min

- Demos - Primeros pasos (solo profesor) – 30 mins
  
  - Python : “Hola mundo”
  
  - Micropython : ‘Blink’ led

- Presentación alumnos -20 mins
  (Taller personalizado para alumnos según sus intereses y formación previa => puesta en común)

- ¿Qué vamos a necesitar (minimo)?

- Programa del curso 24 - 25

## Tutoriales que vamos a seguir

### Tabla resumen de programas

| Programa                                   | Lenguaje                    | HW si Robotica y Notas                                  | Objetivo de Aprendizaje     |
| ------------------------------------------ | --------------------------- | ------------------------------------------------------- | --------------------------- |
| ‘[Blink’ led](./R_2425CL0_Exblink_v1_2.py) | micropython (uPython, o uP) | GPIO16 -> R220 ohm -> LED1 cátodo  y R220 -> LED2 ánodo | Primer programa de robotica |
| [Hola mundo](./P_2425CL0_hola.py)          | Python                      | Input()no funciona con algunos IDE python on line       | Primer programa de Python   |

### Recomendaciones de estudio despues de la clase

Ejecutar "hola mundo" en un IDE de Python, opciones:

- web como : [https://www.online-python.com/](https://www.online-python.com/)

- O si tienes instalado el IDE [Thonny ](https://thonny.org/)

- u otro IDE mas complejo como Visual Studio Code

**+**

Leer capitulo 2 de libro "Invent with python"" [Chapter 2 - Writing Programs](https://inventwithpython.com/invent4thed/chapter2.html)

---

## Presentación curso y profesor – 10 minutos

Currículo de Voluntario tecnológico del profesor [CV](./doc/CV_JCSP_Voluntario_20240906.pdf)

## Enfoque: ¿Por qué Programación y Robotica simultáneamente? – 10 min

La frontera es difusa, hay diferencias al comienzo del aprendizaje de Programación o
Robotica, que luego cuando se avanza se reducen. Lo ideal sería aprender tanto
Programación como Robótica.

| PROGRAMACION                                                                                                                                                  | ROBÓTICA                                                                                                            |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Mas Abstracto, los programas se ejecutan en un ordenador y no interactúan con el mundo salvo el teclado y la pantalla (hasta que se hacen cosas con internet) | Mos concreto, se pueden hacer "cacharros" como termostatos, estaciones meteorológicas, etc                          |
| Rápidamente se avanza a programas más complejos y más “inteligentes”                                                                                          | Los programas que se cargan en el microcontrolador son relativamente simples, aunque poco a poco se van complicando |
| No se necesita hardware para empezar (microcontrolador y materiales de robótica), salvo un PC o similar                                                       | Se NECESITA hardware para empezar: materiales de robótica y microcontrolador                                        |

<img src="./doc/Python-logo-notext.svg.png" alt="" width="140">

En <u>programación</u>, **Python** es sin duda el lenguaje mas adecuado para aprender (en edad adulta) porque es :

- **Gratis** (al igual que su código fuente y sus bibliotecas).

- **Fácil de aprender y de usar**. Beneficia tanto a los principiantes como a los expertos.

- **Sintaxis legible**.

- **Libre** y de **código abierto** (open source).

- Amplias **bibliotecas**.

- **Creación rápida** de programas: ***es un lenguaje Interpretado***

- **Extensible e integrable** con otros lenguajes

- Funciona en los principales sistemas operativos y plataformas informáticas

Mas razones en los siguientes videos

[Video corto en castellano 1 ](https://www.tiktok.com/@edteam/video/7410916311821323526?is_from_webapp=1&web_id=7343715684931307040)

[Video corto en castellano 2](https://www.tiktok.com/@edteam/video/7410916311821323526?is_from_webapp=1&web_id=7343715684931307040)

[3 Reasons to Learn Python - AI and LLMs is One of Them, but There are MORE!](https://www.youtube.com/watch?v=EHsLuHbE_9s)

En <u>Robotica</u>, hasta hace poco tiempo había que usar para programar los microcontroladores , que son el cerebro de los proyectos de robotica, lenguajes relativamente oscuros como "C" o derivadas de C ( IDE Arduino) . Afortunadamente, en 2013 el físico Australiano Damien George, desarrollo junto a otros personas **micropython** para el microcontrolador PyBoard, y rápidamente se "porto" a otros microcontroladores como ESP32 o RPI Pico.

<img src="./doc/MicroPython_new_logo.jpg" title="" alt="" width="140">

**Micropython** es una implementación del lenguaje de programación Python 3, escrita en C, optimizada para poder ejecutarse en un microcontrolador. Es decir **permite programar los microcontroladores con "programas" escritos en un sub-conjunto de Python con alguna peculiaridad del microcontrolador** por lo que son aplicables todas las ventajas de Python

***En este curso se aprende simultáneamente Python y microPython con lo cual el aprendizaje se realimenta y multiplica***

## Demos - Primeros pasos (solo profesor) – 30 mins

Vamos a ver como demostración los mas clásico que en programación consiste que que un programa te "salude" : 

Python : [Hola mundo](./P_2425CL0_hola.py)

y en robotica es un programa que hace que un led se encienda y se apague. En nuestro caso van a ser 2 leds

Micropython : ‘[Blink’ led](./R_2425CL0_Exblink_v1_2.py)

## Presentación alumnos -20 mins

Es el momento de conocernos un poco, porque este es un taller personalizado para alumnos según sus intereses y formación previa 

--> Hagamos una puesta en común de 20 mins

## ¿Qué vamos a necesitar (minimo)?

<u>**IDE:**</u> Para programar **tanto en Python como en micropython** vamos usar **<u>Thonny</u>** que es un IDE: Entorno integrado de Desarrollo. Es gratis y solo necesitamos instalarlo en un PC o en un pendrive : lo contaremos en la clase 1.

**<u>Microcontrolador</u>**: ya hemso comentado que es como el cerebro de todos los proyectos de robotica, es también donde se conectan todos los sensores, displays, etc. El **año pasado decidimos usar el microcontrolador <u>Raspberry Pi Pico W</u>** 

![](C:\Users\josec\OneDrive\Documentos\03_MAKER\MK_PROJECTS\CMM_MK_2410O_J25\CL0_2525\doc\CMM_BML_Taller_P_R2023_compara_micros.png)

Seguiremos con él el curso 2024 - 2025, porque las razones no han cambiado y el precio es aproximadamente el mismo. Comentaremos este tema en próximas clases

**Novedad:** Recientemente, agosto 2024, ha aparecido una versión muy mejorada de la Raspberry Pico -> [**Raspberry Pi Pico 2**: A Powerful New Addition to the Microcontroller Family | Elektor Magazine](https://www.elektormagazine.com/news/raspberry-pi-pico-2-a-powerful-new-addition-to-the-microcontroller-family)) muy interesante, pero de momento sin wifi asi que nos quedaremos con el Pico W

Lo ideal es comprar un kit, pero se puede empezar solo con el microcontrolador + una protoboard y algunas cosas ( muy baratas) mas.

## Programa del curso 24 - 25

El programa se adaptará a los alumnos como se hizo los dos cursos anteriores. Si hay alumnos nuevos con un nivel inicial, lo que haremos será 

Robotica : dispositivos de entrada que no se ha dado de forma completa

Programación: reforzar conceptos repasando "Invent with Python " y otros libros y guías

---

TO DO :
