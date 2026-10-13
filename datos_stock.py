import json

lista_plantas =[]
contador_planta = 1


def guardar_datos():
    with open('datos_stock.json', 'w') as f:
        json.dump(lista_plantas, f, indent=4)

def cargar_datos():
    global lista_plantas, contador_planta
    try:
        with open('datos_stock.json', 'r') as f:
            lista_plantas = json.load(f)
            if lista_plantas:
                contador_planta = lista_plantas[-1]['id'] + 1
    except FileNotFoundError:
       lista_plantas =[]
       contador_planta = 1




