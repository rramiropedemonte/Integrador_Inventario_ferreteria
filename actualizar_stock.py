

def actualizar_stock(inventario):
    if len(inventario) == 0:
        print("No hay stock para actualizar.")
    else:
        buscar_herramienta = input("Ingrese el nombre de la herramienta que quiere actualizar: ").strip()
        actualizado = False
        for producto in inventario:
            if buscar_herramienta.lower() == producto['herramienta'].lower():
                actualizado = True
                try:
                    nuevo_stock = int(input("Ingrese la nueva cantidad de stock: "))
                    if nuevo_stock >= 0:
                        producto['cantidad'] = nuevo_stock
                        print("El stock se actualizo correctamente.")
                        break
                    else:
                        print("El nuevo stock no puede ser negativo.")
                        break
                except ValueError as e:
                    print(f"Error {e}")
                    break
        if actualizado == False:
            print("La herramienta ingresada no existe en el registro.")