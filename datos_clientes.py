import json
lista_clientes =[]
contador_cliente = 1
def guardar_datos():
    with open('datos_clientes.json', 'w') as f:
        json.dump(lista_clientes, f, indent=4)

def cargar_datos():
    global lista_clientes, contador_cliente
    try:
        with open('datos_clientes.json', 'r') as f:
            lista_clientes = json.load(f)
            if lista_clientes:
                contador_cliente = lista_clientes[-1]['id'] + 1
    except FileNotFoundError:
        lista_clientes =[]
        contador_cliente = 1