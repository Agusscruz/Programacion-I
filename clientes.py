import datos_clientes
datos_clientes.cargar_datos()

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



def registrar_cliente():
     print("Registrar nuevo cliente")
     id_cliente=datos_clientes.contador_cliente
     nombre= input("Ingrese su nombre completo: ")
     dni= input("Ingrese su número de DNI sin puntos: ")
     telefono= input("Ingrese su numero de telefono: ")
     correo_electronico=correo_valido()
     tipo_cliente= input("Ingrese una caracteristica del cliente:  ")
     nota= input("Detalle a tener en cuenta del cliente:  ")
     nuevo_cliente={
          "id": id_cliente,
          "nombre": nombre,
          "dni": dni,
          "telefono": telefono,
          "correo_electronico": correo_electronico,
          "tipo_cliente": tipo_cliente,
          "nota": nota,
     }
     datos_clientes.lista_clientes.append(nuevo_cliente)
     datos_clientes.contador_cliente +=1
     datos_clientes.guardar_datos()
     print(f"\n✔️ Cliente guardado con éxito. Su ID es: {id_cliente}")

def listado_clientes():
     print("\n Listado de clientes")
     print("------------------------")

     if len(datos_clientes.lista_clientes) ==0:
          print("No hay registro en el sistema")
     else:
          print(f"{'ID':<4} | {'NOMBRE':<16} | {'DNI':<10} | {'TELÉFONO':<12} | {'CORREO':<25} | {'TIPO':<12}")
          print("-" * 90)
          for cliente in datos_clientes.lista_clientes:
              print(f"{cliente['id']:<4} | {cliente['nombre']:<16} | {cliente['dni']:<10} | {cliente['telefono']:<12} | {cliente['correo_electronico']:<25} | {cliente['tipo_cliente']:<12}")

def buscar_cliente():
     print("\n Buscar cliente")
     cliente_nombre= str(input("Ingrese el nombre del cliente que desea buscar: "))

     se_encuentra=False

     for cliente in datos_clientes.lista_clientes:
        if cliente ['nombre'] == cliente_nombre or ['dni']== cliente_nombre:
               print(f"👩‍🌾 Cliente encontrado: {cliente['nombre']} ")
               print(f"👥 Dni del cliente:    {cliente['dni']}") 
               print(f"🤝 Id del cliente:     {cliente['id']}")
               
               se_encuentra=True
               return
     if not se_encuentra:
               print ("Cliente no encontrado, verifique su nombre y vuelva a intentarlo")


def actualizar_contacto():
    print("\nActualizar datos de contacto")
    buscar_dni_nombre = input("Ingrese el nombre o dni del cliente que desea actualizar: ")
    encontrado = False
    for cliente in datos_clientes.lista_clientes:
        if cliente['dni']== buscar_dni_nombre or  cliente['nombre'] == buscar_dni_nombre:
            encontrado = cliente
            break 
    if encontrado:
        print(f"\nCliente seleccionada/o: {encontrado['nombre']} | ID: {encontrado['id']} | telefono: {encontrado['telefono']} | correo: {encontrado['correo_electronico']} | tipo: {encontrado['tipo_cliente']} | nota: {encontrado['nota']}")
        print("1. Editar telefono")
        print("2. Editar correo")
        opcion = input("Seleccione un dato a modificar:  ")
        if opcion == "1":
                nuevo_telefono=input("Ingrese el nuevo telefono: ")
                encontrado['telefono'] = nuevo_telefono
                print("Telefono actualizado correctamente.")
        elif opcion == "2":
            nuevo_correo=input("Ingrese el nuevo correo: ")
            encontrado['correo_electronico'] = nuevo_correo
            print("Correo electronico actualizado correctamente.")
        else:
            print("Opción no válida.")
        datos_clientes.guardar_datos()
    else:
        print("Cliente no encontrada, verifique su nombre o dni.")
    return
    


def baja_cliente():
    print("\n--- ELIMINAR EL REGISTRO DE CLIENTES ---")
    borrar_dato = input("Ingrese el nombre o id del cliente: ").lower()
    
    cliente_encontrado = None
    
    for cliente in datos_clientes.lista_clientes:
        if str(cliente['id']) == borrar_dato or cliente['nombre'].lower() == borrar_dato:
            cliente_encontrado = cliente
            break 
            
    if cliente_encontrado:
        print(f"\n¿Está seguro que desea eliminar a '{cliente_encontrado['nombre']}' (ID: {cliente_encontrado['id']})?")
        print("1. Sí")
        print("2. No")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            datos_clientes.lista_clientes.remove(cliente_encontrado)
            datos_clientes.guardar_datos() 
            print("Cliente eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print(" Error: No se encontró información con ese nombre o ID.")




def submenu_clientes():
    while True:
        limpiar_pantalla()
        print("\n---REGISTRO DE CLIENTES ---")
        print("a. Registrar cliente")
        print("b. Ver registro de clientes")
        print("c. Buscar cliente")
        print("d. Actualizar datos de contacto")
        print("e. Eliminar cliente")
        print("o. Volver al menú principal")
        print("h. Consulte el historial de ventas")
        print("---------------------------------")
        opcion = input("Seleccione una opción: ").lower()  
        if opcion == "a":
            print("\n A continuación ingresar los datos solicitados: ")
            registrar_cliente()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "b":
            print("\n[Elegiste: Ver listado  ]")
            listado_clientes()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "c":
            print("\n Elegiste: Buscar cliente ")
            buscar_cliente()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "d":
            print("\n Elegiste: Actualizar datos de contacto ")
            actualizar_contacto()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "e":
            print("\n Elegiste: Eliminar cliente ")
            baja_cliente()
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "h":
            import registro_venta
            dni=input("Ingrese el DNI del cliente: ")
            registro_venta.ver_historial_cliente(dni)
            input("\nPresione ENTER para volver atrás...")
        elif opcion == "o":
            print("\nVolviendo al menú principal...")
            break





    