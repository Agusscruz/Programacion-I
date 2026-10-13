import datos_ventas
datos_ventas.cargar_datos()
from datetime import date

import os
def limpiar_pantalla():
     os.system('cls')


def ingresar_ventas():
        print("Registrar venta")
        id_venta=datos_ventas.contador_venta
        cliente_dni= input("Ingresar DNI del cliente: ")
        cliente_comprador = input ("Cliente que realizó la compra: ")
        items_vendidos = input("Nombre de items vendidos: ")
        total_venta = float(input("Ingrese el total vendido de unidades: "))
        forma_pago = input("Ingrese el metodo de pago: ")
        fecha= date.today().strftime("%d/%m/%Y")
        print(f"Fecha de pedido registrada: {fecha}")

        nueva_venta={
             "id" : id_venta,
             "cliente_comprador" : cliente_comprador,
             "cliente_dni": cliente_dni,
             "items_vendidos" : items_vendidos,
             "total_venta" : total_venta,
             "forma_pago" : forma_pago,
             "fecha" : fecha,

             
        }

        datos_ventas.lista_ventas.append(nueva_venta) 
        datos_ventas.contador_venta += 1
        datos_ventas.guardar_datos()
        print(f"\n Venta guardada con éxito. Su ID es: {id_venta}")



def listado_ventas():
     print("------------------------")
     print ("\n Listado de Ventas ")
     print("------------------------")

     if len(datos_ventas.lista_ventas) ==0:
          print("No hay registros del sistema")
     else:
          print(f"{'ID':<4} | {'CLIENTE':<16} | {'DNI':<10} | {'TOTAL/ITEMS':<12} | {'FORMA PAGO':<12}")
          print("-" * 65)
          for venta in datos_ventas.lista_ventas:
               print(f"{venta['id']:<4} | {venta['cliente_comprador']:<16} | {venta['cliente_dni']:<10} | {venta['total_venta']:<12} | {venta['forma_pago']:<12}")

def buscar_venta():
     print("\n Buscar venta")
     venta_nombre=(input("Ingrese DNI del cliente o fecha de venta: "))

     se_encuentra=False

     for venta in datos_ventas.lista_ventas:
          if venta ['cliente_dni']== venta_nombre or venta ['fecha']== venta_nombre: 
               print(f"Venta encontrada: {venta['cliente_comprador']} | {venta['cliente_dni']} | {venta['items_vendidos']} ")
               
               se_encuentra=True
               break

     if not se_encuentra:
               print ("Venta no encontrada, verifique su nombre y vuelva a intentarlo")



def modificar_venta():
    print("\nModificar datos de venta ")
    buscar_id_cliente = input("Ingrese el id o nombre del cliente que realizó la compra: ")
    encontrada = False
    for venta in datos_ventas.lista_ventas:
        if venta['id'] or venta['cliente_comprador'] == buscar_id_cliente:
            encontrada = venta
            break 
    if encontrada:
        print(f"\nVenta seleccionada:  ID: {venta['id']} | Cliente: {venta['cliente_comprador']} | Items: {venta['items_vendidos']} | Total: {venta['total_venta']} | Pago: {venta['forma_pago']}")
        print("1. Editar items vendidos")
        print("2. Editar forma de pago")
        opcion = input("Seleccione un dato a modificar:  ")
        if opcion == "1":
                items_modificados=input("Modifique el item: ")
                encontrada['items_vendidos'] = items_modificados
                print("Item modificado correctamente.")
        elif opcion == "2":
            editar_pago=input("Modifique el método de pago: ")
            encontrada['forma_pago'] = editar_pago
            print("Forma de pago actualizada correctamente")
        else:
            print("Opción no válida.")
        datos_ventas.guardar_datos()
    else:
        print("Venta no encontrada, verifique nombre de cliente o id.")
    
    return



def baja_venta():
    print("\n--- ELIMINAR EL REGISTRO DE VENTAS ---")
    borrar_dato = input("Ingrese el nombre del cliente o id de venta: ").lower()
    
    venta_encontrada = None
    
    for venta in datos_ventas.lista_ventas:
        if str(venta['id']) == borrar_dato or venta ['cliente_comprador'].lower() == borrar_dato:
            venta_encontrada = venta
            break 
            
    if venta_encontrada:
        print(f"\n¿Está seguro que desea eliminar a '{venta_encontrada['id']})?")
        print("1. Sí")
        print("2. No")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            datos_ventas.lista_ventas.remove(venta_encontrada)
            datos_ventas.guardar_datos() 
            print("Venta eliminada correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print(" Error: No se encontró información con ese nombre o ID.")


def submenu_ventas():
    while True:
        limpiar_pantalla()
        print("\n---STOCK DE VENTAS ---")
        print("a. Registrar nueva venta")
        print("b. Ver ventas efectuadas")
        print("c. Buscar venta")
        print("d. Modificar registro de venta")
        print("e. Elminar venta")
        print("o. Volver al menú principal")
        print("---------------------------------")
    
       
        opcion = input("Seleccione una opción: ").lower()  
        if opcion == "a":
            print("====================================================")
            print("\n A continuación ingresar los datos solicitados : ")
            print("====================================================")
            ingresar_ventas()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "b":
            print("================")
            print("\n Ver listado")
            print("================")
            listado_ventas()
            input("\nPresione ENTER para volver atrás...")

        elif opcion == "c":
            print("==================")
            print("\n Buscar encargo")
            print("==================")
            buscar_venta()
            input("\nPresione ENTER para volver atrás...")
        
        elif opcion == "d":
            print("============================")
            print("\n Modificar venta cargada")
            print("============================")
            modificar_venta()
            input("\nPresione ENTER para volver atrás...")

        elif opcion == "e":
            print("===================")
            print("\n Eliminar venta")
            print("===================")
            baja_venta()
            input("\nPresione ENTER para volver atrás...")

        elif opcion == "o":
            print("\nVolviendo al menú principal...")
            break