

def visualizar_inventario(inventario):
    if len(inventario) == 0:
        print("El inventario no tiene productos registrados.")
    else:
        for producto in inventario:
            print(f"Herramienta: {producto['herramienta']} - Stock: {producto['cantidad']}")