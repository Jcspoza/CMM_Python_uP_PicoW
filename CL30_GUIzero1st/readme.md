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

| Programa                     | Capitulo del libro | Objetivo de Aprendizaje           |
| ---------------------------- |:------------------:| --------------------------------- |
| BMMP_CL30_GZch1hola_1_0.py   | ch1                | primeros paso - crear una ventana |
| BMMP_CL30_GZch2wanted_1_0.py | ch2                |                                   |
| BMMP_CL30_GZch3spy_1_0.py    | ch3                |                                   |
| BMMP_CL30_GZch4meme_1_0.py   | ch4                |                                   |
|                              |                    |                                   |
|                              |                    |                                   |
|                              |                    |                                   |

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

### Capitulo 2

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

- A posteriori de la adicion del widget Text, se puede cambiar cualquier valor de los parámetros de creación , que ahora serán propiedades , ejemplo

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

---

TO DO : 
