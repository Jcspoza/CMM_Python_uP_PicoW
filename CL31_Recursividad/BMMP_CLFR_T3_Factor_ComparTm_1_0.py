# Taller Programación y Robótica en CMM BML – 2023 - Clase xx
# Resumen: Funciones Recursivas en Python
# Topicos nuevos: Recursividad
# Ref Tutorial : T1. Recursion in Python: An Introduction
# Ref link https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=90&codigo=91&inicio=75
# Fecha inicio 2024 05 25
# Licencia : CC BY-NC-SA 4.0
# Proyecto Programa que compara el Tiempo de ejecucion de implementaciones de factorial
# Version 1.0 

# IMPORTAR
from timeit import timeit
from functools import reduce


# Informative block - start
p_topic = "Funciones Recursivas"
p_project = "Programa que compara el Tiempo de ejecucion de implementaciones de factorial"
p_ref = "Recursion in Python: An Introduction"
p_version = "1.0"
p_keyLib = "timeit & functools"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# Funcion - Recursiva Factorial
def factorialReduce(n):
    """ Reduce aplica una funcion a un iterable empezando con los 2 primero items, el resultado lo toma como
    1er argumento junto con el 3er elemento iterable y el resultado lo tomo como 1er argumento junto al
    4to elemento , etc. . Puede incluir un elemento de inicializacion
    """
    # multiplica todos los numeros consecutivos ahsta n incluido. Si n=0
    # range(1,1) = > [] , asi que usamso un 'or' para tener [1]
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
        
# 0.1 - Funciones definidas en strings para setup de Factorial con Iteraciones (Bucles)
setupS_FactBuc = """
print("Algoritmo Iterativo")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
    """
# 0.2 - Funciones definidas en strings para setup de Factorial con Recursividad
setupS_FactRec = """
print("Algoritmo Recursivo")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
    """
# 0.3 - Funciones definidas en strings para setup de Factorial con Iteraciones (Bucles)
setupS_FactRed = """
from functools import reduce
print("Algoritmo con Funcion Reduce:")
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
    """
# 0.4 - Funciones definidas en strings para setup de Factorial con funcion interna
setupS_FactInt = """
from math import factorial
print("Algoritmo con Funcion Factorial interna")
    """

print()
timeFactBuc = timeit("factorial(4)", setup=setupS_FactBuc, number=10_000_000)
print(f'El tiempo empleado para factorial de 4 (x10M) con algoritmo en bucle = {timeFactBuc}')
print()
timeFactRec = timeit("factorial(4)", setup=setupS_FactRec, number=10_000_000)
print(f'El tiempo empleado para factorial de 4 (x10M) con algoritmo recursivo = {timeFactRec}')
print()
timeFactRed = timeit("factorial(4)", setup=setupS_FactRed, number=10_000_000)
print(f'El tiempo empleado para factorial de 4 (x10M) con algoritmo funcion Reduce = {timeFactRed}')
print()
timeFactInt = timeit("factorial(4)", setup=setupS_FactInt, number=10_000_000)
print(f'El tiempo empleado para factorial de 4 (x10M) con algoritmo funcion Interna = {timeFactInt}')
