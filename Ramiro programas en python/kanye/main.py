from tkinter import *
# import requests
from pip._vendor import requests


def get_quote():

    status = requests.get(url="https://api.kanye.rest")
    print(status.status_code) #imprime el status actual de la solicitud enviada, verifica la conexion con el servidor
    status.raise_for_status()
    mensaje = status.json()
    respuesta = mensaje["quote"]
    print(respuesta)
    canvas.itemconfig(quote_text, text = respuesta)
    

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="PIS-EndPoints/kanye/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=" loading....", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="APIS-EndPoints/kanye/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()