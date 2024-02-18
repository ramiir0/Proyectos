
#para usar twilio desde pythonanywhere, se tiene que usar la sig libreria twilio.http.http_client import TwilioHttpClient

import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

sid_twilio = "AC9755cfa4a995c8a4676acd379"
token_twilio = "adffd131de27ffb4b619fb75aaf"

latitud = 25.677186873805844
longitud = -184.41608778139233
api_key = "83d8bdd03171ba232d7777249"

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
    proxy_twilio = TwilioHttpClient()
    proxy_twilio.session.proxies={'https': os.environ['https_proxy']}
    cliente = Client(sid_twilio, token_twilio, http_client=proxy_twilio)
    mensaje = cliente.messages \
                     .create(
                     body="Ramiro no olvides tu ⛱☂️paraguas🌂 porque llovera en las proximas 12hrs",
                     from_='+138889', #numero que me asigno twilio
                     to='TU_NUM' #mi numero con el que me registre
    )
    print(mensaje.status) #para verificar que se mando correctamente el msj
    