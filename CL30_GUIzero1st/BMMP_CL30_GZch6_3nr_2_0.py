# Taller Programación y Robótica en CMM BML – 2023 - Clase 30
# Resumen: Primeros pasos con una GUi simple como GUIzero
# Topicos nuevos: Uso de GUI´s
# Ref Tutorial : libro "Create Graphical User Interfaces with Python"
# Ref code : https://github.com/themagpimag/createguis
# Ref 2: https://lawsie.github.io/guizero/
# Fecha inicio 2024 03 22
# Licencia : CC BY-NC-SA 4.0
# Proyecto ch6-3 en Raya
# Version 2.0 : desabilita los pushbutton cuando se gana o se empata

# IMPORTAR modulo GUIzero
from guizero import App, Box, PushButton, Text

# Informative block - start
p_topic = "1st stepps with GUIzero"
p_project = "ch6-3 en Raya"
p_ref = "Libro GUIzero de Laura Sach"
p_version = "2.0"
p_keyLib = "guizero"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# F- Functions
# F.1 CAMBIA LA VARIABLE QUE LLEVA EL CARACTER QUE CORRESPONDE AL TURNO
def toggle_player():
    global turno
    if turno == "X":
        turno = "O"
    else:
        turno = "X"
    message.value = "Es tu turno, " + turno
    
def moves_taken():
    """ Cuenta las X o las O """
    moves = 0
    for row in board_squares:
        for col in row:
            if col.text == "X" or col.text == "O":
                moves = moves + 1
    return moves
   
def check_win():
    winner = None
    # Vertical lines
    if (
        board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text
    ) and board_squares[0][2].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (
        board_squares[1][0].text == board_squares[1][1].text == board_squares[1][2].text
    ) and board_squares[1][2].text in ["X", "O"]:
        winner = board_squares[1][0]
    elif (
        board_squares[2][0].text == board_squares[2][1].text == board_squares[2][2].text
    ) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[2][0]

    # Horizontal lines
    elif (
        board_squares[0][0].text == board_squares[1][0].text == board_squares[2][0].text
    ) and board_squares[2][0].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (
        board_squares[0][1].text == board_squares[1][1].text == board_squares[2][1].text
    ) and board_squares[2][1].text in ["X", "O"]:
        winner = board_squares[0][1]
    elif (
        board_squares[0][2].text == board_squares[1][2].text == board_squares[2][2].text
    ) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[0][2]

    # Diagonals
    elif (
        board_squares[0][0].text == board_squares[1][1].text == board_squares[2][2].text
    ) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (
        board_squares[2][0].text == board_squares[1][1].text == board_squares[0][2].text
    ) and board_squares[0][2].text in ["X", "O"]:
        winner = board_squares[0][2]

    if winner is not None:
        board.disable()
        message.value = winner.text + " wins!"
    elif moves_taken() == 9:
        board.disable()
        message.value = "Es un Empate"        
        
def clear_board():
    new_board = [[None, None, None], [None, None, None], [None, None, None]]
    for x in range(3):
        for y in range(3):
            button = PushButton(board, text="", grid=[x, y], width=3, command=choose_square, args=[x,y])
            new_board[x][y] = button
            
    return new_board

# F- BUCLE DE JUEGO
def choose_square(x, y):
    board_squares[x][y].text = turno
    board_squares[x][y].disable() # este cuadrado ya NO se puede volver a usar
    toggle_player()
    check_win() # CHECK DE SI HAY GANADOR O FIN, 


# 0 - Variables y constantes
turno = 'X'

# 1 - App 
app = App("Juego 3 en Raya")

# 2- wg#1 - Añade un Box
board = Box(app, layout="grid")

board_squares = clear_board() # Crea el Tablero

message = Text(app, text="Es tu turno, " + turno)

# 8- Fin App display
app.display()