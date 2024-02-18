from turtle import Turtle, Screen
from cuerpo import Cuerpo
from pelota import Pelota
from puntuacion import Marcador
import time


pantalla = Screen()
pantalla.setup(width= 800, height=600)
pantalla.title("Ping Pong")
pantalla.bgcolor("black")

#******************** todo esto se va a una clase *************************
pantalla.tracer(0)   #quita la animacion que tiene la tortuga de movimiento

    
tortuga = Turtle() #solo para usar el goto
pantalla.listen()


#posiciones de los objetos 
#posicion (x, y)
palaDerecha = Cuerpo((350, 0)) # se crea el objeto y se pone la posicion donde quieres que aparezca
palaIzquierda = Cuerpo((-350, 0))
balon = Pelota((0,0))
marcadorIzq = Marcador((-100, 200))
marcadorDer = Marcador((100, 200))

# pantalla.onkey(key="w", fun= avanza)  
pantalla.onkey(key= "Up", fun= palaDerecha.arriba)
pantalla.onkey(key= "Down", fun= palaDerecha.abajo)
pantalla.onkey(key= "w", fun= palaIzquierda.arriba)
pantalla.onkey(key= "z", fun= palaIzquierda.abajo)




#el while se pone para que la pantalla se este ciclando siempre
juego_corriendo = True
while juego_corriendo:
    time.sleep(balon.velocidadPelota)
    #se agrega la funcion update de manera manual para que se este ciclando con el while, esto se hizo porque
    # usamos la funcion tracer para quitar la animacion automatica.
    pantalla.update()
    #agregamos la funcion de movimiento dentro del while para que se este ciclando el movimiento
    balon.movimiento()
    
    paredArribaY = balon.ycor() > 290 #580
    paredAbajoY = balon.ycor() < - 290 #-580
    
    if paredArribaY or paredAbajoY:
        balon.choqueArriba_y()
    
    #para no poner separado los contactos con las paredes se puede poner en un solo if
    distancia_balon = balon.distance(palaDerecha) < 50  
    movimiento_x = balon.xcor() > 325        
    distancia2_balon = balon.distance(palaIzquierda) < 50
    movimiento2_x = balon.xcor() < -325

    if distancia_balon and movimiento_x or distancia2_balon and movimiento2_x:
        balon.choque_x()
        
        
    #si no hace contacto en una pala derecha
    if balon.xcor() > 380:
        #print("pego en la pared")  
        balon.fuera() 
        marcadorIzq.puntoIzq()
        balon.pause()


    #si no hace contacto en una pala izquierda
    if balon.xcor() < -380:
        balon.fuera()
        marcadorDer.puntoDer()
        balon.pause()


pantalla.exitonclick()
