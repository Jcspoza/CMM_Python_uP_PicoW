# Taller Programación y Robótica en CMM BML – 2023 - Clase xx
# Resumen: Funciones Recursivas en Python
# Topicos nuevos: Recursividad
# Ref Tutorial : T2. 90 - Recursividad: Conceptos básicos
# Ref link https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=90&codigo=91&inicio=75
# Fecha inicio 2024 05 25
# Licencia : CC BY-NC-SA 4.0
# Proyecto Programa que imprime hasta cero menor> Mayor - Recursivo Ok
# Version 1.0 

# IMPORTAR 

# Informative block - start
p_topic = "Funciones Recursivas"
p_project = "Programa 314 que imprime hasta cero menor> Mayor - Recursivo Ok"
p_ref = "T2. 90 - Recursividad: Conceptos básicos"
p_version = "1.0"
p_keyLib = "None"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# Funcion - Recursiva bien hecha
def cuentaArriba(x):
    if x>0:
        cuentaArriba(x-1)
        print(x)

# 1 - ejecuto la funcion
cuentaArriba(5)    
