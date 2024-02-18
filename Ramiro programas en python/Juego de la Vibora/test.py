
from turtle import Turtle
from turtle import Screen

tortuga = Turtle()
pantalla = Screen()

def avanza():
    tortuga.forward(10)
    
def retrocede():
    tortuga.backward(10)

def izquierda():
    tortuga.left(5)

def derecha():
    tortuga.right(5)
    
def borrar():
    tortuga.reset()

    
pantalla.listen()           # se usa el metodo listen() para poder usar las funciones onkey
#pantalla.onkey(key="left", fun= avanza)            #onkey(key= "tecla", fun= lo que deseas que realicze) tambien se puede usar
#pantalla.onkey(key="right", fun= retrocede)         #tortuga.backward(10)
pantalla.onkey(key="Up", fun= izquierda) 
pantalla.onkey(key="Down", fun= derecha) 
pantalla.onkey(key="c", fun= borrar)
pantalla.exitonclick()