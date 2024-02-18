
from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    
    def __init__(self,):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.nivel = 1
        self.actulizarPuntos()
        
        
    def actulizarPuntos(self):
        self.clear()
        self.write(f"Dificultad: {self.nivel}", self, align= "center", font=(FONT))

        
    def sumador_punto(self):
        self.nivel += 1
        self.actulizarPuntos()
        
        
    def mensajePerder(self):
        self.goto(0, 0)
        self.write(f"Game Over!!!", self, align= "center", font=("Courier", 30, "normal"))