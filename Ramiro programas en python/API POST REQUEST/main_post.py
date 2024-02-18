
import requests
from datetime import datetime

##########   PASO 1         crear tu cuenta en pixela desde este codigo
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "ramiir0"
MY_TOKEN = "TOKEN_ID"
parametros_usuario = {
    "token": MY_TOKEN ,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# conexion = requests.post(url= PIXELA_ENDPOINT, json= parametros_usuario)
# print(conexion.text)  #se le agrega el .text para que te mande en texto si hay conexion exitosa

########   PASO 2      configuracion del grafico
grafico_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
configuracion_grafico = {
    "id":"grafico1",
    "name":"Grafico de Ciclismo",
    "unit": "Km",
    "type": "float",
    "color":"sora",
}
cabecera = {
    "X-USER-TOKEN": MY_TOKEN
}
grafico = requests.post(url=grafico_endpoint, json= configuracion_grafico, headers=cabecera)
print(grafico.text)


#######          PASO 3 Agregar pixeles o datos a tu grafico 
hoy = datetime.now()
hoy = hoy.strftime("%Y%m%d")
# print(hoy)
#v1/users/<username>/graphs/<graphID>
pixel_endpoint = f"{grafico_endpoint}/grafico1"
configuracion_pixel = {
    "date":"20240109",
    "quantity": "7.5",
    #pudiera ser de la siguiente manera:
    #"quantity":input("cuantos km recorriste hoy?"),
}
pixel = requests.post(url=pixel_endpoint, json=configuracion_pixel, headers=cabecera )
print(pixel.text)

###########             actualizar un pixel dependiendo de la fecha
actualizar_pixel_endpoint = f"{pixel_endpoint}/20240110"
pixel_actualizar = {
    "quantity":"30"
}
pixel = requests.put(url=actualizar_pixel_endpoint, json=pixel_actualizar, headers=cabecera)
print(pixel.text)

############ Eliminar un pixel del grafico
eliminar_pixel_endpoint = f"{pixel_endpoint}/20240110"
eliminar_pixel = requests.delete(url=eliminar_pixel_endpoint, headers=cabecera)
print(eliminar_pixel.text)