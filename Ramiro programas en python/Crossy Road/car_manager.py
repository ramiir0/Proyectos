from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():
    
    def __init__(self):
        self.listaCarros = []
        self.velocidadCarro = STARTING_MOVE_DISTANCE


    def crearCarro(self):
        # con el while del main hara que se cicle 6 veces y cree un carro nuevo
        # esto hara que la tortuga tenga oportunidad de poder cruzar sin crear muchos obtaculos de manera rapida
        generar_carro = random.randint(0, 6) 
        if generar_carro == 1:
            nuevosCarros = Turtle("square")  
            nuevosCarros.penup()
            nuevosCarros.color(random.choice(COLORS))
            nuevosCarros.setheading(180)
            nuevosCarros.goto(x=300, y= self.posicion_y())  #posicion inicial de la tortuga
            nuevosCarros.shapesize(stretch_wid= 1, stretch_len=2)
            self.listaCarros.append(nuevosCarros)
    
    #posicion random de cada carro
    def posicion_y(self):
        eje_y = random.randint(-270, 270)
        return eje_y
    
    #funcion donde avanzan todos los carros 
    def avance_carros(self):
        for carro in self.listaCarros:  
            carro.forward(self.velocidadCarro)
        
    #incremento de velocidad de los carros cada que se cruza la meta
    def aumentoDificultad(self):
        self.velocidadCarro += MOVE_INCREMENT

