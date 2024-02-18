from turtle import Turtle
import time

#heredaremos la clase Turtle para ya no crear un objeto tortuga
#  self.tortuga = Turtle()
# self.tortuga.shape("square")

class Cuerpo(Turtle):
    
    def __init__(self, posicion):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1) #cada cuadrado es de 20px por 20px, entonces lo alargamos 5 veces
        self.goto(posicion)

    def arriba(self):
        self.nueva_y = self.ycor() + 20    #le dice que se tiene que mover 20px 
        self.goto(self.xcor(), self.nueva_y) # en el goto se pone que la posicion "x",  sera fija y la "y" se estara moviendo
        
    def abajo(self):
        self.nueva_y = self.ycor() - 20
        self.goto(self.xcor(), self.nueva_y)
    
