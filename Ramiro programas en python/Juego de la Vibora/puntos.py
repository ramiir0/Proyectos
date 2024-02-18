
from turtle import Turtle

class TableroPuntos(Turtle):
    
    def __init__(self):
        super().__init__()
        self.puntos = 0 
        self.color("white")
        self.penup()
        self.goto(0, 275)     #posicion de la etiqueta de puntuacion
        self.write(f"Puntos {self.puntos}",align="center", font=("arial", 20, "normal"))
        self.hideturtle()
        #self.incrementos_puntos()
        
    def incrementos_puntos(self):
        self.puntos += 1
        self.clear()
        self.write(f"Puntos {self.puntos}",align="center", font=("arial", 20, "normal"))
        
    def game_over(self):
        self.goto(0, 0)     #posicion de la etiqueta de puntuacion
        self.write(f"GAME OVER", align="center", font=("arial", 40, "normal"))