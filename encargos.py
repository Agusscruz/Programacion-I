import datos_encargos
datos_encargos.cargar_datos()
from datetime import date

import os
def limpiar_pantalla():
     os.system('cls')




def estado_valido():
    estado_pedido1= ("Pendiente", "Entregado", "Cancelado")
    while True:
        estado = input("Ingrese estado del pedido (Pendiente, Entregado, Cancelado): ")
        if estado in estado_pedido1:
            return estado 
        else:
            print(" El estado ingresado no es válido. Por favor, intente de nuevo.")


def ingresar_encargo():
    print("Registrar encargo especial")
    id_encargo = datos_encargos.contador_encargo
    cliente_dueno = input("Cliente que realizó el encargo: ")
    provedor = input("Nombre de provedor al que se solicitó: ")
    producto_encargado = input("Ingrese el producto encargado: ")
    cantidad = int(input("Ingrese las unidades solicitadas: "))
    stock = int(input("Ingrese la cantidad disponible: "))
    sena_recibida = float(input("Ingrese monto de la seña: "))
    fecha_pedido = date.today().strftime("%d/%m/%Y")
    print(f"Fecha de pedido registrada: {fecha_pedido}")
    fecha_llegada = input("Ingrese fecha estimada de llegada (ej: 25/06/2026): ")
    estado_pedido = estado_valido()
    nueva_planta = {
         "id" : id_encargo,
         "cliente" : cliente_dueno,
         "provedor" : provedor,
         "producto_encargado" : producto_encargado,
         "cantidad" : cantidad,
         "stock" : stock,
         "sena_recibida" : sena_recibida,
         "fecha_pedido" : fecha_pedido,   
         "fecha_llegada" : fecha_llegada, 
         "estado" : estado_pedido,              
    }
    datos_encargos.lista_encargos.append(nueva_planta) 
    datos_encargos.contador_encargo += 1
    datos_encargos.guardar_datos()
    print(f"\n Encargo guardado con éxito. Su ID es: {id_encargo}")


def listado_encargos():
     print ("\n Listado de Encargos ")
     print("------------------------")

     if len(datos_encargos.lista_encargos) ==0:
          print("No hay registros del sistema")
     else:
          print(f"{'ID':<4} | {'CLIENTE':<15} | {'PROVEEDOR':<12} | {'PRODUCTO':<15} | {'CANT':<5} | {'STOCK':<5} | {'SEÑA':<7} | {'ESTADO':<10}")
          print("-" * 95)
          for encargo in datos_encargos.lista_encargos:
               print(f"{encargo['id']:<4} | {encargo['cliente']:<15} | {encargo['provedor']:<12} | {encargo['producto_encargado']:<15} | {encargo['cantidad']:<5} | {encargo['stock']:<5} | ${encargo['sena_recibida']:<6} | {encargo['estado']:<10}")

def buscar_encargo():
     print("\n Buscar encargo")
     encargo_nombre=(input("Ingrese el nombre del cliente o proveedor o fecha que desea buscar: "))

     se_encuentra=False

     for encargo in datos_encargos.lista_encargos:
          if encargo ['cliente_dueno'] ==encargo_nombre or encargo['provedor']== encargo_nombre or encargo['fecha_llegada'] == encargo_nombre:
               print(f"Encargo encontrado: {encargo['cliente']}")
               print(f"{encargo['provedor']}") 
               print(f"{encargo['planta_encargada']}")
               print(f"{encargo['fecha_llegada']} ")
               se_encuentra=True
               break

     if not se_encuentra:
               print ("Encargo no encontrado, verifique su nombre y vuelva a intentarlo")





def actualizar_estado ():
    print("\nModificar estado del encargo ")
    buscar_nombre_encargo = input("Ingrese el nombre del cliente o estado del producto: ")
    encontrado = False
    for encargo in datos_encargos.lista_encargos:
        if encargo['cliente'] == buscar_nombre_encargo or encargo['estado'] == buscar_nombre_encargo:
            encontrado = encargo
            break 
    if encontrado:
        print(f"\nEncargo seleccionado:  ID: {encargo['id']} | Cliente: {encargo['cliente']} | Provedor: {encargo['provedor']} | Producto encargado: {encargo['producto_encargado']} | Estado: {encargo['estado']}")
        
        editar_estado=input("Actualizar estado: ")

        encontrado['estado'] = editar_estado

        print("Estado actualizado correctamente.")
        datos_encargos.guardar_datos()
    else:
        print("Encargo no encontrado, verifique nombre de cliente o estado.")
    return



def baja_encargo():
    print("\n--- CANCELAR ENCARGO DEL REGISTRO ---")
    borrar_dato = input("Ingrese el nombre o id del encargo: ").lower()
    
    encargo_encontrado = None
    
    for encargo in datos_encargos.lista_encargos:
        if str(encargo['id']) == borrar_dato or encargo['cliente'] == borrar_dato:
            encargo_encontrado = encargo
            break 
            
    if encargo_encontrado:
        print(f"\n¿Está seguro que desea eliminar a '{encargo_encontrado['cliente']}' (ID: {encargo_encontrado['id']})?")
        print("1. Sí")
        print("2. No")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            datos_encargos.lista_encargos.remove(encargo_encontrado)
            datos_encargos.guardar_datos() 
            print("Encargo eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print(" Error: No se encontró información con ese nombre o ID.")




def submenu_encargos():
    while True:
        limpiar_pantalla()
        print("\n---STOCK DE ENCARGOS ---")
        print("a. Registrar encargo especial")
        print("b. Listar encargos activos")
        print("c. Buscar encargos")
        print("d. Actualizar estado de encargo")
        print("e. Cancelar encargo")
        print("o. Volver al menú principal")
        print("---------------------------------")
    
       
        opcion = input("Seleccione una opción: ").lower()  
        if opcion == "a":
            print("=====================================================")
            print("\n A continuación ingresar los datos solicitados : ")
            print("=====================================================")
            ingresar_encargo()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "b":
            print("=================")
            print("\n Ver listado")
            print("=================")
            listado_encargos()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "c":
            print("===================")
            print("\n Buscar encargo")
            print("===================")
            buscar_encargo()
            input("\nPresione ENTER para volver atrás...")

        elif opcion == "d":
            print("======================")
            print("\n Actualizar estado")
            print("======================")
            actualizar_estado()
            input("\nPresione ENTER para volver atrás...")

        elif opcion == "e":
            print("===================")
            print("\n Buscar encargo")
            print("===================")
            baja_encargo()
            input("\nPresione ENTER para volver atrás...")

        elif opcion == "o":
            print("\nVolviendo al menú principal...")
            break 