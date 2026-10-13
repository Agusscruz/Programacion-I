import json
lista_ventas =[]
contador_venta = 1
def guardar_datos():
    with open('datos_ventas.json', 'w') as f:
        json.dump(lista_ventas, f, indent=4)

def cargar_datos():
    global lista_ventas, contador_venta
    try:
        with open('datos_ventas.json', 'r') as f:
            lista_ventas = json.load(f)
            if lista_ventas:
                contador_venta = lista_ventas[-1]['id'] + 1
    except FileNotFoundError:
       lista_ventas =[]
       contador_venta = 1