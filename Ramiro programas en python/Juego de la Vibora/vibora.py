

from turtle import Turtle, Screen

CUERPO = [(0,0), (-20,0), (-40,0)]   #se pone como constante las posiciones del cuerpo completo 
DISTANCIA = 20   #la distancia siempre es la misma, si se quisiera modificar, se modifica desde aqui
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Vibora:
    
    def __init__(self) -> None:
        self.nueva_tortuga = []
        self.crear_vibora()
        self.cabeza = self.nueva_tortuga[0]
        
    
    def crear_vibora(self):
        for posicion_inicial in CUERPO:
            self.agregar_cuerpo(posicion_inicial)
            # tortuga = Turtle("square")
            # tortuga.color("white")
            # tortuga.penup()
            # tortuga.goto(posicion_inicial)
            # self.nueva_tortuga.append(tortuga)
    
    def agregar_cuerpo(self, posicion_inicial):
        tortuga = Turtle("square")
        tortuga.color("white")
        tortuga.penup()
        tortuga.goto(posicion_inicial)
        self.nueva_tortuga.append(tortuga)
            
            
    def extender(self):
        #extiende el cuerpo de la tortuga cada que va comiendo
        self.agregar_cuerpo(self.nueva_tortuga[-1].position())


    def move(self):
        for posicionCuerpo in range (len(self.nueva_tortuga)-1, 0, -1):
            nuevoEje_x = self.nueva_tortuga[posicionCuerpo -1].xcor()
            nuevoEje_y = self.nueva_tortuga[posicionCuerpo -1].ycor()
            self.nueva_tortuga[posicionCuerpo].goto(nuevoEje_x, nuevoEje_y)  #hasta aqui todo el cuerpo se mueve a la posicion (0,0)
        self.cabeza.forward(DISTANCIA) #la vibora avanza hacia adelante 
    
    
    def Up(self):
        if self.cabeza.heading() != DOWN:
            self.cabeza.setheading(UP)
        
    def Down(self):
        if self.cabeza.heading() != UP:
            self.cabeza.setheading(DOWN)
    
    def Left(self):
        if self.cabeza.heading() != RIGHT:
            self.cabeza.setheading(LEFT)
    
    def Right(self):
        if self.cabeza.heading() != LEFT:
            self.cabeza.setheading(RIGHT)