

def alta_de_nuevo_producto(inventario):
    nombre_valido = False
    while not nombre_valido:
        try:
            nombre_herramienta = input("¿Cual es el nombre de la herramienta?: ").strip()
            if nombre_herramienta == "":
                raise ValueError("El nombre no puede estar vacio.")
            for producto in inventario:
                if nombre_herramienta.lower() == producto["herramienta"].lower():
                    raise ValueError("La herramienta ya existe en el inventario.")
            nombre_valido = True
        except ValueError as e:
            print(f"Error {e}")
            
    stock_valido = False
    while not stock_valido:
        try:
            cantidad_stock = int(input("Con cuanto stock cuenta: "))
            if cantidad_stock < 0:
                raise ValueError("El stock no puede ser negativo")
            stock_valido = True
        except ValueError as e:
            print(f"Error {e}")
    
    inventario.append({"herramienta": nombre_herramienta, "cantidad": cantidad_stock})
    print("Producto agregado con éxito.")
    