# Spanish
## Intro
En esta clase, vamos por un lado a empezar el estudio de los **Displays,** que se usan en la mayoría de los proyectos "de verdad" dado que, normalmente no tendremso conectada la PICO, ni la PICO W al PC por USB, como cuando probamos los proyecto con Thonny -> necesitaremos una forma de mostrar información compleja, y sera con displays. 
El display SSD1306 es el diplay **grafico** más simple de los que normañmente se usan en los proyectos maker. En **1- Display OLED I2C**, veremos el primer display gráfico del curso 

# Contenido CL23

1. [R-HW] Usar Displays #2 OLED I2C 128x64 - 120'
   
   1. Librería y Pros y Contras
   
   2. Montaje Pico ((W) + display SSD1306
   
   3. Pantalla : disposicion de pixels
   
   4. Comandos de la librería + programa de muestra con menu
   
   5. HW Tests x6 : básicos y avanzados
   
   6. 1.Avanzado: Conversión de imágenes – 20’
   
   7. Avanzado: “Tripas” de la librería – OOP /POO - Herencia y Sobrecarga - 20'

2. [R] – Potenciómetro, ver lectura grafica en OLED - 45'
   
   1. Idea y montaje
   
   2. Un ejemplo que funciona, pero con codigo mal escrito
   
   3. SOLUCION: seudocódigo y explicación

## 1- Displays#2 OLED I2C 128X64
Como resumen decir que:
- Librería: hay una standard ==> los tutoriales que encontremos usaran siempre esta libreria
- Montaje: sencillo usamos I2C, usaremos el I2C1 para poder compatibilizar con LCD
- Pantalla: IMPORTANTE dedicar tiempo a acostumbrarse a como se dispone la maya de coordenadas, porque en el resto de las pantallas graficas, habrá mas colores y mas pixeles, pero la lógica será muy similar
- Podemos usar tanto una placa PICO como una PICO W

En la presentacion veremos:

- Comandos de la librería + **programa de menú con casi todos los comandos gráficos**
  
  - Adicionalmente veremos como hacer un programa con un menú, de forma que se puedan añadir opciones fácilmente
  
  - Veremos también como las funciones se puede tratar como un objeto mas

- Test básicos x3 : conviene tenerlos a mano , por si en algun programa mas complejo el display no funcionara, poder descartar una fuente de error

- Test avanzados x3  : Incluiremos también algun programa de test mas avanzado
  
  Avanzado: Se explicara como transformar una imagen para poder ser vista en el display

- Avanzado: se estudiara la librería SSD1306 para ver los conceptos OOP de Herencia y sobrecarga de métodos


- [ ] <u>Programa menú con comandos gráficos</u>

- [ ]  **BMMR_bhwt_ssd1306_cmd_graph_3_0.py**

- [ ] <u> Básicos</u>

- [ ]  **BMMR_bhwt_ssd1306_all_lines_1_0.py**

- [ ]  **BMMR_bhwt_ssd1306_text_logo_lin_1_5.py**

- [ ]  **BMMR_bhwt_ssd1306_icon_en_matriz_1_0.py**

- [ ]  <u>Avanzados</u>

- [ ]  **BMMR_bhwt_ssd1306_blit_1_0.py**

- [ ]  **BMMR_bhwt_ssd1306_img_en_lista_3_0.py**

- [ ]  **BMMR_bhwt_ssd1306_img_en_file_2_0.py**

## 2- Potenciómetro, ver lectura grafica en OLED – 55’

En la parte 2, haremos un proyecto donde la idea es usar intensivamente las capacidades gráficas del display. 

Objetivo: **Representar gráficamente un valor analógico en unos ejes de coordenadas standard Y= valor analógico, X=tiempo**. Para el valor analógico elegimos la lectura por uno de los ADC de la PICO, del voltaje del pin intermedio de un potenciómetro cuyos otros 2 pines pines estan a 0 y +3.3 voltios respectivamente, de forma que el voltaje en este pin este en este rango que es el que puede leer el ADC directamente

### 2.2.Un ejemplo que funciona con un codigo de no mucha calidad
1ro siempre hay que buscar ejemplos similares

[Encontramos un ejemplo que funciona](https://controlautomaticoeducacion.com/micropython/display-oled-raspberry-pi-pico-esp8266/), pero cuyo codigo es confuso, mal organizado y probablemente una "traducción" de C a Python, es decir poco "*pytonico*". Lo bueno es que fijamos mejor el objetivo y sub-objetivos:

- Dejamos la línea 0 para mostrar en texto el voltaje

- Eje Y a al izquierda con los valores máximo y minimo del voltaje : anchura en horizontal 25 pix = 3 char

- Eje X ultima línea horizontal del display = 63

- Grafico dibujo continuo con 2 fases
  
  - hasta llegar al final a al derecha del display
  
  - Scroll horizontal SOLO de la parte grafica del valor de voltaje

**¿ Por qué el codigo es malo?**

Mal comentado

Mezcla codigo de distintos niveles de abstracción

Lo peor, desde mi punto de vista, es que en la funcion **plot_time** hay demasiadas cosas, esta casi todo el programa --> mala estructura

- [ ] **BMMR_ssd1306_graf_pot_malcode_3_0.py.py**

Asi que, vamso a empezar en **base cero** reciclando alguans ideas del codigo anterior

### 2.3.1 Planteamiento y seudocódigo


### 2.3.2 Codigo nuevo y explicación

- [ ] **BMMR_ssd1306_graf_pot_4_1.py**

**SOLUCION** : Con lo aprendido del codigo “mal codificado” , empiezo en base cero a codificar.
Lo más laborioso es la definición de zonas, y revisar los valores frontera de los pixeles,  ver si en al ejecución no "desbordamos" zonas o el propio display, etc. 

Recomiendo:
   1. Usar papel cuadriculado para la definicion de las zonas
   2. Codificacion progresiva, es decir codificar por segmentos => Probar. Por ejemplo:
         1. Parte 1- mostrar los voltios actualizandose en texto en la primera linea
         2. Parte 2- Voltios en texto actualizandose + dibujo ejes ( hacerlo como funcion) VER SI LAS ZONAS ESTAN OK
         3. Parte 3- Voltios en texto actualizandose + dibujo ejes + Dibujo grafico voltios SIN scroll ==> Cambio a bucle 'for'
              Aqui estará la programación de como se dibuja el grafico de los voltios:
                  a) Ver comos e mapea el valor de voltios a coordenadas verticales del display
                  b) Ver como se almacenan las coordenadas
                  b) Ver que se dibuja una linea desde punto anterior, no solo un punto ( queda mejor) 
         4. Parte 4 (programa completo) - parte 3 + Añado 2do bucle para el scroll, necesito funcion de borrado de top, zona izquierda y ejes.

- [ ] **BMMR_ssd1306_graf_pot_parte1.py**
- [ ] **BMMR_ssd1306_graf_pot_parte2.py**
- [ ] **BMMR_ssd1306_graf_pot_parte3.py**

TO DO : scroll con un framebuffer para la zona grafica + scroll solo de ese frambuffer + ‘blit’


