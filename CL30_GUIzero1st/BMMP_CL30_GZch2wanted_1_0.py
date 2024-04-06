# Taller Programación y Robótica en CMM BML – 2023 - Clase 30
# Resumen: Primeros pasos con una GUi simple como GUIzero
# Topicos nuevos: Uso de GUI´s
# Ref Tutorial : libro "Create Graphical User Interfaces with Python"
# Ref code : https://github.com/themagpimag/createguis
# Ref 2: https://lawsie.github.io/guizero/
# Fecha inicio 2024 03 22
# Licencia : CC BY-NC-SA 4.0
# Proyecto ch2-wanted
# Version 1.0 

# IMPORTAR modulo GUIzero
from guizero import App, Text, Picture

# Informative block - start
p_topic = "1st stepps with GUIzero"
p_project = "ch2-wanted"
p_ref = "Libro GUIzero de Laura Sach"
p_version = "1.0"
p_keyLib = "guizero"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 1 - Una ventana para wanted
aplicacion = App(title="Wanted")
aplicacion.bg = "#1CE0D6"

# 2 - Añado widget Text
wanted_text = Text(aplicacion, "WANTED")
wanted_text.text_size = 50
wanted_text.font = "Bodoni MT"

# 3 - Añado widget Picture
cat = Picture(aplicacion, image="tabitha.png")

aplicacion.display()