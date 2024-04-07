# Taller Programación y Robótica en CMM BML – 2023 - Clase 30
# Resumen: Primeros pasos con una GUi simple como GUIzero
# Topicos nuevos: Uso de GUI´s
# Ref Tutorial : libro "Create Graphical User Interfaces with Python"
# Ref code : https://github.com/themagpimag/createguis
# Ref 2: https://lawsie.github.io/guizero/
# Fecha inicio 2024 03 22
# Licencia : CC BY-NC-SA 4.0
# Proyecto ch3-spy
# Version 1.0 

# IMPORTAR modulo GUIzero
from guizero import App, Text, PushButton
from random import choice

# Informative block - start
p_topic = "1st stepps with GUIzero"
p_project = "ch3-spy"
p_ref = "Libro GUIzero de Laura Sach"
p_version = "1.0"
p_keyLib = "guizero"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# F- Functions
# F.1
def choose_name():
    print("Button was pressed")
    first_names = ["Rafa", "Fernando", "Begoña", "Jose", "Carlos", "Gema"]
    last_names = ["Garcia", "Perez", "Sanchez", "Gomez", "Anton", "Martin"]
    spy_name = choice(first_names) + " " + choice(last_names)
    print(spy_name)
    name.value = spy_name # no entiendo porque no hay que definirla como Global !!!

# 1 - Una ventana para TOP SECRET + TEXTO + BOTON
apl = App("TOP SECRET")

# 2- añado un widget Text
title = Text(apl, "Push the red button to find out your spy name")

# 3- añado un widget PushButton
button = PushButton(apl, choose_name, text="Tell me!")
button.bg = "red"
button.text_size = 30

# 4- añado un widget Text nuevo que se visualizara debajo del boton
name = Text(apl, text="") # se inicaliza con un texto vacio para la primera vez que se muestra

apl.display()