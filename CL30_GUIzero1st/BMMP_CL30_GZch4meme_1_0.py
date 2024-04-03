# Taller Programación y Robótica en CMM BML – 2023 - Clase 30
# Resumen: Primeros pasos con una GUi simple como GUIzero
# Topicos nuevos: Uso de GUI´s
# Ref Tutorial : libro "Create Graphical User Interfaces with Python"
# Ref code : https://github.com/themagpimag/createguis
# Ref 2: https://lawsie.github.io/guizero/
# Fecha inicio 2024 03 22
# Licencia : CC BY-NC-SA 4.0
# Proyecto ch4-meme generator
# Version 1.0 

# IMPORTAR modulo GUIzero
from guizero import App, TextBox, Drawing, Combo, Slider

# Informative block - start
p_topic = "1st stepps with GUIzero"
p_project = "ch4-meme generator"
p_ref = "Libro GUIzero de Laura Sach"
p_version = "1.0"
p_keyLib = "guizero"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# F- Functions
# F.1
def draw_meme():
    meme.clear()
    meme.image(0, 0, "woodpecker.png")
    meme.text(
        20, 20, top_text.value, 
        color=color.value,
        size=size.value, 
        font=font.value)
    meme.text(
        20, 320, bottom_text.value,
        color=color.value,
        size=size.value,
        font=font.value,
        )

# 1 - App 
app = App("meme")

top_text = TextBox(app, "top text", command=draw_meme) # llama adraw_meme si cambia
bottom_text = TextBox(app, "bottom text", command=draw_meme) # llama adraw_meme si cambia

color = Combo(app,
              options=["black", "white", "red", "green", "blue", "orange"],
              command=draw_meme, selected="blue") # crea una drop-down list para elegir color

font = Combo(app,
             options=["times new roman", "verdana", "courier", "impact"],
             command=draw_meme) # crea una drop-down list para elegir fuente

size = Slider(app, start=20, end=50, command=draw_meme) # crea slider para elegir tamaño

meme = Drawing(app, width="fill", height="fill")

draw_meme()

app.display()