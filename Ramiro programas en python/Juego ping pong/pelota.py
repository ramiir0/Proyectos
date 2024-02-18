from turtle import Turtle, Screen
from cuerpo import Cuerpo
import time

""" aqui se crea una clase normal"""
# class Pelota(Turtle):
    
#     def __init__(self,posicion):
#         super().__init__()
#         self.shape("circle")
#         self.color("white")
#         self.penup()
#         self.goto(posicion)


""" aqui heredamos de la clase cuerpo con ya varios atributos, pero solo modificamos los que necesitamos, 
en este caso solo: shape y shapesize"""
class Pelota(Cuerpo):
    
    def __init__(self, posicion):
        super().__init__(posicion)
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.eje_x = 3   # son los valores de los pixeles con los que se movera
        self.eje_y = 3
        self.velocidadPelota = 0.1
        self.msj = "Perdiste, presiona Enter para continuar ......"
        self.pantalla = Screen()


    def movimiento(self):
        nuevo_x = self.xcor() + self.eje_x
        nuevo_y = self.ycor() + self.eje_y
        self.goto(nuevo_x, nuevo_y)
    
    def choqueArriba_y(self):
        self.eje_y *= -1   # self.eje_x = 3 * (-1)
        
    def choque_x(self):
        self.eje_x *= -1
        self.velocidadPelota /= 10 
        
    def fuera(self):
        self.goto(0,0)
        #cuando un jugador pierde se vuelve a la velocidad inicial 
        self.velocidadPelota = 0.1
        self.choque_x()
        
        
    pausa = False
    def continuar(self):
        global pausa
        pausa = False

        
    def pause(self):
        global pausa
        pausa = True
        while pausa:
            time.sleep(0.1)
            self.write(self.msj, align= "center", font=("Courier", 20, "normal"))
            if self.pantalla.onkeypress(key="Return", fun=self.continuar):
                pausa = False
                self.fuera()
            else:
                pass
