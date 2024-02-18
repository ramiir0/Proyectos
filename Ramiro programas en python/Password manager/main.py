from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle  
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generador_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    pass_letras = [choice(letters) for _ in range(randint(8, 10))]
    pass_numeros = [choice(numbers) for _ in range(randint(2, 4))]
    pass_simbolos = [choice(symbols) for _ in range(randint(2, 4))]
    
    password_list = pass_letras + pass_numeros + pass_simbolos

    shuffle(password_list)

    password = "".join(password_list)
    print(password)
    ct_password.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def agregar():
    direccion = ct_web.get()
    usuario = ct_user.get()
    password_user = ct_password.get()
    
    if len(direccion) == 0 or len(password_user) == 0 or len(usuario) == 0:
        messagebox.showinfo(title="Aviso", message="Tienes campos vacios")
    else:
        aceptar = messagebox.askokcancel(title=direccion, message=f"los datos son:\nDireccion: {direccion} \n"
                                                                f"Mail/Usuario: {usuario}")
        if aceptar:
            guardar(direccion, usuario, password_user)
            limpiar()
    
    
def guardar(direccion, usuario, password_user):
        with open(f"//Ruta_designada", mode="a") as datos:
            datos.write(f"Direccion web: {direccion} | Usuario: {usuario} | Password:{password_user} \n")

def limpiar():
    ct_web.delete(0, END)
    ct_password.delete(0,END)
    ct_web.focus()

# ---------------------------- UI SETUP ------------------------------- #

ventana = Tk()
ventana.title("Password Manager")
ventana.config(padx=50, pady=50)

porta_imagen = Canvas(width=200, height= 200)
logo = PhotoImage(file="logo.png")
porta_imagen.create_image(100, 100, image = logo)  
porta_imagen.grid(column=1, row=0)

#   --------- Etiquetas
et_web = Label(text="Website", font=("Arial", 15, "normal"))
et_web.grid(column=0, row=2)

et_user = Label(text="Email/Username", font=("Arial", 15, "normal"))
et_user.grid(column=0, row=3)

et_password = Label(text="Password", font=("Arial", 15, "normal"))
et_password.grid(column=0, row=4)

#   --------- Cajas Entrys
ct_web = Entry(width= 35)
ct_web.grid(column=1, row=2, columnspan= 2)
ct_web.focus()

ct_user = Entry(width= 35)
ct_user.grid(column=1, row=3, columnspan=2)
ct_user.insert(0, "ramiro.ignot@gmail.com")

ct_password = Entry(width=22)
ct_password.grid(column=1, row=4)

#   --------- Botones
bt_password = Button(text="Generar Password", command=generador_pass)
bt_password.grid(column=2, row=4)

bt_agregar = Button(text="Agregar", width=36, command=agregar)
bt_agregar.grid(column=1, row=5, columnspan=2)



mainloop()