
from turtle import Turtle
from turtle import Screen
import random

class Comida(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("blue")
        self.speed("fastest")
        self.actualizar()
        
        
    def actualizar(self):
        #son los ejes de la pantalla, pero no se pone desde los "-300 a 300", esto para evitar los problemas de giro
        random_x = random.randint(-280, 280) 
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)