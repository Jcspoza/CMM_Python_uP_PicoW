# Taller Programación y Robótica en CMM BML – 2023 - Clase 30
# Resumen: Primeros pasos con una GUi simple como GUIzero
# Topicos nuevos: Uso de GUI´s
# Ref Tutorial : libro "Create Graphical User Interfaces with Python"
# Ref code : https://github.com/themagpimag/createguis
# Ref 2: https://lawsie.github.io/guizero/
# Fecha inicio 2024 03 22
# Licencia : CC BY-NC-SA 4.0
# Proyecto ch7-Destruye Puntos en Grid
# Version 1.0 

# IMPORTAR modulo GUIzero
from guizero import App, Text, Waffle
from random import randint

# Informative block - start
p_topic = "1st stepps with GUIzero"
p_project = "ch7-Destruye Puntos en Grid"
p_ref = "Libro GUIzero de Laura Sach"
p_version = "1.0"
p_keyLib = "guizero"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0- Constantes y Variables globales
GRID_SIZE = 5
Puntos = 0

# F- Functions
# F.1
def add_dot():
    """Añade un 'dot' aleatoriamente , solo siantes habia un cuadrado"""
    x, y = randint(0,GRID_SIZE-1), randint(0,GRID_SIZE-1)
    while board[x, y].dotty == True: # sale cuando . dotty == false es decir es un cuadrado
        x, y = randint(0,GRID_SIZE-1), randint(0,GRID_SIZE-1)
    board[x, y].dotty = True # Convierte en dot
    board.set_pixel(x, y, "red")
    
    velocidad = 1000
    if Puntos > 30:
        velocidad = 200
    elif Puntos > 20:
        velocidad = 400
    elif Puntos > 10:
        velocidad = 500
        
    TodosRed = True
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if board[x,y].color != "red":
                TodosRed = False
    if TodosRed:
        board.disable() # Mejora respecto al programa del Libro
        puntosW.value = "Has perdido! Puntos: " + str(Puntos)
    else:
        board.after(velocidad, add_dot) # llamada RECURSIVA
           
    
def destroy_dot(x, y):
    """ Destruye puntos clicados en board, lladada como callback y le pasa los parametros x e y"""
    global Puntos
    if board[x,y].dotty == True:
        board[x,y].dotty = False
        board.set_pixel(x, y, "white")
        Puntos += 1				# Cuidado no escribir '=+ 1' porque eso no incrementa
        puntosW.value = "Puntos =" + str(Puntos)


# 1 - App 
apl = App("Destruye los Puntos")

# 2- wg#1 - Añade un widget Text 
instructiones = Text(apl, text="Clica los puntos para destruirlos")

# 3- wg#2 - Añade un widget Waffle
board = Waffle(apl, width=GRID_SIZE, height=GRID_SIZE, command=destroy_dot)

# 4- wg#3 - Añade un widget Text 
puntosW = Text(apl, text= "Puntos =" + str(Puntos))

# 5 - Aranca el bucle de juego
board.after(1000, add_dot)

# 8- Fin App display
apl.display()