import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Road!! ")
screen.tracer(0)
screen.listen()


jugador = Player()
jugador_win = Scoreboard()
cars = CarManager()



screen.onkey(key= "Up", fun= jugador.arriba)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.crearCarro()
    cars.avance_carros()
    
    #si hace contacto con un obstaculo
    for carro in cars.listaCarros:
        if carro.distance(jugador) < 25:
            game_is_on = False
            jugador_win.mensajePerder()


    # si llega a la meta, si cruza hasta el final
    if jugador.cruce_meta():
        jugador.regreso_inicio()
        jugador_win.sumador_punto()
        cars.aumentoDificultad()
        
screen.exitonclick()
