# Taller Programación y Robótica en Colegio Santo Domingo – 2024 -2025 - Clase 5
# Resumen: Muestra bromas en pantalla - texto
# Aprendizajes : tuplas y for
# Creditos : adaptacion de JCSP basado en "Invent with python" ed4 - cap. 4
# https://inventwithpython.com/invent4thed/chapter4.html
# Fecha JCSP 2024 10 08
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es
from time import sleep
from random import randint

PAUSAFIN = 3 # 3 segundos de pausa
chistesTupla = (
"""
\tMarciano 1: Me invitarion a una fiesta de 15 años
\tMarciano 2: ¿Y vas a ir?
\tMarciano 1: Sí pero solo 3 horas, 15 años es mucho tiempo
""",               
"""
\tMarciano 1: Ayer vi a dos zombis contando chistes
\tMarciano 2: y que pasó
\tMarciano 1: Me reí mucho, zom-bien graciosos
""",
"""
\tMarciano 1: ¿Qué son 50 físicos y 50 químicos?
\tMarciano 2: No sé
\tMarciano 1: Son CIEN-tíficos
""",
# """
# \tMarciano 1: Aliennolo, ¿Vendes tu casa?
# \tMarciano 2: No, la al-kilo
# \tMarciano 1: y..... ¿cuanto pesa?
# """,
"""
\tMarciano 1: Ayer a la abuela le dió un infarto y le revisaron el corazón
\tMarciano 2: Latía?
\tMarciano 1: La tia no, la abuela, burro, la abuela
""")


titulo = 'CHISTES malos CONTADOS por 2 MARCIANOS'
print(titulo.capitalize())
print(len(titulo) * '=')
print()

# Empieza el bloque de chistes
for chiste in chistesTupla:
    print(chiste)
    print('ja' * randint(2,5))
    print('--------')
    sleep(PAUSAFIN)
    
print('Fin de los chistes')