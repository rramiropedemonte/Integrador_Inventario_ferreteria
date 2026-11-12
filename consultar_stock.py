

def consultar_stock(inventario):
    if len(inventario) == 0:
        print("No hay productos para consultar.")
    else:
        buscar_herramienta = input("¿Que herramienta esta buscando? ").strip()
        encontrado = False
        for producto in inventario:
            if buscar_herramienta.lower() == producto["herramienta"].lower():
                print(f"La cantidad de stock es de: {producto["cantidad"]}")
                encontrado = True
                break
        if encontrado == False:
            print("El producto buscado no se encuentra registrado!!")