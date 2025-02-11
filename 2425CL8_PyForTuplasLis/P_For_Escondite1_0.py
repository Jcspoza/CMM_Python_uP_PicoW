# Taller Programación y Robótica en Colegio Santo Domingo – 2024 -2025 - Clase 5
# Resumen: Cuenta adelante con for
# Aprendizajes : formatos F-string basico + uso de for con range
# Autor y y Fecha JCSP 2024 10 08
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es

from time import sleep # importamos SOLO la funcion sleep
# Los valores que se usan varias veces en un programa SIN cambiar, se llaman constantes
# Es bueno definirloss al principio por si se quiren cambiar, y asi solo modificar en 1 lugar
# Se suelen nombrar con mayusculas
MAXCUENTA = 20 
PAUSACUENTA = 1.5 # 1 SEGUNDO Y MEDIO

titulo = 'empieza la cuenta del escondite'
print(titulo.upper()) # Cambia un texto a modo frase
print(len(titulo) * '=') # hace un subrallado de *'s de la misma longitud que el titulo
print()

# Empieza la cuenta
# cuentaTemplate = 'Cuenta {:>2d}' # metodo anterior a Python 3.6
for c in range(1,MAXCUENTA+1):
    print(F'Cuento {c:>2d}') # Metodo preferido desde Python 3.7
    # print(cuentaTemplate.format(c))
    sleep(PAUSACUENTA)
    
print('Fin de la cuenta del escondite')