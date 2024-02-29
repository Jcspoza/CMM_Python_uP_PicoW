# DISPLAYS BASIC HW TEST (Spanish)

## Objetivo

Se trata de compilar en este tutorial, todos los test hw básicos de los displays más habituales:

- LCD 16x2 y 20x4 - I2C: solo texto

- SSD1306 128 x 64- I2C : Grafico , monocromo

- ST7789 240 x 320 - SPI : Grafico 64k colores

- ILI9341 240 x 320 - SPI: Grafico 2.8”/3.2· 320 x 240, RGB 64K + touch screen XPT2046 + SD card

## Tabla resumen de programas

| Programa | Funcionalidad |
| -------- | ------------- |
|          |               |
|          |               |
|          |               |

## LCD 16x2 y 20x4 - I2C: solo texto

### Alimentación

Estos dos displays se deben alimentar a 5volt, por lo que :

1. la tarjeta pico esta conectada al ordenador por USB, 

2. o se alimenta por un powerbank o 

3. Se alimenta la PICO por VSYS a 5volt

### Libreria/s

No hay una librería standard en micropython, por lo que se investigaron 3 opciones 

1. T622 -> Test ok tiene 3 años ==> OK con Pico 

2. Brainelectronics : 3 meses muchas funciones y custom char —> MAL algunas funnciones

3. Sunfounder : pocas funciones

Selecciono la librería del usuario T62 : [GitHub - T-622/RPI-PICO-I2C-LCD: ](https://github.com/T-622/RPI-PICO-I2C-LCD)

Va Ok a 400.000Hz, tiene función de crear emojis x8. **Se usan dos librerías combinadas en jerarquía**, re-definiendo la capa superior algunas funciones como ***hal_write_command***

### Conexionado usado en los Test

| pin # PICO | Pin Logico en PICO | Display |
|:----------:|:------------------:|:-------:|
| 40         | VSYS               | VCC     |
| 8          | GND                | GND     |
| 6          | I2C0 SDA           | SDA     |
| 7          | I2C0 SCL           | SCL     |

### Dirección I2C

Los displays LCD suelen tener una de dos direcciones 3E o 3F. El programa de test incluye un *scan* del bus I2C que muestra las direcciones I2C encontradas

### Test1 - LCD 20x4 - I2C

0- Crea los objetos I2C y luego el display lcd

1- Llenar display con todo el juego de caracteres los caracteres

2- Llenar display con mensaje de prueba

- Incluye un carácter creado por bit

- Muestra el día y la hora

---

## SSD1306 128 x 64- I2C

### Libreria para SSD1306

### Conexionado para SSD1306 usado en los Test

### Test1 - SSD1306 -

---

## ST7789 240 x 320 - SPI : Grafico 64k colores

### Librería Russ Hughes en C ( y alternativas)

Elegimos esta libreria por potencia, documentación y porque vale para los display ST7735, ST7789 e ILI9341

Referencia :

Es un l ibreria compilada con la fuente de micropython

#### Librería Russ Hughes- tft_config

Guardaremos las configuraciones de conexión y otros parámetros en "tft_config.py", asi nos valdrán los mismos programas con cambios muy pequeños. 

#### 

#### Librería Russ Hughes- HW Test básicos

| Programa                                                                                                            | Funcionalidad                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| bhwt_ili9341FW_B_colorR1_1_0.py_1_0.py                                                                              | **Colores de letra y Fondo** Muestra combinaciones de color de letra y fondo de texto |
| Rotación 1 = apaisado – pines derecha                                                                               |                                                                                       |
| bhwt_ili9341FW_McenterR1_1_0.py                                                                                     | **Texto en centro Display & caracteres castellano**                                   |
| Muestra un texto centrado en el display + uso de caracteres con acento y “ñ” (no UTF-8)                             |                                                                                       |
| Rotación 1 = apaisado – pines derecha                                                                               |                                                                                       |
| bhwt_ili9341FW_fill_irisR1_1_0.py                                                                                   | **Color de Fondo Arcoiris**                                                           |
| El color de fondo del display cambia recorriendo el arco iris (255 pasos). Usa función de cambio de RGB888 a RGB565 |                                                                                       |
| Rotación 1 = apaisado – pines derecha                                                                               |                                                                                       |
| bhwt_ili9341FW_4fontsR2_1_0.py                                                                                      | **Todos char de 4 fuentes**                                                           |
| Muestra cada uno de los caracteres de 4 fuentes de 127 char (no char castellano)                                    |                                                                                       |
| Rotación 2 = Retrato – pines arriba                                                                                 |                                                                                       |
| bhwt_ili9341FW_lineasHyVR2_1_0.py                                                                                   | **Cuadricula de lineas**                                                              |
| Muestra líneas horizontales y luego verticales, con separación de 10 pixeles                                        |                                                                                       |
| Rotación 2 = Retrato – pines arriba                                                                                 |                                                                                       |
| bhwt_ili9341_pacmanR2_2_0.py                                                                                        | **(AVD) Demo de sprites**                                                             |
| Ejemplo de cómo manejar sprites, definiéndolos con bitarray - Avanzado                                              |                                                                                       |
| Rotación 2 = Retrato – pines arriba                                                                                 |                                                                                       |
