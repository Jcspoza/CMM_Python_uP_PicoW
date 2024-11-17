# CL4 - Escribir Adivina Numero (seleccion y bucles) - PyR 2024_25 CMM BML

## Clase 3 - Indice - 90 minutos

- Vistazo a Capitulo 3 de ***Invent with Python ...***
  
  - Cambiamso el bucle for por while por simplificar 

- Adivina numero 1 sola apuesta (sin bucles)

- Adivina numero varias apuestas (con bucle)

- Conceptos cubiertos en este capitulo

- Preguntas sobre la Clase 1 - 10 minutos

## Tutoriales y Programas que vamos a seguir

### Tutoriales resumen

[Introducing Thonny - YouTube](https://youtu.be/nwIgxrXP-X4?si=eb19qXyd4cJWSYng)

### Tabla resumen de programas

| Programa                                                             | Lenguaje | Objetivo de Aprendizaje                           |
| -------------------------------------------------------------------- | -------- | ------------------------------------------------- |
| [P2425_adivinanumsimple.py](./P2425_adivinanumsimple.py)             | Py       | Selección con if                                  |
| [P2425_adivinanumcompleto2_0.py ](./P2425_adivinanumcompleto2_0.py)  | Py       | Bucles **while**                                  |
| [P2425_adivinanumcompletoMej1.py](./P2425_adivinanumcompletoMej1.py) | Py       | **elif**                                          |
| [P2425_adivinanumcompletoMej2.py](./P2425_adivinanumcompletoMej2.py) | Py       | Condiciones lógicas compuestas : **and, or, not** |

### Recomendaciones de estudio despues de la clase

Leer capitulo 3 de libro "Invent with python" [Chapter 3 - GUESS THE NUMBER](https://inventwithpython.com/invent4thed/chapter3.html), explica como hacer este programa pero con bucles for en vez de while

---

## Vistazo a Capitulo 3 de  ***Invent ...*** y cambios– 10'

En el libro se usan los  <u> bucles **for** que son mas complejos que los **while** en Python.</u> **Por eso he optado por reescribir el programa con bucles while:**

- Para bucles poco complejos siempre se puede optar por programar el bucle con **for** o **while**

- Los bucles **for** en Python estan mas enfocados a recorrer objetos compuestos como listas o tupls ( no lo s hemso visto)

## Analizamos Adivinanumsimple = 1 sola apuesta (sin bucles)-  15'

[P2425_adivinanumsimple.py](./P2425_adivinanumsimple.py)

## Analizamos Adivina numero para varias apuestas (con bucles)- 15'

[P2425_adivinanumcompleto2_0.py ](./P2425_adivinanumcompleto2_0.py)

Lo +  interesante :

- Inicialización

- Ver como esta construido el bucle y como se sale

- En la parte 3 despues del bucle , hay que determinar por cual de las condiciones se salió

## Posibles Mejoras de AdivinanumeroComplejo

### Una condición de salida si se introduce 0

[P2425_adivinanumcompletoMej1.py](./P2425_adivinanumcompletoMej1.py)

### Todas las condiciones de salida en el while: condiciones lógicas compuestas

El bucle de juego se puede escribir de forma mas limpia evitando los  `break` Se trata de escribir al condición del bucle de juego ( el while) como una condición compuesta usando expresiones lógicas y uniéndolas con **`and or`**

[P2425_adivinanumcompletoMej2.py](P2425_adivinanumcompletoMej2.py)

La dificultad de los principiantes es si se debe usar **and** o por el contrario **or**. En realidad siempre es posible escribir la expresión con and o con or, pero uno de los casos es mas sencillo que el otro . Veamos nuestro caso ( solo la condición lógica)

`apuestas < MAXAPUESTAS and numeroSupuesto != numero and numeroSupuesto != 0:`

En este caso se puede salir del bucle por CUALQUIERA  de una de las 3 condiciones, por lo que pareceria mas logico usar or, y en este caso con or la formulacion logica alternativa seria:

`not(apuestas == MAXAPUESTAS or numeroSupuesto == numero or numeroSupuesto == 0)`

Esto es conocido como **Teorema de Morgan** de la logica booleana:

*La negación de la conjunción es la disyunción de las negaciones. La negación de la disyunción es la conjunción de las negaciones. o informalmente como: «no (A y B)» es lo mismo que «(no A) o (no B)», y también, «no (A o B)» es lo mismo que «(no A) y (no B)»*

## Conceptos cubiertos en este capitulo - 5'

En esta clase hemos cubierto los siguientes conceptos de lenguaje Python: 

- import y modulos

- La función  ‘randint()’

- Input con mensajes antes del texto a introducir

- Unir cadenas con el operador  ‘+’ 

- Selección con ‘if’, elif, else

- Operadores de comparación y la diferencia entre ‘=‘ y ‘==‘

- Bloques

- Bucles con while

- Sentencia ‘break’

- Expresiones lógicas compuesta y conversiones con el Teorema de Morgan

## Preguntas sobre la Clase 3 - 10 minutos

Sección para que los alumnos pregunten sus dudas durante la clase

---

TO DO :
