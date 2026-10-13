#MENU PRINCIPAL 
from stock import submenu_plantas
from clientes import submenu_clientes
from ventas import submenu_ventas
from proveedores import submenu_proveedores
from encargos import submenu_encargos
import datos_stock
datos_stock.cargar_datos
import datos_clientes
datos_clientes.cargar_datos
import datos_ventas
datos_ventas.cargar_datos
import datos_proveedores
datos_proveedores.cargar_datos
import datos_encargos
datos_encargos.cargar_datos


import os

def limpiar_pantalla():
    os.system('cls')

def menu_principal():
    while True:
        limpiar_pantalla()
        print("\n ==========================================")
        print("   🌻🌱 VIVERO EL JACARANDÁ - MENÚ 🌸🌺🌵   ")
        print("   ==========================================")
        print(" ➡️  1. Stock de plantas")
        print(" ➡️  2. Clientes")
        print(" ➡️  3. Ventas")
        print(" ➡️  4. Proveedores")
        print(" ➡️  5. Encargos especiales")
        print(" ➡️  6. Salir")
        print("==================================")
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            print("====================================")
            print("\n 🌵Bienvenido al Stock de plantas") 
            print("===================================")
            submenu_plantas()
        elif opcion =="2":
            print("============================")
            print("\n 👥Bienvenido a Clientes ")
            print("============================")
            submenu_clientes()
        elif opcion == "3":
            print("==========================")
            print("\n 💰Bienvenido a Ventas")
            print("==========================")
            submenu_ventas()
        elif opcion == "4":
            print("===============================")
            print("\n 🚚Bienvenido a Proveedores")
            print("===============================")
            submenu_proveedores()
        elif opcion == "5":
            print("========================================")
            print("\n ⏳Bienvenido a Encargos especiales")
            print("========================================")
            submenu_encargos()
        elif opcion == "6":
            print("========================")
            print("\n Saliste del sistema✅")
            print("========================")
            break 
        else:
            print("\nOpción inválida. Por favor, vuelva a intentarlo")

menu_principal()