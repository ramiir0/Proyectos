
import pandas

data = pandas.read_csv("/Proyecto mapa/50_states.csv")
estados = data["state"]
# print(estados)
# estados = data[data.state == "California"]
# print(estados.x)
# total = len(data)
# print(total)

lista_estados = []
lista_estados.append(estados)
print(lista_estados)