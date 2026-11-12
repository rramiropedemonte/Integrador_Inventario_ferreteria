from carga_de_herramientas import cargar_herramientas
from visualizar_inventario import visualizar_inventario
from consultar_stock import consultar_stock
from reporte_agotados import reporte_agotados
from alta_de_nuevo_producto import alta_de_nuevo_producto
from actualizar_stock import actualizar_stock

def main():
    inventario = []
    opcion = 0

    while opcion != 7:
        print("1. Cargar herramientas: ")
        print("2. Visualizar inventario: ")
        print("3. Consultar stock: ")
        print("4. Reporte de productos agotados: ")
        print("5. Alta de nuevo producto: ")
        print("6. Actualizar stock: ")
        print("7. Salir")
        try:
            opcion = int(input("Elija una opción: "))
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                visualizar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_de_nuevo_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion != 7:
                raise ValueError("Debe elegir un número entre 1/7")
            else:
                print("Saliendo del sistema de inventario... ¡Hasta pronto!")
        except ValueError as e:
            print(f"Error: {e}")



main()