# Taller Programación y Robótica en CMM BML – 2023 - Clase xx
# Resumen: Funciones Recursivas en Python
# Topicos nuevos: Recursividad
# Ref Tutorial : T1. Recursion in Python: An Introduction
# Ref link https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=90&codigo=91&inicio=75
# Fecha inicio 2024 05 25
# Licencia : CC BY-NC-SA 4.0
# Proyecto Programa que calcula el factorial - Recursivo
# Version 1.0 

# IMPORTAR

# Informative block - start
p_topic = "Funciones Recursivas"
p_project = "Programa que calcula el factorial - Recursivo"
p_ref = "Recursion in Python: An Introduction"
p_version = "1.0"
p_keyLib = "None"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# Funcion - Recursiva Factorial
def factorialRec(n):
    print(f"factorial() called with n = {n}") # debug
    return_value = 1 if n <= 1 else n * factorialRec(n -1)
    print(f"-> factorial({n}) returns {return_value}") # debug
    return return_value

    
# 1 - ejecuto la funcion
print(f"Algoritmo Recursivo -> factorial(5) = {factorialRec(5)}")
