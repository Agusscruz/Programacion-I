import json
lista_encargos =[]
contador_encargo = 1
def guardar_datos():
    with open('datos_encargos.json', 'w') as f:
        json.dump(lista_encargos, f, indent=4)

def cargar_datos():
    global lista_encargos, contador_encargo
    try:
        with open('datos_encargos.json', 'r') as f:
            lista_encargos = json.load(f)
            if lista_encargos:
                contador_encargo = lista_encargos[-1]['id'] + 1
    except FileNotFoundError:
        lista_encargos =[]
        contador_encargo = 1