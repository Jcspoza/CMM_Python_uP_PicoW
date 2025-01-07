# CL2 - Escribir los primeros programas en Python con Thonny - PyR 2024_25 CMM BML

## Clase 2 - Indice - 90 minutos

- ¿ Como usar el libro ***Invent with Python ...***?

- Escribimos y ejecutamos programas
  
  - 2 programas en Secuencia
  
  - 1 programa con con bucle **while**
  
  - 1 programa con Seleccion con **if**

- Uso de Debug de Thonny, con un ejemplo de programa mal escrito

- Conceptos cubiertos en este capitulo

- Preguntas sobre la Clase 1 - 10 minutos

## Tutoriales y Programas que vamos a seguir

### Tutoriales resumen

[Introducing Thonny - YouTube](https://youtu.be/nwIgxrXP-X4?si=eb19qXyd4cJWSYng)

### Tabla resumen de programas

| Programa                                                       | Lenguaje | HW si Robotica y Notas                                                 | Objetivo de Aprendizaje                             |
| -------------------------------------------------------------- | -------- | ---------------------------------------------------------------------- | --------------------------------------------------- |
| [P2425CL2_holaplus.py](./P2425CL2_holaplus.py)                 | Python   |                                                                        | **Flujo en secuencia**                              |
| [P2425CL2_multiplicasimple.py](./P2425CL2_multiplicasimple.py) | Python   |                                                                        | **Tipos numéricos**, 2 variables                    |
| [P2425CL2_cuentaAtras.py](./P2425CL2_cuentaAtras.py)           | Python   | Se podía haber hecho con for                                           | **bucles while** Flujo en bucles                    |
| [P2425CL2_parimpar.py](P2425CL2_parimpar.py)                   | Python   |                                                                        | **Selección** con **if**                            |
| [P2425CL2_debugPcafeBIEN.py](P2425CL2_debugPcafeBIEN.py)       | Python   | Varios programas mal escritos para ir corrigiéndolos hasta el correcto | uso básico de Debug, basico por no usar breakpoints |

### Recomendaciones de estudio despues de la clase

Ayuda de Thonny y

**+**

Leer capitulo 2 de libro "Invent with python"" [Chapter 2 - Writing Programs](https://inventwithpython.com/invent4thed/chapter2.html), que muestra un IDE muy sencillo que viene con el propio Python y que se llama IDLE

---

## ¿Cómo usar el libro ***Invent with Python ...***?– 15 minutos

Se muestra en la clase como usar la web del libro en ingles y el libro en castellano

## Escribimos y ejecutamos programas incluyendo Debug de Thonny-  60'

### Holaplus.py

### P2425CL2_multiplicasimple.py

### P2425CL2_cuentaAtras.py

### P2425CL2_parimpar.py

### Debuger en Thonny

Un buen video introductorio es 

[Ejemplo Python: Encuentra los errores de tus programas usando el debugger de Thonny - YouTube](https://youtu.be/NYYT0J8nf3o?si=UcN4g8975rK0qkV8)

Lo vamos a hacer en vivo siguiendo un ejemplo casi igual la del video, pero antes veamos los 3 tipos de error ( cap 6 invent with python..)

#### **Types of Bugs**

There are three types of bugs that can happen in your program:

- **Syntax errors** This type of bug comes from typos. When the Python interpreter sees a syntax error, it’s because your code isn’t written in proper Python language. A Python program with even a single syntax error won’t run.

- **Runtime errors** These are bugs that happen while the program is running. The program will work up until it reaches the line of code with the error, and then the program will terminate with an error message (this is called *crashing*). The Python interpreter will display a *traceback*: an error message showing the line containing the problem.

- **Semantic errors** These bugs—which are the trickiest to fix—don’t crash the program, but they prevent the program from doing what the programmer intended it to do. For example, if the programmer wants the variable total to be the *sum* of the values in variables a, b, and c but writes total = a * b * c, then the value in total will be wrong. This could crash the program later on, but it won’t be immediately obvious where the semantic bug happened.

| Programa                                                 | 1er Error                           | Tipo de Error |
| -------------------------------------------------------- | ----------------------------------- | ------------- |
| [P2425CL2_debugPcafeMAL1.py](P2425CL2_debugPcafeMAL1.py) | Sintaxis indentación print          | Sintáctico    |
| [P2425CL2_debugPcafeMAL2.py](P2425CL2_debugPcafeMAL2.py) | Sintaxis indentación else           | Sintáctico    |
| [P2425CL2_debugPcafeMAL3.py](P2425CL2_debugPcafeMAL3.py) | Division por cero                   | Run time      |
| [P2425CL2_debugPcafeMAL4.py](P2425CL2_debugPcafeMAL4.py) | Concicion 2do if : and en vez de or | Semántico     |
| [P2425CL2_debugPcafeBIEN.py](P2425CL2_debugPcafeBIEN.py) | SIN ERRORES                         |               |

Nota : Para aprender a usar debug, se puede consultar también [el capitulo 6 del llibro invent con ....](https://inventwithpython.com/invent4thed/chapter6.html)  pero emplea un IDE diferente a Thonny y quizá os lie

## Conceptos cubiertos en este capitulo - 5'

En esta clase hemso cubierto los siguientes conceptos: 

- Cadenas de caracteres + unir cadenas

- Tipos de datos:
  
  * Enteros, decimales (float)
  
  * Cadenas
* Usar editor de Thonny

* Salvar los programas en Thonny

* Ejecutar con y sin Debug

* Comments

* Funcion print()

* Funcion input()

* Bucle while

* Selección con if

* NO es lo mismo mayusculas que minusculas

* **Debug con Thonny ( básico)**

## Preguntas sobre la Clase 2 - 10 minutos

Sección para que los alumnos pregunten sus dudas durante la clase

---

TO DO :
