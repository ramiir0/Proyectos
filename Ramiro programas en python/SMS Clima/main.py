
import requests
from twilio.rest import Client

sid_twilio = "AC975695c8a4676acd379"
token_twilio = "adfffb4b619fb75aaf"
cliente = Client(sid_twilio, token_twilio)

latitud = 30.677186873805844
longitud = -163.41608778139233
api_key = "83d8bdd0332d7777249"

""" en la consulta normal arrojara el resultado de las proximas 12 hrs dividido en 3 horas por los 5 dias proximos
entonces como seran muchos datos, solo queremos los proximos 4 del dia de manana y usamos la opcion "cnt"
"""
parametros = {
    "lat": latitud,
    "lon":longitud,
    "appid":api_key,
    "cnt": 4, #este param es opcional, pero en vez de arrojarnos 40 datos de los 5 dias, solo arrojara 4 del dia 
}


conexion = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parametros)
conexion.raise_for_status()
datos = conexion.json()

lluvia =  False
for datos_hora in datos["list"]:
    condicion_clima = datos_hora["weather"][0]["id"]
    if int(condicion_clima) < 700:
        lluvia = True
if lluvia:
    # print("No olvides el paraguas, hoy llovera")
    mensaje = cliente.messages \
                     .create(
                     body="Ramiro no olvides tu ⛱☂️paraguas🌂 porque llovera en las proximas 12hrs",
                     from_='+138889', #numero que me asigno twilio
                     to='MI_NUM' #mi numero con el que me registre
    )
    print(mensaje.status) #para verificar que se mando correctamente el msj
    