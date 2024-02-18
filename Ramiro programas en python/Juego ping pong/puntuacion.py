from turtle import Turtle
from cuerpo import Cuerpo

class Marcador(Cuerpo):
    
    def __init__(self, posicion):
        super().__init__(posicion)
        self.hideturtle()
        self.anotacion = 0
        #al principio estaba aqui el tablero pero se mueve a cada funcion para que se actulice cuandos se manda a llamar
        self.write(self.anotacion, align= "center", font=("Courier", 80, "normal"))
        
        
    def puntoIzq(self):
        self.anotacion += 1
        self.clear()
        self.write(self.anotacion, align= "center", font=("Courier", 80, "normal"))
        
    def puntoDer(self):
        self.anotacion += 1
        self.clear()
        self.write(self.anotacion, align= "center", font=("Courier", 80, "normal"))