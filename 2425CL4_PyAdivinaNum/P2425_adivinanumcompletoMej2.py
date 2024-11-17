# Taller Programación y Robótica CMM BML – 2024 -2025 - Clase 4
# Nombre de programa : P_adivinanumerocompletoRETOCL3.py
# Mejora 2 'Adivina Numero completo' para que el jugador pueda abandonar
# Topicos nuevos: importar libreria, bloques, bucle for , flujo condicional if,
# ... cambiar tipos, tipado dinamico, operadores de comparacion
# Creditos : adaptacion de JCSP basado en "Invent with python" ed4 - cap. 3
# https://inventwithpython.com/invent4thed/chapter3.html
# Fecha JCSP 2023 02 09
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es
# version 2.0 for -> while
# Mejora num 2

# BLOQUE JUEGO 1 de 3: Inicializacion
import random

MAXAPUESTAS = 6 # Las constantyes se nombran en mayusculas por convencion

print('Hola! ¿Cuál es tu nombre?')
miNombre = input()

numero = random.randint(1, 20)
print('Vale, ' + miNombre + ', he pensado un numero del 1 al 20.')

# BLOQUE JUEGO 2 de 3: Bucle de juego
apuestas = 0
numeroSupuesto = -1
# Formulacion logica alternativa
# while not(apuestas == MAXAPUESTAS or numeroSupuesto == numero or numeroSupuesto == 0):

while apuestas < MAXAPUESTAS and numeroSupuesto != numero and numeroSupuesto != 0:
    numeroSupuesto = int(input('¡Intenta adivinarlo! Di un número (0 para salir) ')) #cambio de tipo de cadena a entero
    apuestas = apuestas + 1 # actualizo el numero de apuestas hechas
      
    if numeroSupuesto < numero and numeroSupuesto != 0:
        print('Tu número esta demasiado bajo.') # 8 espacios antes de "print"

    if numeroSupuesto > numero:
        print('Tu número esta demasiado alto.')

# BLOQUE JUEGO 3 de 3: Final Ganas / Fierdes / Decides salir
if numeroSupuesto == 0 :
    print('¡Decidiste salir del juego ', 'cuando habias hecho ', apuestas-1, ' apuestas')
elif numeroSupuesto == numero:
    print('Bien hecho, ' + miNombre + ' adivinaste mi mumero en ', apuestas, ' apuestas')
    print('El numero que habia pensado era ', numero)
else:
    print('No adivinaste mi numero en ', MAXAPUESTAS, ' intentos')
    print('El numero que habia pensado era ', numero)

