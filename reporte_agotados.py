

def reporte_agotados(inventario):
    if len(inventario) == 0:
        print("No hay productos cargados.")
    else:
        encontrado = False
        for producto in inventario:
            if producto["cantidad"] == 0:
                print(f"Producto agotado: {producto['herramienta']}")
                encontrado = True
        if encontrado == False:
            print("Todas las herramientas tienen stock disponible.")