# Spanish

En esta clase, vamos por un lado a empezar le estudio de los **Displays,** que se usan en la mayoría de los proyectos "de verdad" dado que, normalmente no tendremso conectada la PICO ni la PICO W al PC por USB, como cuando porbamos los proyecto con Thony: necesitaremos una forma de mostrar información compleja, y sera con displays.

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

En **1- Display OLED I2C**, veremos el primer display gráfico del curso 

Veremos:

- Librería: hay una standard

- Montaje: sencillo usamos I2C, usaremos el I2C1 para poder compatibilizar con LCD

- Pantalla: IMPORTANTE dedicar tiempo a acostumbrarse a como se dispone la maya de coordenadas, porque en el resto de las pantallas graficas, habrá mas colores y mas pixeles, pero la lógica será muy similar

- Comandos de la librería + programa de menú con casi todos los comandos gráficos
  
  - Adicionalmente veremos como hacer un programa con un menú, de forma que se puedan añadir opciones fácilmente
  
  - Veremos también como las funciones se puede tratar como un objeto mas

- Test básicos x3 : conviene tenerlos a mano , por si en algun programa mas complejo el display no funcionara, poder descartar una fuente de error

- Test avanzados x3  : Incluiremos también algun programa de test mas avanzado
  
  Avanzado: Se explicara como transformar una imagen para poder ser vista en el display

- Avanzado: se estudiara la libreria SSD1306 para ver lso conceptos OOP de Herencia y sobrecarga de metodos

- 

- [ ]   **BMMR_bhwt_ssd1306_cmd_graph_3_0.py**

- [ ]  **BMMR_bhwt_ssd1306_all_lines_1_0.py**

- [ ]  **BMMR_bhwt_ssd1306_text_logo_lin_1_5.py**

- [ ]  **BMMR_bhwt_ssd1306_icon_en_matriz_1_0.py**

- [ ]  **BMMR_bhwt_ssd1306_blit_1_0.py**

- [ ]  **BMMR_bhwt_ssd1306_img_en_lista_3_0.py**

- [ ] 
- [ ]  **BMMR_bhwt_ssd1306_img_en_file_2_0.py**

## 2- Potenciómetro, ver lectura grafica en OLED – 55’

En la parte 2, haremos un proyecto donde la idea es usar intensivamente las capacidades gráficas del display. 

Objetivo: **Representar gráficamente un valor analógico en unos ejes de coordenadas standard Y= valor analógico, X=tiempo**. Para el valor analógico elegimos la lectura por uno de los ADC de la PICO, del voltaje del pin intermedio de un potenciómetro cuyos otros 2 pines pines estan a 0 y +3.3 voltios respectivamente, de forma que el voltaje en este pin este en este rango que es el que puede leer el ADC directamente

### 2.1 1.Un ejemplo que funciona con mal codigo

[Encontramos un ejemplo que funciona](https://controlautomaticoeducacion.com/micropython/display-oled-raspberry-pi-pico-esp8266/), pero cuyo codigo es confuso, mal organizado y probablemente una "traducción" de C a Python, es decir poco "*pytonico*". Lo bueno es que fijamos mejor el objetivo:

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

### 2.1.2 Planteamiento y seudocódigo

### 2.1.3 Codigo nuevo y explicación

- [ ] **BMMR_ssd1306_graf_pot_4_1.py**

**SOLUCION** : Con lo aprendido del codigo “mal codificado” , empiezo en base cero a codificar.
Lo más laborioso es la definición de zonas, y revisar los valores frontera de los pixeles,  ver si en al ejecución no "desbordamos" zonas o el propio display, etc. 

Recomiendo usar papel cuadriculado
