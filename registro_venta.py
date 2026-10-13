# reportes.py
import datos_clientes
import datos_ventas

def ver_historial_cliente(cliente_dni):
    cliente_encontrado = None
    for cliente in datos_clientes.lista_clientes:
        if str(cliente['dni']) == str(cliente_dni):
            cliente_encontrado = cliente
            break            
    if not cliente_encontrado:
        print("❌ Cliente no encontrado.")
        return
    print(f"\n--- Historial de compras: {cliente_encontrado['nombre']} ---")
    compras = [v for v in datos_ventas.lista_ventas if str(v.get('cliente_dni')) == str(cliente_dni)]   
    if not compras:
        print("Este cliente aún no tiene ventas registradas.")
    else:
        for v in compras:
            print(f"- Total: ${v.get('total_venta', 0)}")