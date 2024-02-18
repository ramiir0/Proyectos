
import datetime as dato
import smtplib
import pandas
import random
import os

def main():
    fecha_cumple()

def fecha_cumple():
    fecha_actual = dato.datetime.now() #dato es el objeto y con la fecha actual
    mes_actual = fecha_actual.month
    dia_actual = fecha_actual.day
    tupla_fecha = (mes_actual, dia_actual) # se empieza por el mes ya que en el archivo esta primero el mes
    archivo = pandas.read_csv("/birthdays.csv")
    archivo_cumple = {(archivo_dato["month"], archivo_dato["day"]):archivo_dato for (index, archivo_dato) in archivo.iterrows() }
    # print(tupla_fecha)
    
    if tupla_fecha in archivo_cumple:
        persona_cumple = archivo_cumple[tupla_fecha]
        sustitucion = "[NAME]"
        dir = f"/letter_{random.randint(1,3)}.txt"
        with open(dir) as cartas:
            nombre_carta = cartas.read()
            mensaje = nombre_carta.replace(sustitucion, persona_cumple["name"])

        correo_archivo = persona_cumple["email"]
        mi_correo = "ramiro.python.test@gmail.com"
        password = "mi_pass"
        with smtplib.SMTP("smtp.gmail.com") as conexion:
            conexion.starttls()        
            conexion.login(user=mi_correo, password= password)
            #ahora se enviara el correo
            conexion.sendmail(
                from_addr=mi_correo, to_addrs=correo_archivo,
                msg=f"Subject: Feliz Cumple C= ! \n\n {mensaje}")


main()