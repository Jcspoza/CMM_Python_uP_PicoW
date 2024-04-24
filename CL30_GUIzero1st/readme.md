# Primeros pasos con GUI Zero

## Objetivo

En esta clase, vamos a estudiar como '**Crear GUI´s con guizero'**, que forma parte de un proyecto macro de visualización de API´s.

Recuerdo que ya vimos en la CL29:

- <u>Aprender a trabajar con JSON en Python</u>

- <u>Explotar los datos open source por medio de API´s</u> del Ayuntamiento de Madrid y/ o AEMT - primeros pasos

Quedaría por decidir si hacemos el proyecto en micropython + display tipi ILI9341 o en una raspberry pi en python con guizero

### Libro que vamos a seguir y documentacion

'***Create Graphical User Interfaces with Python***' by Laura Sach & Martin O’Hanlon
How to build windows, buttons, and widgets for your Python projects

[El libro esta disponible para descargar desde el repositorio de la revista  Magic Pi ](https://magpi.raspberrypi.com/books/create-guis). Por comodidad también se puede descargar en este repositorio

**Los programas estan disponibles** en el repositorio de github

[GitHub - themagpimag/createguis](https://github.com/themagpimag/createguis)

Una **extensa documentación sobre el uso de GUIzero** esta disponible en este repositorio creado con Mkdocs

[guizero](https://lawsie.github.io/guizero/)

### Tabla resumen de programas

| Programa                                                         | Widget                          | Capitulo del libro | Objetivo de Aprendizaje                                                                                                                |
| ---------------------------------------------------------------- | ------------------------------- |:------------------:| -------------------------------------------------------------------------------------------------------------------------------------- |
| [BMMP_CL30_GZch1hola_1_0.py](BMMP_CL30_GZch1hola_1_0.py)         | App                             | ch1                | primeros paso - crear una ventana                                                                                                      |
| BMMP_CL30_GZch2wanted_1_0.py                                     | Text, Picture                   | ch2                | Reproduce un cartel típico de 'se busca'                                                                                               |
| BMMP_CL30_GZch3spy_1_0.py                                        | PushButton                      | ch3                | Genera nombres de espía al pulsar un botón en la ventana                                                                               |
| BMMP_CL30_GZch4meme_1_0.py                                       | TextBox, Drawing, Combo, Slider | ch4                | Crea dibujos de memes con texto a escribir por el usuario , arriba y abajo , asi como elegir entre diferentes colores y tipos de letra |
|                                                                  | me´todo .repeat(..)             | ch5                | Solo ejemplos de lo que No se debe hacer                                                                                               |
| [BMMP_CL30_GZch6_3nr_1_0.py](BMMP_CL30_GZch6_3nr_1_0.py)         | Box                             | ch6                | Crea un panel para jugar a 3 en Raya, no tiene inteligencia de juego salvo detectar ganador                                            |
| [BMMP_CL30_GZch7_mataPun_1_0.py](BMMP_CL30_GZch7_mataPun_1_0.py) | Waffle                          | ch7                |                                                                                                                                        |

### Recomendaciones de estudio

El libro es excelente y auto explicativo, con lo que habría poco que explicar en esta tutorial. Sin embargo esta pensado para una destinatario joven que quiere hacer apps rápido sin preocuparse de aprender sólidamente los conceptos.

Recomiendo :

1. Hacer el ejemplo del libro => el programa adjunto de este repositorio

2. Profundizar en los conceptos en la web de documentación

Normalmente se hará un programa por capitulo incluyendo todas las partes que a veces en el capitulo se ven paso a paso

### **Capitulo 1.1 - Instalación**

Instalar la libreria con Thonny es lo mas sencillo, aparte de las opciones que da el libro o las que indica en la documentación en [guizero- installation](https://lawsie.github.io/guizero/#installation)

![](./doc/install1.png)

![](./doc/install2.png)

### **Capitulo 1 - Hola mundo / widget = App**

Nota: widget no tiene una traducción directa, se podría decir que es una mini-aplicación, dentro de una aplicación mas grande

1- Haz el programa del capitulo 1 o ejecuta el programa

[BMMP_CL30_GZch1hola_1_0.py](BMMP_CL30_GZch1hola_1_0.py)

2- Recomiendo leer el principio de  [Using Widgets - guizero](https://lawsie.github.io/guizero/usingwidgets/). Resumen:

- Cada app de guizero necesita una [App](https://lawsie.github.io/guizero/app/) widget => será la ventana principal

- Cada widget que se añada ha de referenciarse a la app

- Importa solo los widgets que necesites

```
from guizero import App, Text, PushButton, Slider
```

- Al final debe haber una instrucción para mostrar la app, como en el ejemplo ch1 : **`aplicacion.display()`**

```
aplicacion = App(title="Hola Mundo JCSP")
message = Text(aplicacion, text="Bienvenido a la app")
aplicacion.display()
```

- Todo lo que aparece en la GUI son widget : text boxes, buttons, sliders ...

- **Todos los widgets**  van entre la línea que crea la app y la linea `app.display()` 

### Capitulo 2 / widget = Text, Picture

1- Haz el programa del capitulo 2 o ejecuta el programa

[BMMP_CL30_GZch2wanted_1_0.py](BMMP_CL30_GZch2wanted_1_0.py)

2- Recomiendo **profundizar un poco en el widget 'App'** leyendo la documentación [App - guizero](https://lawsie.github.io/guizero/app/). Para este programa ch2 resumo algunas informaciones :

- La ventana que se crea por defecto con  `aplicacion = App()` es de 500 x 500

- Ningún parámetro en la creación de App es obligatorio

- A posteriori de la creación se puede cambia cualquier valor de los parámetros de creación , que ahora serán propiedades , ejemplo para cambiar a posteriori el color de fondo

```
aplicacion.bg = "#1CE0D6"
```

3- Recomiendo profundizar un poco en el **widget Text** [Text - guizero](https://lawsie.github.io/guizero/text/) . Resumen:

- Es obligatorio incluir un paramento con el "master" = el contenedor al que el widget pertenece : el nombre de la app creada con `App`

- La alineación por defecto = None = "top"

- A posteriori de la adición del widget Text, se puede cambiar cualquier valor de los parámetros de creación , que ahora serán propiedades , ejemplo

```
wanted_text.text_size = 50
wanted_text.font = "Bodoni MT"
```

Nota: el tamaño del texto como parámetro es 'size', pero como propiedad es 'text_size'

4- Recomiendo profundizar un poco en el **widget Picture** [Picture - guizero](https://lawsie.github.io/guizero/picture/)

- Es obligatorio incluir un paramento con el "master" = el contenedor al que el widget pertenece : el nombre de la app creada con `App`

- El nombre del fichero debe incluir el path

`picture = Picture(app, image="images/test.gif")`

- Se soportan imágenes GIF y PNG por defecto. Otros tipos de imagen requieren instalar un paquete adicional

### Capitulo 3 - Sugerir nombre de espía / widgets = PushButton

1- Haz el programa del capitulo 3 o ejecuta el programa

[BMMP_CL30_GZch3spy_1_0.py](BMMP_CL30_GZch3spy_1_0.py)

2- Recomiendo **profundizar un poco en el widget 'PushButton'** leyendo la documentación [PushButton - guizero](https://lawsie.github.io/guizero/pushbutton/) . Para este programa ch3 resumo algunas informaciones :

- El widget  `PushButton` muestra un boton con texto o una imagen dentro, y al ser presionado llama a una función.

- Es obligatorio incluir un paramento con el "master" = el contenedor al que el widget pertenece : el nombre de la app creada con `App`

- El parámetro de función a llamar es como la llamada de una función de interrupción

- **NO ENTIENDO** porque para devolver el valor a un widget Text, no se declara la variable como global al final de la función

```
def choose_name():
    print("Button was pressed")
    first_names = ["Rafa", "Fernando", "Begoña", "Jose", "Carlos", "Gema"]
    last_names = ["Garcia", "Perez", "Sanchez", "Gomez", "Anton", "Martin"]
    spy_name = choice(first_names) + " " + choice(last_names)
    print(spy_name)
    name.value = spy_name # no entiendo porque no hay que definirla como Global !!!
```

- Se soportan imágenes GIF y PNG por defecto. Otros tipos de imagen requieren instalar un paquete adicional

### Capitulo 4 - Crear memes / widgets = TextBox, Drawing, Combo, Slider

1- Haz el programa del capitulo 4 o ejecuta el programa

[BMMP_CL30_GZch4meme_1_0.py](BMMP_CL30_GZch4meme_1_0.py)

El programa tiene 1 App master y 6 widgets = 2 TextBox + 2 Combo + 1 Slider + 1 Drawing

Cada cambio en los widgets : 2 TextBox + 2 Combo + 1 Slider, llama a una función de re-pintado del meme, todos a al misma por simplicidad

Cambio en TextBox = escribir otro texto el la caja de texto

Cambio en Combo = seleccionar color o tipo de letra en una lista drop-down

Cambio en el slider = mover el valor de tamaño de texto

2- Recomiendo **profundizar un poco en el widget 'TextBox'** leyendo la documentación [TextBox - guizero](https://lawsie.github.io/guizero/textbox/)   . Resumo:

- Crea una caja de texto donde el usuario puede escribir, seria como un `input` de Python

- Se puede poner un texto inicial en la caja

- Si se añade una función en `command` se ejecuta en los cambios = escribir otro texto el la caja de texto

- Si se añade una función a ejecutar NO DEBE tener argumentos o solo 1. >La documentacion parece decir que el argumento lo tomo de lo introducido en la text box

3- Recomiendo **profundizar un poco en el widget 'Combo'** leyendo la documentación [Combo - guizero](https://lawsie.github.io/guizero/combo/). Resumo:

- Crea un 'drop-down-box' para seleccionar 1 SOLA opción

- Las opciones se proporcionan como Lista entre ' [ ] '. Se puede poner una opcion por defecto

- Si se añade una función en `command` se ejecuta en los cambios = seleccionar otra opción en la lista drop-down

- Si se añade una función a ejecutar NO DEBE tener argumentos o solo 1.  Si tiene 1 argumento se toma la selección actual como argumento

4- Recomiendo **profundizar un poco en el widget 'Slider'** leyendo la documentación [Slider - guizero](https://lawsie.github.io/guizero/slider/). Resumo:

- Muestra una barra horizontal con un dial que se puede desplazar para dar un valor entero entre dos limites

- Si se añade una función en `command` se ejecuta en los cambios = mover el dial

- Argumentos de la función en `command` , la documentación dice que ha de tener un argumento, pero en el ejemplo no tiene y funciona.

5- Recomiendo **profundizar un poco en el widget 'Drawing'** leyendo la documentación [Drawing - guizero](https://lawsie.github.io/guizero/drawing/). Resumo:

- Es como un cajón de sastre para crear figuras geométricas dentro de una ventana: líneas, rectángulos, círculos, polígonos, etc.

- También vuelca imágenes ( como en el ejemplo del capitulo) 

- NO llama a ninguna función, porque la lógica es mas bien diferente :
  
  - Crear el widget Drawing
  
  - Dibijar cosas : lineas, imagenes , etc.
  
  - llamar al master.display()

### Capitulo 5 / metodos .after(), .cancel() y .repeat()

1- El capitulo 5 es un conjunto de programas MAL hechos para aprender. Baja los programas del repositorio y ejecuta 1 a 1 con la explicación del libro



**El programa mas interesante es el ch5-2**, que usa el método repeat()

2- Recomiendo profundizar un poco en los métodos .after(), .cancel() y .repeat() de App  en la documentación [App - guizero](https://lawsie.github.io/guizero/app/). Resumo algunas informaciones :

- Hay un 'scheduler' que se puede programar para que llame a una función
  - A intervalos fijos **.repeat()**
  - Solo una vez despues de un tiempo **.after()**
  - para cancelar la funcion que se llama con **.cancel()**
- El programa ch5-2 tiene problemas según como se salga de el en Thonny. Si se ejecuta en cmd NO hay estos problemas. Esta la opción de incluir 

```
app.when_closed = app.cancel(flash_text)
```

Para cancelar la función que se llama con el 'scheduler'

- Se puede simular repeat() con after() haciendo llamadas recursivas - ver ch 7 programa mataPun

### Capitulo 7 - Matar puntos rojos / widgets = Waffle

1- Haz el programa del **capitulo 7** o ejecuta el programa

[BMMP_CL30_GZch7_mataPun_1_0.py](BMMP_CL30_GZch7_mataPun_1_0.py)

OBJETIVO: en una retícula de 5 x 5 ( se puede cambiar), se van cambiando aleatoriamente cuadrados blancos por puntos rojos. Hay que ir matando los puntos clicando, para retornarlos a cuadrado. Cada retorno suma 1 punto. Se pierde cuando todos los 5 x5 cuadrados son puntos rojos.

**¿Cómo esta construido el programa y la dinámica del juego?**

Crea un App y 3 widgets : 2 Text y un Waffle, en este ultimo se ejecuta el juego. El waffle es el 'board' con funcion de callback:

-  para destruir los cirulos rojos

- sumar puntos

Se lanza el bucle de juego con 

```
board.after(1000, add_dot)
```

El método .after() programa una llamada UNICA a la función de callback indicada despues de un tiempo dado en milisegundos (Para repetir las llamadas se debería usar el método repeat() ) 

`add_dot()` lleva la dinámica de añadir puntos aleatorios. Y luego en `add_dot()` se vuelve a hacer una llamada recursiva SI no estamos al final de juego, SI estamos al FINAL del juego :

- muestra un mensaje de que se ha perdido y los puntos finales

- **MEJORA respecto al libro**: debe deshabilitar el `board` porque si no una vez acabado el juego aun funcionaria el `destroy_dot`

2- Recomiendo **profundizar un poco en el widget 'Waffle'** leyendo la documentación  [Waffle - guizero](https://lawsie.github.io/guizero/waffle/). Resumo:

- Muestra una retícula de n x n cuadrados o puntos. en este programa el uso es muy básico, es como un waffle de los de comer

- Es obligatorio incluir un paramento con el "master" = el contenedor al que el widget pertenece : el nombre de la app creada con `App`

- Convertir una zona de la retícula en cuadrado o circulo (dot) se controla con la propiedad `dotty` a True o a False

```
board[x, y].dotty = True # Convierte en dot
```

- La función de callback ha de tener o 0 o 2 argumentos que son las coordenadas x e y, de la retícula tocada

---

TO DO : 
