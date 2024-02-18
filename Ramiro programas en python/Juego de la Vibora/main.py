from turtle import Turtle, Screen
#/carp Vibora/ archivo vibora import clase Vibora
#from ..Vibora.vibora import Vibora   #importamos el archivo donde esta la clase Vibora
from vibora import Vibora
from comida import Comida
from puntos import TableroPuntos
import time

pantalla = Screen()
pantalla.setup(width= 600, height= 600)
pantalla.title("juego de la vibora")
pantalla.bgcolor("black")       #.bgcolor es el background color de fondo
pantalla.tracer(0)   #cuando se usa tracer se debe usar la funcion update 

miVibora = Vibora()
comida = Comida()
puntos = TableroPuntos()

pantalla.listen()
# pantalla.onkey(key="w", fun= avanza)  
pantalla.onkey(key="Up", fun= miVibora.Up)
pantalla.onkey(key="Down", fun= miVibora.Down)
pantalla.onkey(key="Left", fun= miVibora.Left)
pantalla.onkey(key="Right", fun= miVibora.Right) 

jugando = True
while jugando:
    pantalla.update()
    time.sleep(0.1)
    miVibora.move()
    
    #contacto con la comida
    if miVibora.cabeza.distance(comida) <15:  
        comida.actualizar()
        miVibora.extender()
        puntos.incrementos_puntos()
        
    #limites de pared, se pondran los limites por si la vibora choca en una de las 4 paredes
    #if miVibora.cabeza.xcor() > 280 or miVibora.cabeza.xcor() < -280 or miVibora.cabeza.ycor() > 280 or miVibora.cabeza.ycor() < -280:
    x_positivo = miVibora.cabeza.xcor() > 280
    x_negativo = miVibora.cabeza.xcor() < -280
    y_positivo = miVibora.cabeza.ycor() > 280
    y_negativo = miVibora.cabeza.ycor() < -280
    
    if x_positivo or x_negativo or y_positivo or y_negativo:
        jugando = False
        puntos.game_over()
        
    #si cabeza pega en la cola de la serpiente
    # for cuerpo in miVibora.nueva_tortuga: 
    #     if cuerpo == miVibora.cabeza:
    #         pass
    #     elif miVibora.cabeza.distance(cuerpo) < 10:
    #         jugando = False
    #         puntos.game_over()
    
    
    
    ## usano slacing 
    for cuerpo in miVibora.nueva_tortuga[1:]: 
        if miVibora.cabeza.distance(cuerpo) < 10:
            jugando = False
            puntos.game_over()
        
pantalla.exitonclick()