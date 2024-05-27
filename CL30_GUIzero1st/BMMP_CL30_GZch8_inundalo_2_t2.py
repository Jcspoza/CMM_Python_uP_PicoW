# Taller Programación y Robótica en CMM BML – 2023 - Clase 30
# Resumen: Primeros pasos con una GUi simple como GUIzero
# Topicos nuevos: Uso de GUI´s
# Ref Tutorial : libro "Create Graphical User Interfaces with Python"
# Ref code : https://github.com/themagpimag/createguis
# Ref 2: https://lawsie.github.io/guizero/
# Fecha inicio 2024 03 22
# Licencia : CC BY-NC-SA 4.0
# Proyecto ch8-Puzzle Inundalo
# Version 2.0 : incluyo info + trazas y no mensajes

# IMPORTAR modulo GUIzero
from guizero import App, Waffle, Text, PushButton, info
import random


# Informative block - start
p_topic = "1st stepps with GUIzero"
p_project = "ch8-Puzzle Inundalo"
p_ref = "Libro GUIzero de Laura Sach"
p_version = "2.t2"
p_keyLib = "guizero"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0- Constantes y Variables globales
colores = ["white", "red", "green", "blue", "yellow", "magenta"]
tablero_lado = 14
moves_limite = 25
moves_hechos = 0
recorrido = [] # Lista para guardar las tuplas (x,y) del recorrido, se inicializa en cada llamada turno
sustituciones = [] # Lista para guardar celdas sustituidas y las que ha llegado a un limite de zona, se inicializa en cada llamada turno


# F- Functions
# F.1 - Recursively floods adjacent squares
def inunda(x, y, target, reemplazo):     # Algorithm from https://en.wikipedia.org/wiki/Flood_fill
    # traza 
    global recorrido, sustituciones
    recorrido.append((x, y))
    
    if target == reemplazo: # para le caso en que el color de reemplazo sea = 0,0. Evita errores
        return False
    
    if tablero.get_pixel(x, y) != target: # Check de fin de zona YA conquistada
        sustituciones.append(("SALGO" , x, y))
        return False
    
    tablero.set_pixel(x, y, reemplazo)
    sustituciones.append(( reemplazo , x, y))
        
    if y+1 <= tablero_lado-1:   # South
        inunda(x, y+1, target, reemplazo)
    if y-1 >= 0:            # North
        inunda(x, y-1, target, reemplazo)
    if x+1 <= tablero_lado-1:    # East
        inunda(x+1, y, target, reemplazo)
    if x-1 >= 0:            # West
        inunda(x-1, y, target, reemplazo)

# F.2 - Check whether all squares are the same to [0,0] 
def todos_cuadrados_iguales():
    cuadrados = tablero.get_all()
    if all(color == cuadrados[0] for color in cuadrados):
        return True
    else:
        return False
    
# F.3 - llena el tablero con colores aleatorios   
def llena_tablero():
    for x in range(tablero_lado):
        for y in range(tablero_lado):
            tablero.set_pixel(x, y, random.choice(colores))

# F.4 - inicializa la paleta con lo 6 colores
def init_paleta():
    for color in colores:
        paleta.set_pixel(colores.index(color), 0, color)

# F.6 - Comprueba si no hemso llego al final
def gana_check():
    
    global moves_hechos
    moves_hechos += 1
    moves_text.value = "Movimientos hechos=" + str(moves_hechos) + " ->Pulsa color de paleta"
    
    if moves_hechos < moves_limite:
        if todos_cuadrados_iguales():
            gana_text.value = "You win (-;)!"        
    else:
        gana_text.value = "Perdiste :("

# F.5 - 
def comienza_inunda(x, y):
    global recorrido, sustituciones # traza
    
    inunda_color = paleta.get_pixel(x,y)
    target = tablero.get_pixel(0,0)
    
    print(f'================ JUGADA #{moves_hechos} ================') # traza
    
    inunda(0, 0, target, inunda_color) # funcion recursiva
    # traza
    print("Recorrido ", recorrido)
    recorrido = []
    print("Sustituciones ", sustituciones)
    sustituciones = []
    # traza
    gana_check() # check de fin de juego


# 1 - App 
apl = App("Puzzle: ¡Inúndalo!")
tablero = Waffle(apl, width=tablero_lado, height=tablero_lado, pad=0) # pad especio entre cuadrados
paleta = Waffle(apl, width=6, height=1, dotty=True, command=comienza_inunda)
llena_tablero()
init_paleta()
gana_text = Text(apl)
moves_text = Text(apl)
apl.info("Instrucciones", """Clica en la Paleta de 6 colores el color elegido,
Los cuadrados adyacentes de ese color se convertiran en parte de la Inundación.
Repite el proceso hasta que consigas llenar el tablero de 14x14 o hagas 25 movimientos (limite)
""")

# 8- Fin App display
apl.display()