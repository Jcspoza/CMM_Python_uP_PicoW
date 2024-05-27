# Taller Programación y Robótica en CMM BML – 2023 - Clase xx
# Resumen: Funciones Recursivas en Python
# Topicos nuevos: Recursividad
# Ref Tutorial : T1. Recursion in Python: An Introduction
# Ref link https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=90&codigo=91&inicio=75
# Fecha inicio 2024 05 25
# Licencia : CC BY-NC-SA 4.0
# Proyecto Programa que imprime hasta cero de Mayor>menor - Bucle
# Version 1.0 

# IMPORTAR modulo GUIzero

# Informative block - start
p_topic = "Funciones Recursivas"
p_project = "Programa que imprime hasta cero de Mayor>menor - Bucle"
p_ref = "Recursion in Python: An Introduction"
p_version = "1.0"
p_keyLib = "None"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# Funcion - Recursiva bien hecha
def cuentaAbajoBucle(n):
    while n >= 0:
        print(n)
        n -= 1
    
# 1 - ejecuto la funcion
cuentaAbajoBucle(5)    
