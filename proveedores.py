
import datos_proveedores
datos_proveedores.cargar_datos()

from datetime import date



import os
def limpiar_pantalla():
     os.system('cls')

def correo_valido():
    while True:
        correo_electronico = input("Ingrese su correo electrónico (no olvide utilizar @): ")
        
        if "@" in correo_electronico:
            return correo_electronico 
        else:
            print(" Error: El correo es inválido porque le falta el '@'. Intente de nuevo.")


def registrar_proveedor():
     print("Registrar nuevo provedor")
     id_proveedor=datos_proveedores.contador_proveedor
     fecha_hoy = date.today().strftime("%d/%m/%Y")
     nombre= input("Ingrese nombre de proveedor: ")
     telefono= int(input("Ingrese el numero de telefono: "))
     correo_electronico= correo_valido()
     localidad= input("Ingrese la localidad de donde proviene: ")
     provee_de= input("Ingrese producto/s que provee: ")
     print(f"Fecha de pedido registrada automáticamente: {fecha_hoy}")
     nuevo_proveedor={
          "id": id_proveedor,
          "nombre": nombre,
          "telefono": telefono,
          "correo_electronico": correo_electronico,
          "localidad": localidad,
          "provee_de": provee_de,
          "fecha_ultimo_pedido": fecha_hoy,


     }

     datos_proveedores.lista_proveedores.append(nuevo_proveedor)
     datos_proveedores.contador_proveedor +=1
     datos_proveedores.guardar_datos()
     print(f"\n✔️ Proveedor guardado con éxito. Su ID es: {id_proveedor}")

def listado_proveedores():
     print("\n Listado de proveedores")
     print("------------------------")

     if len(datos_proveedores.lista_proveedores) ==0:
          print("No hay registro en el sistema")
     else:
          print(f"{'ID':<4} | {'NOMBRE':<15} | {'TELÉFONO':<12} | {'CORREO':<25} | {'LOCALIDAD':<15} | {'PROVEE DE':<15}")
          print("-" * 98)
          for proveedor in datos_proveedores.lista_proveedores:
           print(f"{proveedor['id']:<4} | {proveedor['nombre']:<15} | {proveedor['telefono']:<12} | {proveedor['correo_electronico']:<25} | {proveedor['localidad']:<15} | {proveedor['provee_de']:<15}")

def buscar_proveedor():
     print("\n Buscar proveedor")
     proveedor_nombre= str(input("Ingrese el nombre o producto del proveedor que desea buscar: "))

     se_encuentra=False

     for proveedor in datos_proveedores.lista_proveedores:
        if proveedor ['nombre'] == proveedor_nombre or proveedor['provee_de']== proveedor_nombre:
               print(f"Proveedor encontrado: {proveedor['nombre']} | {proveedor['provee_de']} | {proveedor['id']} ")
               
               
               se_encuentra=True
               break
     if not se_encuentra:
               print ("Proveedor no encontrado, verifique su nombre y vuelva a intentarlo")


def actualizar_datos ():
    print("\nModificar datos del proveedor ")
    buscar_id_proveedor = input("Ingrese el nombre del proveedor o producto que provee: ")
    encontrado = False
    for proveedor in datos_proveedores.lista_proveedores:
     if proveedor['nombre']== buscar_id_proveedor or proveedor['provee_de'] == buscar_id_proveedor:
            encontrado = proveedor
            break 
    if encontrado:
        print(f"\nProveedor seleccionado:  ID: {proveedor['id']} | Nombre: {proveedor['nombre']} | Telefono: {proveedor['telefono']} | Provee de: {proveedor['provee_de']} | Localidad: {proveedor['localidad']}")
        print("1. Editar telefono de contacto")
        print("2. Editar productos que provee")
        opcion = input("Seleccione un dato a modificar: ")
        if opcion == "1":
                editar_telefono=input("Modifique el telefono: ")
                encontrado['telefono'] = editar_telefono
                print("Item modificado correctamente.")
        elif opcion == "2":
            editar_productos=input("Modifique el producto que ofrece: ")
            encontrado['provee_de'] = editar_productos
            print("Productos actualizados correctamente")
        else:
            print("Opción no válida.")
        datos_proveedores.guardar_datos()
    else:
        print("Proveedor no encontrado, verifique nombre de cliente o id.")
    return


def baja_proveedor():
    print("\n--- ELIMINAR AL PROVEEDOR DEL REGISTRO ---")
    borrar_dato = input("Ingrese el nombre o id del proveedor: ").lower()
    
    proveedor_encontrado = None
    
    for proveedor in datos_proveedores.lista_proveedores:
        if str(proveedor['id']) == borrar_dato or proveedor['nombre'].lower() == borrar_dato:
            proveedor_encontrado = proveedor
            break 
            
    if proveedor_encontrado:
        print(f"\n¿Está seguro que desea eliminar a '{proveedor_encontrado['nombre']}' (ID: {proveedor_encontrado['id']})?")
        print("1. Sí")
        print("2. No")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            datos_proveedores.lista_proveedores.remove(proveedor_encontrado)
            datos_proveedores.guardar_datos() 
            print("Proveedor eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print(" Error: No se encontró información con ese nombre o ID.")


def submenu_proveedores():
    while True:
        limpiar_pantalla()
        print("\n---REGISTRO DE PROVEDOR ---")
        print("a. Registrar proveedor")
        print("b. Ver registro de proveedores")
        print("c. Buscar proveedor")
        print("d. Actualizar datos")
        print("e. Dar de baja proveedor")
        print("o. Volver al menú principal")
        print("---------------------------------")
    
       
        opcion = input("Seleccione una opción: ").lower()  
        if opcion == "a":
            print("\n A continuación ingresar los datos solicitados : ")
            registrar_proveedor()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "b":
            print("\n Ver listado: ")
            listado_proveedores()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "c":
            print("\n Buscar provedor: ")
            buscar_proveedor()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "d":
            print("\n Actualizar datos de proveedor: ")
            actualizar_datos()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "e":
            print("\n Eliminar proveedor: ")
            baja_proveedor()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "o":
            print("\nVolviendo al menú principal...")
            break

