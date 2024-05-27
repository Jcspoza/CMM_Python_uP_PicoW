# Funciones Recursivas en Python

## Objetivo e introducción

En esta clase vamos a estudiar una forma de implementar algoritmos que es la recursividad 

*La **recursividad** o recursión es un concepto que proviene de las matemáticas, y que aplicado al mundo de la programación nos permite resolver problemas o tareas donde las mismas pueden ser divididas en subtareas cuya funcionalidad es la misma.*

En realidad en la mayoría de los casos, el mismo algoritmo que se implementa con recursividad se puede implementar con bucles. El porque se hace en algunos casos de **forma recursiva es porque la implementación es mas concisa y clara**

### Tutoriales que vamos a seguir

1. [El tutorial mas básico es el de "El libro de Python"](https://ellibrodepython.com/recursividad) : que es una web básica de aprendizaje de python => NO LO VAMOS A SEGUIR . ES SOLO PAR AUNA 1RA LECTURA

2. En castellano un buen tutorial para entender como funcionan las llamadas sucesivas es [90 - Recursividad: Conceptos básicos](https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=90&codigo=91&inicio=75)

3. Pero como siempre el tutorial definitivo es el de Real Python [Recursion in Python: An Introduction – Real Python](https://realpython.com/python-recursion/)

### Tabla resumen de programas

| Programa                                                                           | Tutorial-parte | Objetivo de Aprendizaje                                                                                                        |
| ---------------------------------------------------------------------------------- |:--------------:| ------------------------------------------------------------------------------------------------------------------------------ |
| [BMMP_CLFR_T2_312print_rec_MAL_1_0.py](BMMP_CLFR_T2_312print_rec_MAL_1_0.py)       | T2             | Programa de recursividad mal hecho -> NO para nunca                                                                            |
| [BMMP_CLFR_T2_313print_rec_OK_1_0.py](BMMP_CLFR_T2_313print_rec_OK_1_0.py)         | T2             | Imprime una cuenta de números descendente- Algoritmo recursivo                                                                 |
| [BMMP_CLFR_T2_314print_rec_OK_inv_1_0.py](BMMP_CLFR_T2_314print_rec_OK_inv_1_0.py) | T2             | Imprime una cuenta de números ASCENDENTE- Algoritmo recursivo -> Ver la importancia de la salida del algoritmo RECURSIVO       |
| [BMMP_CLFR_T3_printDn_bucleInv_1_0.py](BMMP_CLFR_T3_printDn_bucleInv_1_0.py)       | T3             | Imprime una cuenta de números DESCENDENTE- Algoritmo ITERATIVO                                                                 |
| [BMMP_CLFR_T3_printUp_bucle_1_0.py](BMMP_CLFR_T3_printUp_bucle_1_0.py)             | T3             | Imprime una cuenta de números ASCENDENTE - Algoritmo ITERATIVO                                                                 |
| [BMMP_CLFR_T3_Factorial_Rec_1_0.py](BMMP_CLFR_T3_Factorial_Rec_1_0.py)             | T3             | Cálculo de Factorial de un número - algoritmo RECURSIVO                                                                        |
| [BMMP_CLFR_T3_Factorial_Bucle_1_0.py](BMMP_CLFR_T3_Factorial_Bucle_1_0.py)         | T3             | Cálculo de Factorial de un número - algoritmo ITERATIVO (BUCLE)                                                                |
| [BMMP_CLFR_T3_Factorial_reduce_1_0.py](BMMP_CLFR_T3_Factorial_reduce_1_0.py)       | T3             | Cálculo de Factorial de un número - algoritmo FUNCION REDUCE                                                                   |
| [BMMP_CLFR_T3_Factor_ComparTm_1_0.py](BMMP_CLFR_T3_Factor_ComparTm_1_0.py)         | T3             | Compara los tiempos de ejecución de cuatro implementaciones de la función Factorial: Iterativa, Recursiva, Reducción e Interna |

### Recomendaciones de estudio

A- Leer el tutorial 1 como introducción. Sirve para un primer acercamiento, pero no aclara bien como construir funciones recursivas ni porque en algun caso son mas "sencillas"

B- El tutorial 2 aclara bien los conceptos de llamadas y pilas

C- Es el tutorial 3 el que aclara definitivamente los conceptos

## **Primeros pasos con Funciones recursivas - Tuto 2** - pilas de llamada

Recomiendo ejecutar los programas del tutorial 2 números 312, 313, y 314

El primer programa 312, esta MAL para ver como si no se tiene cuidado la recursividad puede no terminar nunca

[BMMP_CLFR_T2_312print_rec_MAL_1_0.py](BMMP_CLFR_T2_312print_rec_MAL_1_0.py)

Los programas 313 y 314 imprimen los números comprendidos entre el valor de la llamada y 0: es decir `imprimir(5)` producirá con el programa [BMMP_CLFR_T2_313print_rec_OK_1_0.py](BMMP_CLFR_T2_313print_rec_OK_1_0.py)

```
Topic : Funciones Recursivas - Ref : T2. 90 - Recursividad: Conceptos básicos
Libreria: None
Program: Programa que imprime hasta cero Mayor>menor - Recursivo Ok - Version: 1.0
5
4
3
2
1
```

pero con el programa [BMMP_CLFR_T2_314print_rec_OK_inv_1_0.py](BMMP_CLFR_T2_314print_rec_OK_inv_1_0.py)

producirá la lista pero de menor a Mayor

```
Topic : Funciones Recursivas - Ref : T2. 90 - Recursividad: Conceptos básicos
Libreria: None
Program: Programa que imprime hasta cero menor> Mayor - Recursivo Ok - Version: 1.0
1
2
3
4
5
```

Estos programas hay que verlos juntos, y sirven junto a los dibujos del tutorial para ver como se van guardando en pila las distintas llamas y variables locales.

¿ **Por qué uno imprime de MAYOR > menor y el otro de menor > MAYOR**? Es por la posición de la instrucción `print(x)` anterior o posterior a la llamada recursiva

## Tuto 3 . Recursividad versus Iteracion (Bucle)

En el tutorial 3 leemos hasta **Get Started: Count Down to Zero**. La mayoría de los conceptos estan ya dichos en el tutorial T2, pero en este tutorial se desarrollan mas y mejor los conceptos.

Comparemos la implementación de los programas para imprimir números en cuenta descendente  <u>**Algoritmo de Iteracion (bucle)**</u>

en Bucle : [BMMP_CLFR_T3_printDn_bucleInv_1_0.py](BMMP_CLFR_T3_printDn_bucleInv_1_0.py)

```
def cuentaAbajoBucle(n):
    while n >= 0:
        print(n)
        n -= 1
```

<u>**Algoritmo Recursivo**</u> : [BMMP_CLFR_T2_313print_rec_OK_1_0.py](BMMP_CLFR_T2_313print_rec_OK_1_0.py)

```
def cuentaAbajo(x):
    if x>0:
        print(x)
        cuentaAbajo(x-1)
```

Ver los **ejemplos de cuenta arriba recursivo**

[BMMP_CLFR_T2_314print_rec_OK_inv_1_0.py](BMMP_CLFR_T2_314print_rec_OK_inv_1_0.py)

y con **iteración (bucle)**  [BMMP_CLFR_T3_printUp_bucle_1_0.py](BMMP_CLFR_T3_printUp_bucle_1_0.py)

## ¿Por qué usar la Recursividad? T3- Factorial

Es el ejemplo clásico de los tutoriales de recursividad. Seguiremos el Tutorial T3

### **Algoritmo Recursivo**

[BMMP_CLFR_T3_Factorial_Rec_1_0.py](BMMP_CLFR_T3_Factorial_Rec_1_0.py)

```
def factorialRec(n):
    print(f"factorial() called with n = {n}") # debug
    return_value = 1 if n <= 1 else n * factorialRec(n -1)
    print(f"-> factorial({n}) returns {return_value}") # debug
    return return_value
```

Lo interesante del ejemplo es ver como se van sucediendo las llamadas a la función recursiva

```
Topic : Funciones Recursivas - Ref : Recursion in Python: An Introduction
Libreria: None
Program: Programa que calcula el factorial - Recursivo - Version: 1.0
factorial() called with n = 5
factorial() called with n = 4
factorial() called with n = 3
factorial() called with n = 2
factorial() called with n = 1
-> factorial(1) returns 1
-> factorial(2) returns 2
-> factorial(3) returns 6
-> factorial(4) returns 24
-> factorial(5) returns 120
Algoritmo Recursivo -> factorial(5) = 120
```

### Algoritmo Iterativo (con **un bucle**)

 [BMMP_CLFR_T3_Factorial_Bucle_1_0.py](BMMP_CLFR_T3_Factorial_Bucle_1_0.py)

```
def factorialBucle(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i

    return return_value
```

### Algoritmo Funcional - meta función Reduce

Hay otra manera de hacer estos cálculos y es con la meta-función `reduce` ( meta-función es un concepto propio).

La la meta-función `reduce` 

**reduce todos los elementos de un iterable( una lista por ejemplo) a un único valor** aplicando una función a sus 2 primeros elementos, y con ese valor se aplica de nuevo la función al 3er elemento , etc. 

```
from functools import reduce

# Funcion - Factorial con Reduce
def factorialReduce(n):
    """ Reduce aplica una funcion a un iterable empezando con los 2 primeros items, el resultado lo toma como
    1er argumento junto con el 3er elemento iterable y el resultado lo tomo como 1er argumento junto al
    4to elemento , etc. . Puede incluir un elemento de inicializacion
    """
    # multiplica todos los numeros consecutivos hasta n incluido. Si n=0
    # range(1,1) = > [] , asi que usamos un 'or' para tener [1]
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
```

### ¿ Cual es mejor?

Hay que atender a 2 criterios :

- **Legibilidad** -> menor probabilidad de errores & Mejor mantenibilidad

- **Rapidez**

<u>Legibilidad</u> => Recursivo vs Iterativo : son mas o menos igual de legibles, **quizá mas elegante el recursivo**

<u>Rapidez</u> => Recursivo vs Iterativo : son mas o menos igual de legibles, **mas rápido el Iterativo**

Veamos como comprobar la rapidez con un programa propio:

( explicación ver Tuto 3)

[BMMP_CLFR_T3_Factor_ComparTm_1_0.py](BMMP_CLFR_T3_Factor_ComparTm_1_0.py)

Vemos los siguientes tiempos para factorial de 4 (x10Millones de veces)

- Algoritmo Iterativo = 2.14

- Algoritmo Recursivo = 2.56

- Algoritmo con Función Reduce = 4.17

- Algoritmo con Función Factorial interna = 0.22

Los algoritmos iterativos y recursivos son muy parecidos

---

TO DO :  del Tutorial 3 : Lista anidada / Palíndromos / Quciksort
