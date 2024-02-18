
from tkinter import *
import math    

# ---------------------------- VAR------------------------------- #
tiempo = None
contador = 0
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
#reinciar todo a sus valores por defecto de inicio
def reinicio():
    global contador
    ventana.after_cancel(tiempo)
    et_timer.config(text="TIMER", bg="#9bdeac", foreground="#e7305b", font=(FONT_NAME, 40, "normal"))
    et_check.config(bg="#9bdeac", foreground="#e7305b", font=(FONT_NAME, 25, "normal"))
    porta_canvas.itemconfig(conteo, text="00:00") 
    contador = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
#como se quiere expresar el tiempo en formato: 12:55 se tiene que convertir en seg, por ejemplo 
#5min = 300 seg
def tiempo_inicio():  
    global contador
    contador += 1
                     # tiempo * 60 seg
    tiempo_trabajo = WORK_MIN * 60
    descanso_corto = SHORT_BREAK_MIN * 60
    descanso_largo = LONG_BREAK_MIN * 60
    if contador % 8 == 0:   
        et_timer.config(text="Descanso largo", fg=RED)
        #cada 4 pomodoros de 25 min es igual a un descanso largo, pero se suman
        #los 4 descansos cortos: 4 pomo + 4 descansos = 8
        cuenta_regresiva(descanso_largo)  
    elif contador % 2 == 0:
        et_timer.config(text="Descanso corto", fg=PINK)
        cuenta_regresiva(descanso_corto)
    else:
        et_timer.config(text="Trabajando", fg=PINK)
        cuenta_regresiva(tiempo_trabajo)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def cuenta_regresiva(segundos):  
    cont_minuto = math.floor(segundos/60)  
    cont_segundos = segundos % 60  #obtenemos el residuo para simular los segundos
    if cont_segundos < 10:
        cont_segundos = f"0{cont_segundos}"

    porta_canvas.itemconfig(conteo, text=f"{cont_minuto}:{cont_segundos}") 
    if segundos > 0:
        global tiempo
        tiempo = ventana.after(1000, cuenta_regresiva, segundos - 1)
    else:
        paloma = ""
        sesiones = math.floor(contador%2)
        for _ in range(sesiones):
            paloma += "✓"
        et_check.config(text=paloma)
        tiempo_inicio()


# ---------------------------- UI SETUP ------------------------------- #

ventana = Tk()
ventana.title("Pomodoro")
ventana.config(padx=100, pady=50, bg="#9bdeac")  

# highlightthickness es el grosor del borde de la imagen 
porta_canvas = Canvas(width=200, height=224, bg="#9bdeac", highlightthickness=0)  #tamaño de la imagen en pixeles
imagen_apple = PhotoImage(file="/tomato.png") #la funcion photoimage es de Tkinter
porta_canvas.create_image(100, 110, image=imagen_apple) 

conteo = porta_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
porta_canvas.grid(column=1, row=1)

et_timer = Label(text="TIMER", bg="#9bdeac", foreground="#e7305b", font=(FONT_NAME, 40, "normal"))
et_timer.grid(column=1, row=0)

et_check = Label(bg="#9bdeac", foreground="#e7305b", font=(FONT_NAME, 25, "normal"))
et_check.grid(column=1, row=4)

boton_inicio = Button(text="Inicio", highlightthickness=0, command=tiempo_inicio)
boton_inicio.grid(column=0, row=4)

boton_reset = Button(text="Reiniciar", highlightthickness=0, command=reinicio)
boton_reset.grid(column=4, row=4)


ventana.mainloop()