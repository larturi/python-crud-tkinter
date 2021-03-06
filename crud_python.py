from tkinter import *
import tkinter.messagebox as tkmb
import sqlite3

####################################
########### CONSTANTES #############
####################################

DB_NAME = "Usuarios.sqlite"

####################################
########### APLICACION #############
####################################

root = Tk()
root.eval('tk::PlaceWindow . center')

root.title("Python CRUD")
root.maxsize(340, 380) 
root.minsize(340, 380) 

mi_frame = Frame(root)
mi_frame.pack()

####################################
########## FUNCIONES UX ############
####################################

def makeMenu():

    menu_barra = Menu(root)
    root.config(menu=menu_barra)

    menu_bd = Menu(menu_barra, tearoff=0)
    menu_bd.add_command(label="Conectar", command=conectarDB)
    menu_bd.add_command(label="Salir", command=salir)

    menu_borrar = Menu(menu_barra, tearoff=0)
    menu_borrar.add_command(label="Borrar campos", command=limpiarCampos)

    menu_crud = Menu(menu_barra, tearoff=0)
    menu_crud.add_command(label="Create", command=create)
    menu_crud.add_command(label="Read", command=read)
    menu_crud.add_command(label="Update", command=update)
    menu_crud.add_command(label="Delete", command=delete)

    menu_help = Menu(menu_barra, tearoff=0)
    menu_help.add_command(label="Licencia")
    menu_help.add_command(label="About")

    menu_barra.add_cascade(label="BBDD", menu=menu_bd)
    menu_barra.add_cascade(label="Borrar", menu=menu_borrar)
    menu_barra.add_cascade(label="CRUD", menu=menu_crud)
    menu_barra.add_cascade(label="Ayuda", menu=menu_help)

def labels():
    label_id = Label(mi_frame, text="Id:")
    label_id.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    label_nombre = Label(mi_frame, text="Nombre:")
    label_nombre.grid(row=1, column=0, sticky="w", padx=10, pady=10)

    label_apellido = Label(mi_frame, text="Apellido:")
    label_apellido.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    label_password = Label(mi_frame, text="Password:")
    label_password.grid(row=3, column=0, sticky="w", padx=10, pady=10)

    label_direccion = Label(mi_frame, text="Direccion:")
    label_direccion.grid(row=4, column=0, sticky="w", padx=10, pady=10)

    label_comentarios = Label(mi_frame, text="Comentarios:")
    label_comentarios.grid(row=5, column=0, sticky="w", padx=10, pady=10)

####################################
########## FUNCIONES BD ############
####################################

def conectarDB():
    
    try:
        connection_db = sqlite3.connect(DB_NAME)
        cursor_db = connection_db.cursor()
        cursor_db.execute(''' 
            CREATE TABLE USUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                APELLIDO VARCHAR(50),
                PASSWORD VARCHAR(50),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(100)
            )
        ''')
    
        tkmb.showinfo("BBDD", "BBDD creada con exito", icon='info')
    except:
        tkmb.showwarning("Atencion!", "La BBDD ya existe", icon='warning')

def salir():
    respuesta = tkmb.askquestion("Salir", "Estas seguro que quieres cerrar la aplicacion?", icon='question')

    if respuesta == "yes":
        root.destroy()

def limpiarCampos():
    my_id.set("")
    my_nombre.set("")
    my_apellido.set("")
    my_password.set("")
    my_direccion.set("")
    my_comentarios.delete(1.0, END)

def create():
    connection_db = sqlite3.connect(DB_NAME)
    cursor_db = connection_db.cursor()

    datos = my_nombre.get(), my_apellido.get(), my_password.get(), my_direccion.get(), my_comentarios.get("1.0", END)

    cursor_db.execute("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)", (datos))

    connection_db.commit()

    limpiarCampos()

    tkmb.showinfo("BBDD", "Registro insertado con exito")

def read():
    connection_db = sqlite3.connect(DB_NAME)
    cursor_db = connection_db.cursor()

    cursor_db.execute("SELECT * FROM USUARIOS WHERE ID = " + my_id.get())

    user = cursor_db.fetchall()

    if not user:
        tkmb.showinfo("BBDD", "No existe un usuario con ID " + str(my_id.get()))

    limpiarCampos()

    for usr in user:
        my_id.set(usr[0])
        my_nombre.set(usr[1])
        my_apellido.set(usr[2])
        my_password.set(usr[3])
        my_direccion.set(usr[4])
        my_comentarios.insert("1.0", usr[5])

    connection_db.commit()

def update():
    connection_db = sqlite3.connect(DB_NAME)
    cursor_db = connection_db.cursor()

    datos = my_nombre.get(), my_apellido.get(), my_password.get(), my_direccion.get(), my_comentarios.get("1.0", END)

    cursor_db.execute("UPDATE USUARIOS SET NOMBRE=?, APELLIDO = ?, PASSWORD = ?, DIRECCION = ?, COMENTARIOS = ? WHERE ID=" + 
    my_id.get(),(datos))

    connection_db.commit()

    tkmb.showinfo("BBDD", "Registro actualizado con exito")

def delete():

    connection_db = sqlite3.connect(DB_NAME)
    cursor_db = connection_db.cursor()

    cursor_db.execute("DELETE FROM USUARIOS WHERE ID=" + my_id.get())

    connection_db.commit()

    tkmb.showinfo("BBDD", "Registro eliminado con exito")

####################################
############## CAMPOS ##############
####################################

makeMenu()
labels()

my_id = StringVar() 
my_nombre = StringVar()
my_apellido = StringVar() 
my_password = StringVar() 
my_direccion = StringVar() 

input_id = Entry(mi_frame, textvariable=my_id)
input_id.grid(row=0, column=1, padx=10, pady=10)
input_id.config(fg="green")

input_nombre = Entry(mi_frame, textvariable=my_nombre)
input_nombre.grid(row=1, column=1, padx=10, pady=10)

input_apellido = Entry(mi_frame, textvariable=my_apellido)
input_apellido.grid(row=2, column=1, padx=10, pady=10)

input_password = Entry(mi_frame, textvariable=my_password)
input_password.grid(row=3, column=1, padx=10, pady=10)
input_password.config(show="*")

input_direccion = Entry(mi_frame, textvariable=my_direccion)
input_direccion.grid(row=4, column=1, padx=10, pady=10)

my_comentarios = Text(mi_frame, width=26, height=5)
my_comentarios.grid(row=5, column=1, padx=10, pady=10)

####################################
############# BOTONERA #############
####################################

botonera_frame = Frame(root)
botonera_frame.pack()

boton_create = Button(botonera_frame, text="Create", command=create)
boton_create.grid(row=1, column=0, sticky="w")

boton_read = Button(botonera_frame, text="Read", command=read)
boton_read.grid(row=1, column=2, sticky="w")

boton_update = Button(botonera_frame, text="Update", command=update)
boton_update.grid(row=1, column=3, sticky="w")

boton_delete = Button(botonera_frame, text="Delete", command=delete)
boton_delete.grid(row=1, column=4, sticky="w")

root.mainloop()
