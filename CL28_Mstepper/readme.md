# Spanish (wip)

## Objetivo

En esta clase, vamos a estudiar los **motores Paso a Paso o Steeper.**

**Teoría :** Dado que hay muchísimos tutoriales sobre el tema, no vamos a desarrollar mucho la teoría solo consultar 1 o 2 tutoriales.

**Programas:** <u>Se construirá un programa básico con todas las opciones de tipos de pasos</u> ( ver mas adelante), pero no se hará un programa complejo, ni se construirá una libreria, dejando esto a los alumnos

## <u>Teoría de Motores Paso a Paso </u>

### Para entender el HW del motor

[Motores paso a paso &#8211; Prometec](https://www.prometec.net/motores-paso-a-paso/)

Resumen : Un **motor paso a paso** es parecido a los motores de continua, pero en lugar de montar un sistema de asegurarnos de que siempre hay una bobina fuera del equilibrio, en un **motor paso a paso** montamos un sistema de varias bobinas que garantizan que solo se mueve la distancia (O paso) entre las bobinas contiguas.

![](./doc\gira.gif)

[In-Depth: Control 28BYJ-48 Stepper Motor with ULN2003 Driver &amp; Arduino](https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/?utm_content=cmp-true)

Es un tutorial excelente, con explicaciones detalladas de como funciona tanto el motor como el controlador

#### Entendiendo el numero de pasos por giro

**ATENCION**: **la figura de las 4 fases que completan el circulo ( 360º) NO es correcta** y lleva a confusión, cuando se pretende entender el numero de pasos de 1 giro completo. Leyendo con calma el tutorial, indica que 

*'when the 28BYJ-48 motor is operated in full-step mode, each step corresponds to a rotation of 11.25°. This means there are 32 steps per revolution (360°/11.25° = 32).'*

Es decir, **en full-step** significa energizar cada una de las 4 x fases 1 vez cada paso, luego un giro es ejecutar la secuencia de 4 paso  x 8 veces = **32 pasos de 11.25º**

**En modo Half-step** se recorren las 4 fases en 8 pasos, luego un giro corresponde a 8 x 8  = **64 pasos = > 5.625º**

**ADEMAS, hay una reductora 1/64**, por lo que en 

Full-Step = 32 * 64 = 2048 pasos por giro , o 0,18º por paso

Half-step = 64 * 64 = 4096 pasos por giro , o 0,09º por paso

![lll](./doc/28BYJ48-Stepper-Motor-Gear-Ratio-Explanation.webp)

### 

### Controladora ULN2003

El motor requiere un consumo elevado 240 mA, por lo que necesitamos un "driver" que proporcione los mA requeridos . El ULN2003a proporciona 500mA por salida con un voltaje máximo de 50volt.

ULN2003  empaqueta 7 pares de transistores en montaje Darlington

![](C:\Users\josec\OneDrive\Documentos\03_MAKER\MK_PROJECTS\CMM_MK_O23_J24\limpios_hechos\CL28_SteppM\doc\uln2003_internal.png)

Lo que se suele vender como driver ULN2003, añade algo de circuitería y simplifica las conexiones. Supuestamente  los 4 leds facilitan el aprendizaje de los pasos, pero dado que la secuencia corre a mucha velocidad, sirven de poco. Se puede usar el integrado ULN2003 directamente pinchándolo en la protoboard.

![](C:\Users\josec\OneDrive\Documentos\03_MAKER\MK_PROJECTS\CMM_MK_O23_J24\limpios_hechos\CL28_SteppM\doc\ULN2003schematic.jpg)

### Para ver un programa en uP

## <u>Practica de aprendizaje con motores PaP</u>

### Tabla resumen de programas

| Programa                   | HW                                            | Funcionalidad                                                                                                                          |
| -------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| pico_stepM_simple.py       | ULN2003   IN1-GPIO10 ...           IN4-GPIO13 |                                                                                                                                        |
| pico_steeper_simple_2_0.py |                                               | Primeras pruebas de funcionalidad con los 3 tipos de stepping + los giros en dirección contraria / Parámetro critico Delay entre pasos |
|                            |                                               |                                                                                                                                        |

### Alimentación y Consumo

Estos motores tienen un consumo relativamente elevado: **Típico =  240mA**

### Libreria/s

No vamos a usar libreria.

### Conexionado usado en los Test

| pin # PICO | Pin Logico en PICO | ULN2003           |
| ---------- | ------------------ | ----------------- |
| 40         | VBUS o +5volt      | (5--12volt) pin + |
| 13         | GND                | (5--12volt) pin - |
| 14         | GPIO10             | IN1               |
| 15         | GPIO11             | IN2               |
| 16         | GPIO12             | IN3               |
| 17         | GPIO13             | IN4               |

### Tutoriales en micropython

[Interface 28BYJ-48 Stepper Motor with ESP32 using MicroPython](https://microcontrollerslab.com/28byj-48-stepper-motor-esp32-micropython/)

[▷ Motores Paso a Paso (PaP) MicroPython- [Raspberry Pi Pico/ESP]](https://controlautomaticoeducacion.com/micropython/motores-paso-a-paso-pap/)

En todos los tutoriales la idea es usar 4 pines digitales activándolos o desactivándolos en la secuencia adecuada

### Programa 1 - pico_stepM_simple.py

Seria el **test mas básico** de estos motores. **Usamos una secuencia de medio-paso**, porque es mas facil que funcione (¡creedme!) : el parámetro 'delay entre pasos' es menso critico, y también la alimentación puede ser también mas baja, que en otros modos.

La secuencia de medio paso la definimos de golpe en una lista

```
half_step_sequence = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1],
    ]
```

otra opción mas compleja seria ir generando esta secuencia a medida que recorremos un bucle. Esta es mas sencilla y rápida.

### Programa 2 - pico_stepM_in_mode_del_2_0.py

Vamos a ver como funcionan todos los modos posibles Clockwise y Counter Clock Wise, con diferentes parámetros de Delay.

| Mode    | Tipo modo      | min Delay           |
| ------- | -------------- | ------------------- |
| FULL1S  |                | 500                 |
| FULL1Sr |                |                     |
| FULL2S  |                |                     |
| FULL2Sr |                |                     |
| HALF    | Medio paso CW  | 180 micro segundos  |
| HALFr   | Medio paso CCW | 180  micro segundos |

### Programa 3 - pico_stepM_1giro_1_0.py

Vamos a ver cuantos pasos corresponden a un giro de 360º 

---

TO DO : 
