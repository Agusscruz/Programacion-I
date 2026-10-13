import datos_stock
datos_stock.cargar_datos()

import os
def limpiar_pantalla():
     os.system('cls')


def sector_valido():
    sector_aceptado= ("interior, exterior, invernadero, huerta")
    while True:
        sector_2 = input("Ingrese el sector donde puede permanecer: ")
        if sector_2 in sector_aceptado:
            return sector_2
        else:
            print(" El sector ingresado no es válido. Por favor, intente de nuevo.")


def ingresar_planta():
        print("Registro de Nueva Planta")
        id_planta=datos_stock.contador_planta
        nombre = input ("Ingrese su nombre cómun: ")
        nombre_cientifico = input("Ingrese su nombre cientifico: ")
        categoria = input("Ingrese que tipo de planta es: ")
        sector = sector_valido()
        stock= int(input("Ingrese la cantidad disponible: "))
        precio = float(input("Ingrese su precio: "))
        cuidados = (input("Ingrese los cuidados a tener: "))
        nueva_planta={
             "id" : id_planta,
             "nombre" : nombre,
             "nombre_cientifico" : nombre_cientifico,
             "categoria" : categoria,
             "sector" : sector,
             "precio" : precio,
             "cuidados" : cuidados,
             "stock" : stock,
        }
        datos_stock.lista_plantas.append(nueva_planta) 
        datos_stock.contador_planta += 1
        datos_stock.guardar_datos()
        print(f"\n Planta guardada con éxito. Su ID es: {id_planta}")



def buscar_planta():
    print("\n Buscar planta")
    planta_nombre = input("Ingrese el nombre comun o nombre cientifico de la planta que desea buscar: ").lower()

    se_encuentra = False

    for planta in datos_stock.lista_plantas:
        if planta['nombre'].lower() == planta_nombre or planta['nombre_cientifico'].lower() == planta_nombre: 
            print(f"🌿 Planta encontrada: ID: {planta['id']}")
            print(f"🌻 Nombre Comun: {planta['nombre']}")
            print(f"🔬 Nombre cientifico: {planta['nombre_cientifico']}")
            print(f"📂 Categoria: {planta['categoria']} ")
            print(f"🔍 Sector: {planta['sector']}")
            print(f"📦 Stock: {planta['stock']} ")
            print(f"💳Precio: ${planta['precio']}")
            print(f"💧 Cuidados: {planta['cuidados']}")
            se_encuentra = True
            break
    if not se_encuentra:
        print("Planta no encontrada, verifique su nombre y vuelva a intentarlo")


def actualizar_stock():
    print("\nActualizar Stock de plantas")
    id_buscado = int(input("Ingrese el ID de la planta que desea actualizar: "))
    encontrada = False
    for planta in datos_stock.lista_plantas:
        if planta['id'] == id_buscado:
            encontrada = planta
            break 
    if encontrada:
        print(f"{planta['id']:<4} | {planta['nombre']:<12} | {planta['categoria']:<12} | {planta['sector']:<12} | ${planta['precio']:<7} | {planta['stock']:<5}")
        print("1. Cargar venta")
        print("2. Registrar planta muerta")
        print("3. Nuevo ingreso o nueva reproducción")
        opcion = input("Seleccione una opción: ")
        cantidad = int(input("Ingrese la cantidad a modificar: "))
        if opcion == "1" or opcion == "2":
            if cantidad <= encontrada['stock']:
                encontrada['stock'] -= cantidad
                print("Stock actualizado correctamente.")
                print(f"Su nuevo Stock es:  {encontrada ['stock']} ")
            else:
                print("Error: No hay suficiente stock.")
        elif opcion == "3":
            encontrada['stock'] += cantidad
            print("Stock actualizado correctamente.")
            print(f"Su nuevo Stock es:  {encontrada ['stock']} ")
        else:
            print("Opción no válida.")
        datos_stock.guardar_datos()
    else:
        print("Planta no encontrada, verifique el ID.")

