# Spanish

## Intro

En esta clase, vamos a realizar un mini proyecto : Alarma de intrusos con aviso por e-mail.

Aunque vamos a seguir el tutorial de[ Sunfounder](https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/3.ifttt_mail.html)  con ligeros cambios , como solemos hacer, vamos a trabajar "como si" hiciéramos el proyecto desde cero. Desarrollaremos el proyecto en <u>Planteamiento del mProyecto</u>, pero en resumen dividiremso el proyecto en 2 fases:

- SIN conexión

- CON conexión 

# Contenido CL24

[R-mP] Alarma de presencia(PIR) con envio de e-mail  – 90’

1. Planteamiento del mProyecto – 15’

2. [HW] – PIR y hw test PIR con interrupciones -15’

3. Alarma PIR operática Buzer y reset (sin conexion)-20’

4. Enviar un correo con PICO W x IFTTT
   
   1. Opciones de diseño -5’
   
   2. Conocer el servicio IFTTT -10’ (ver IFTTT, Logarse y crear servicio)

5. Unir PIR y envio de webhook -> PICOW – 15’

6. Un paso + : añadir info al correo – 10’



## Alarma SIN conexión

Seleccionamos como sensor de intrusos el PIR, por razones de economía y simplicidad, por lo que toca:

1. Comprender el funcionamiento de este sensor

2. Probar una alarma básica con PIR ==> usaremos interrupciones ==> repasaremos las interrupciones

3. Construiremos un alarma PIR "funcional" => tendrá sonido y un botón de reset

Este HW nos valdrá para el prototipo CON Conexión



| Programa                            | Funcionalidad                                                       |
| ----------------------------------- | ------------------------------------------------------------------- |
| BMMRCL24_pir_irq_bhwt_1_0.py        | Test básico de sensor PIR con Interrupciones                        |
| BMMR_CL24_pir_irq_buzled_but_1_3.py | Prototipo funcional de alarma PIR con sonido , luz y boton de reset |



## Alarma CON conexión

Una vez tenemos el HW definido, solo hay que añadir un efecto mas con el disparo de la alarma => enviar un e-mail.

Hay varias alternativas para, enviar e-mail con uControladores con Wifi, seleccionamso usar el servicio IFTTT por 2 razones:

* Sencillez

* Conocer el servicio IFTTT que nos puede servir en otros proyectos



| Programa                   | Funcionalidad                                                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| BMMR_CL24_pir_ifttt_1_1.py | Prototipo funcional de alarma PIR con sonido , luz y botón de reset + envio de e-mail (simple)                                 |
| BMMR_CL24_pir_ifttt_2_0.py | Prototipo funcional de alarma PIR con sonido , luz y boton de reset + envio de e-mail complejo , indicando el numero de sensor |

---

TO DO : Conocer el programa CURL de windows para probar API´s

---
