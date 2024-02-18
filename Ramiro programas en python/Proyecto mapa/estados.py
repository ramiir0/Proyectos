
from turtle import Turtle, Screen
import pandas


class Estados(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.hideturtle()
        self.data = pandas.read_csv("/Proyecto mapa/50_states.csv")

    def nombres_estados(self, respuesta):
        self.estados = self.data["state"]
        # print(estado)
        for self.estado in self.estados:
            if respuesta == self.estado:
                self.goto(self.coordenada_x(), self.coordenada_y())
                self.write(respuesta, font=("Arial", 15,"normal"))

    def coordenada_x(self):
        self.estados1 = self.data[self.data.state == self.estado]
        self.eje_x = self.estados1.x
        return int(self.eje_x)

# solo se obtiene 
    def coordenada_y(self):
        self.estados2 = self.data[self.data.state == self.estado]
        self.eje_y = self.estados2.y
        return int(self.eje_y) 
    
