import json
lista_proveedores =[]
contador_proveedor = 1
def guardar_datos():
    with open('datos_proveedores.json', 'w') as f:
        json.dump(lista_proveedores, f, indent=4)

def cargar_datos():
    global lista_proveedores, contador_proveedor
    try:
        with open('datos_proveedores.json', 'r') as f:
            lista_proveedores = json.load(f)
            if lista_proveedores:
                contador_proveedor = lista_proveedores[-1]['id'] + 1
    except FileNotFoundError:
        lista_proveedores =[]
        contador_proveedor = 1