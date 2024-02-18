from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION) #posicion inicial de la tortuga
        self.shape("turtle")


    def arriba(self):
        self.forward(MOVE_DISTANCE)  #forma mas facil


    def cruce_meta(self):
        if self.ycor() > 290:
            return True
        else:
            return False
        
        
    def regreso_inicio(self):
        self.goto(STARTING_POSITION)        