def listado_plantas():
     print ("\n Registro y filtro de plantas")
     print("------------------------")
     print("\n--- LISTADO COMPLETO DE PLANTAS ---")
     if not datos_stock.lista_plantas:
        print("No hay registros en el sistema.")
        return
     print(f"{'ID':<4} | {'NOMBRE':<12} | {'CATEGORÍA':<12} | {'SECTOR':<12} | {'PRECIO':<8} | {'STOCK':<5}")
     print("-" * 65)
     for planta in datos_stock.lista_plantas:
      print(f"{planta['id']:<4} | {planta['nombre']:<12} | {planta['categoria']:<12} | {planta['sector']:<12} | ${planta['precio']:<7} | {planta['stock']:<5}")
     print("\n¿Desea filtrar este listado?")
     print("1. Filtrar por Sector")
     print("2. Filtrar por categoría")
     opcion = input("Ingrese una opcion por favor: ")
     if opcion == "1":
          dato_filtro=input("Ingrese el sector (interior, exterior, invernadero, otro)")
          clave= "sector"
     elif opcion == "2":
          dato_filtro=input("Ingrese la categoria (árboles, arbustos, suculentas, aromáticas, frutales, ornamentales)")
          clave = "categoria"
     else:
          print ("Opcion invalida, verifique y vuelva a intentarlo: ")
          return
     encontrada = False
     print(f"\n--- Plantas encontradas en {clave} '{dato_filtro}' ---")
     
     for planta in datos_stock.lista_plantas:
          if planta.get(clave, "").lower() == dato_filtro:
               print(f"Id:{planta['id']} | Nombre:{planta['nombre']} | nombre_cientifico:{planta['nombre_cientifico']} | Categoria:{planta['categoria']} | Sector:{planta['sector']} | precio:{planta['precio']} | cuidados:{planta['cuidados']}  ")
               encontrada =True
     if not encontrada:
          print("No se encontraron plantas registradas")



def baja_planta():
    print("\n--- ELIMINAR EL REGISTRO DE PLANTAS ---")
    borrar_dato = input("Ingrese el nombre común o ID a eliminar: ").lower()
    
    planta_encontrada = None
    
    for planta in datos_stock.lista_plantas:
     
        if str(planta['id']) == borrar_dato or planta['nombre'].lower() == borrar_dato:
            planta_encontrada = planta
            break 
            
    if planta_encontrada:
        print(f"\n¿Está seguro que desea eliminar a '{planta_encontrada['nombre']}' (ID: {planta_encontrada['id']})?")
        print("1. Sí")
        print("2. No")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            datos_stock.lista_plantas.remove(planta_encontrada)
            datos_stock.guardar_datos()
            print("Planta eliminada correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Error: No se encontró información con ese nombre o ID.")
             

def submenu_plantas():
    while True:
        limpiar_pantalla()
        print("\n---STOCK DE PLANTAS ---")
        print("a. Ingresar planta")
        print("b. Ver listado de plantas")
        print("c. Buscar plantas")
        print("d. Actualizar Stock")
        print("e. Dar de baja registro de plantas")
        print("o. Volver al menú principal")
        print("---------------------------------")
    
       
        opcion = input("Seleccione una opción: ").lower()  
        if opcion == "a":
            print("====================================================")
            print("\nA continuación ingresar los datos solicitados: ")
            print("====================================================")
            ingresar_planta()
            input("\nPresione ENTER para volver atrás...")

        elif opcion == "b":
            print("=================")
            print("\n Ver listado ")
            print("=================")
            listado_plantas()
            input("\nPresione ENTER para volver atrás...")
            
        elif opcion == "c":
            print("=================")
            print("\n Buscar planta ")
            print("=================")
            buscar_planta()
            input("\nPresione ENTER para volver atrás...")

        elif opcion == "d":
            print("=====================")
            print("\n Actualizar Stock ")
            print("=====================")
            actualizar_stock()
            input("\nPresione ENTER para volver atrás...")
          
        elif opcion == "e":
             print("=====================")
             print("\n Eliminar planta ")
             print("=====================")
             baja_planta()
             input("\nPresione ENTER para volver atrás...")

        elif opcion == "o":
            print("\Volviendo al menu principal")
            break
        


     
