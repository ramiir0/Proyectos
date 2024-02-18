from turtle import Turtle, Screen
from estados import Estados
import pandas


tortuga = Turtle()
pantalla = Screen()
pantalla.title("Adivina Mexico")
pantalla.setup(750, 550)
imagen = "/Proyecto mapa/mapa.gif"
pantalla.addshape(imagen)
tortuga.shape(imagen)

# """ NOTAAAAA     para saber la coordenada de la pantalla se usa la siguiente funcion"""
# def coordenada(x, y):
#     print(x, y)

datos = pandas.read_csv("Proyecto mapa/50_states.csv")


letrero = Estados()
total_estados = len(datos)

estados_faltantes = []          #en esta lista se guardaran todos los estados faltantes
lista_temporal =[]              #en esta lista voy agregando los estados que se van adivinando
estados = datos["state"]        #or estados = datos.state.to_list() otra forma de hacerlo lista
contador = 0
jugando = True
while jugando:
    respuesta_user = pantalla.textinput(f"{contador}/{total_estados} Estados correctos", 
                                        prompt="introduce un nombre de un estado").title()
    if respuesta_user == "Exit":
        for comparador in estados:
            if comparador not in lista_temporal:
                estados_faltantes.append(comparador)
        archivo = pandas.DataFrame(estados_faltantes)
        archivo.to_csv("/Proyecto mapa/estados.csv")
        break
        
    if respuesta_user:
        letrero.nombres_estados(respuesta= respuesta_user)
        lista_temporal.append(respuesta_user)
        contador += 1

# pantalla.mainloop() #se comenta para cuando se escriba exit en el if pueda salir del programa

        # baseDeDatos = pandas.DataFrame(Datos)
        # print(baseDeDatos)
        # baseDeDatos.to_csv("informacion.csv")