from main import *

global ct_web, ct_password, ct_user

def datos():
    print("jaja")
    # direccion = ct_web.get()
    # guardar(direccion)
    
def guardar(direccion):
    with open(f"Ruta_de_los_datos.txt", mode="w") as datos:
            datos.write(direccion)
        