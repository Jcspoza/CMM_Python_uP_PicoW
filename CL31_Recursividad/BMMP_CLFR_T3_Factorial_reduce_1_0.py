# Taller Programación y Robótica en CMM BML – 2023 - Clase xx
# Resumen: Funciones Recursivas en Python
# Topicos nuevos: Recursividad
# Ref Tutorial : T1. Recursion in Python: An Introduction
# Ref link https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=90&codigo=91&inicio=75
# Fecha inicio 2024 05 25
# Licencia : CC BY-NC-SA 4.0
# Proyecto Programa que calcula el factorial - funcion Reduce
# Version 1.0 

# IMPORTAR
from functools import reduce

# Informative block - start
p_topic = "Funciones Recursivas"
p_project = "Programa que calcula el factorial - funcion reduce"
p_ref = "Recursion in Python: An Introduction"
p_version = "1.0"
p_keyLib = "functools"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# Funcion - Factorial con Reduce
def factorialReduce(n):
    """ Reduce aplica una funcion a un iterable empezando con los 2 primeros items, el resultado lo toma como
    1er argumento junto con el 3er elemento iterable y el resultado lo tomo como 1er argumento junto al
    4to elemento , etc. . Puede incluir un elemento de inicializacion
    """
    # multiplica todos los numeros consecutivos hasta n incluido. Si n=0
    # range(1,1) = > [] , asi que usamos un 'or' para tener [1]
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
        
# 1 - ejecuto la funcion
print(f"Algoritmo bucle -> factorial(5) = {factorialReduce(5)}")
