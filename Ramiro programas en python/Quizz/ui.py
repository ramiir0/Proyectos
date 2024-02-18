from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Gui:
    
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.puntos = 0
        self.ventana = Tk()
        self.ventana.title("Quizz")
        self.ventana.config(padx=20, pady=20, bg=THEME_COLOR)

        
        self.et_puntos = Label(text="Puntos: 0", background=THEME_COLOR, fg="white")
        self.et_puntos.grid(row=0, column=1, pady=20)
        
        self.porta_canvas = Canvas(width=300, height=250, bg="white")
        self.texto = self.porta_canvas.create_text(
            150, #posicion del texto en eje x
            125, #posicion del texto en eje y
            width=290,
            text="preguntas", 
            fill=THEME_COLOR,
            font=("Arial",20,"italic"))
        self.porta_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        imagen_ok = PhotoImage(file="/images/true.png")
        self.boton_bien = Button(image=imagen_ok, highlightthickness=0, command=self.boton_true)
        self.boton_bien.grid(row=2, column=0)
        
        imagen_false = PhotoImage(file="/images/false.png")
        self.boton_mal = Button(image=imagen_false, highlightthickness=0,command=self.boton_false )
        self.boton_mal.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.ventana.mainloop()
        
    
    def get_next_question(self):  #funcion para obtener la funcion next_question del archivo quiz_brain
        self.porta_canvas.config(bg="white") 
        if self.quiz.still_has_questions(): 
            self.et_puntos.config(text=f"puntos: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.porta_canvas.itemconfig(self.texto, text=q_text)
        else:
            self.porta_canvas.itemconfig(self.texto, 
                                        text= f"son todas las preguntas \npuntuacion final: {self.quiz.score}pts" )
            self.boton_mal.config(state="disabled")
            self.boton_bien.config(state="disabled")
            
        
    def boton_true(self):
        respuesta = self.quiz.check_answer("true")
        self.comparar_respuesta(respuesta)
        # self.get_next_question()
        
    def boton_false(self):
        respuesta = self.quiz.check_answer("false")
        # self.get_next_question()
        self.comparar_respuesta(respuesta)
        
    def comparar_respuesta(self, resp_user):
        respuesta = resp_user
        if respuesta == True:
            self.porta_canvas.config(bg="green")
        else:
            self.porta_canvas.config(bg="red")
        self.ventana.after(1000, self.get_next_question)