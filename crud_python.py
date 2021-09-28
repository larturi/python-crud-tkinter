from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.eval('tk::PlaceWindow . center')

root.title("Python CRUD")
root.maxsize(340, 380) 
root.minsize(340, 380) 

####################################
############### MENU ###############
####################################

menu_barra = Menu(root)
root.config(menu=menu_barra)

menu_bd = Menu(menu_barra, tearoff=0)
menu_bd.add_command(label="Conectar")
menu_bd.add_command(label="Salir")

menu_borrar = Menu(menu_barra, tearoff=0)
menu_borrar.add_command(label="Borrar campos")

menu_crud = Menu(menu_barra, tearoff=0)
menu_crud.add_command(label="Create")
menu_crud.add_command(label="Read")
menu_crud.add_command(label="Update")
menu_crud.add_command(label="Delete")

menu_help = Menu(menu_barra, tearoff=0)
menu_help.add_command(label="Licencia")
menu_help.add_command(label="About")

menu_barra.add_cascade(label="BBDD", menu=menu_bd)
menu_barra.add_cascade(label="Borrar", menu=menu_borrar)
menu_barra.add_cascade(label="CRUD", menu=menu_crud)
menu_barra.add_cascade(label="Ayuda", menu=menu_help)

mi_frame = Frame(root)
mi_frame.pack()

####################################
############## LABELS ##############
####################################

label_id = Label(mi_frame, text="Id:")
label_id.grid(row=0, column=0, sticky="w", padx=10, pady=10)

label_nombre = Label(mi_frame, text="Nombre:")
label_nombre.grid(row=1, column=0, sticky="w", padx=10, pady=10)

label_apellido = Label(mi_frame, text="Apellido:")
label_apellido.grid(row=2, column=0, sticky="w", padx=10, pady=10)

label_password = Label(mi_frame, text="Password:")
label_password.grid(row=3, column=0, sticky="w", padx=10, pady=10)

label_direccion = Label(mi_frame, text="Dirección:")
label_direccion.grid(row=4, column=0, sticky="w", padx=10, pady=10)

label_comentarios = Label(mi_frame, text="Comentarios:")
label_comentarios.grid(row=5, column=0, sticky="w", padx=10, pady=10)

####################################
############## CAMPOS ##############
####################################

input_id = Entry(mi_frame)
input_id.grid(row=0, column=1, padx=10, pady=10)
input_id.config(fg="green")

input_nombre = Entry(mi_frame)
input_nombre.grid(row=1, column=1, padx=10, pady=10)

input_apellido = Entry(mi_frame)
input_apellido.grid(row=2, column=1, padx=10, pady=10)

input_password = Entry(mi_frame)
input_password.grid(row=3, column=1, padx=10, pady=10)
input_password.config(show="*")

input_direccion = Entry(mi_frame)
input_direccion.grid(row=4, column=1, padx=10, pady=10)

text_comentarios = Text(mi_frame, width=26, height=5)
text_comentarios.grid(row=5, column=1, padx=10, pady=10)

####################################
############# BOTONERA #############
####################################

botonera_frame = Frame(root)
botonera_frame.pack()

boton_create = Button(botonera_frame, text="Create")
boton_create.grid(row=1, column=0, sticky="w")

boton_read = Button(botonera_frame, text="Read")
boton_read.grid(row=1, column=2, sticky="w")

boton_update = Button(botonera_frame, text="Update")
boton_update.grid(row=1, column=3, sticky="w")

boton_delete = Button(botonera_frame, text="Delete")
boton_delete.grid(row=1, column=4, sticky="w")

root.mainloop()
