import os
from modelos import Item, productos

def clear():
    os.system("cls" if os.name == "nt" else "clear")
# 1. Función para filtrar por Precio leonel
def filtrar_por_precio():
    clear()
    print("|====================|")
    print("=== FILTRAR POR PRECIO ===")

    # Validación de entrada
    try:
        min_precio = float(input("Ingrese el precio mínimo: "))
        max_precio = float(input("Ingrese el precio máximo: "))
    except ValueError:
        print("\nERROR: Debes ingresar valores numéricos.")
        input("Presiona Enter para volver...")
        return
    
    print(f"\nBuscando productos entre ${min_precio} y ${max_precio}...\n")

    # Validación: productos existente
    if not productos:
        print("No hay productos cargados para filtrar.")
        input("\nPresiona Enter para continuar...")
        return

    encontrados = [p for p in productos if min_precio <= p.precio <= max_precio]
    if encontrados:
        print(f"Se encontraron {len(encontrados)} coincidencias:\n")
        for item in encontrados:
            try:
                print(item) 
            except:
                print(f"{item.nombre} - ${item.precio}")
    else:
        print("No hay productos en ese rango de precios.")

    input("\nPresiona Enter para continuar...")

def filtrar_por_id():
    print("Función para filtrar por ID (Pendiente)")
    input("\nPresiona Enter para continuar...")

def filtrar_por_fecha():
    print("Función para filtrar por Fecha de Caducidad (Pendiente)")
    input("\nPresiona Enter para continuar...")

def filtrado():
    opc = 1
    clear()

    while opc != 0:
        print("|====================|")
        print("===== MENÚ FILTRADO =====")
        print("1. Por Precio")
        print("2. Por ID de Producto")
        print("3. Por Fecha de Caducidad")
        print("0. Volver al Menú Principal")

        try:
            opc = int(input("\n--> Selecciona una opción: "))
        except ValueError:
            clear()
            print("|====================|")
            print("ERROR: Debes ingresar un número.\n")
            continue

        clear()
        print("|====================|")
        print(f"-----> OPCIÓN {opc} <-----\n")

        match opc:
            case 1:
                filtrar_por_precio()
            case 2:
                filtrar_por_id()
            case 3:
                filtrar_por_fecha()
            case 0:
                print("-----> VOLVIENDO AL MENÚ PRINCIPAL <-----")
            case _:
                print("-----> OPCIÓN NO DISPONIBLE <-----")


def ordenar():
    print("Función ordenar en Rubros.py")
clear()
    print("|====================|")
    print("====== ORDENAR PRODUCTOS ======")
    
    if not productos:
        print("No hay productos cargados para ordenar. ")
        input("\nPresiona Enter para continuar...")
        return
        
    opc_criterio = 0
    while opc_criterio not in [1, 2]:
        print("\nOrdenar por:")
        print("1. Nombre (Alfabético) ")
        print("2. Precio (Numérico) ")
        try:
            opc_criterio = int(input("\n--> Selecciona el criterio de ordenación: "))
        except ValueError:
            print("\nERROR: Debes ingresar un número (1 o 2). ")
            
    if opc_criterio == 0:
        return

    opc_sentido = 0
    while opc_sentido not in [1, 2]:
        print("\nSentido de la ordenación:")
        print("1. Ascendente (A-Z, Menor a Mayor) ")
        print("2. Descendente (Z-A, Mayor a Menor) ")
        try:
            opc_sentido = int(input("\n--> Selecciona el sentido: "))
        except ValueError:
            print("\nERROR: Debes ingresar un número (1 o 2). ")

    # Definir la clave (key) y el sentido (reverse)
    criterio = "nombre" if opc_criterio == 1 else "precio"
    sentido_descendente = (opc_sentido == 2)
    
    # Ordenar la lista global 'productos' in-place. 
    # Usamos getattr para acceder dinámicamente al atributo (nombre o precio).
    try:
        productos.sort(key=lambda p: getattr(p, criterio), reverse=sentido_descendente)
        print("\n✅ ¡Productos ordenados! Mostrando el resultado:\n")
        
        for item in productos:
            try:
                print(item) 
            except:
                print(f"{item.nombre} - ${item.precio}")
                
    except AttributeError:
        print(f"\nERROR: Los objetos 'Item' no tienen el atributo '{criterio}'. Asegúrate de que tu clase 'Item' lo tenga. 😥")
        
    input("\nPresiona Enter para continuar...")

def borrar():
    print("Función borrar en Rubros.py")


def Rubros_menu():
    opc = 1
    clear()

    while opc != 0:
        print("|====================|")
        print("===== MENU =====")
        print("1. Filtrado")
        print("2. Ordenar")
        print("3. Borrar")
        print("0. Salir")

        try:
            opc = int(input("\n--> "))
        except ValueError:
            clear()
            print("|====================|")
            print("ERROR: Debes ingresar un número.\n")
            continue

        clear()
        print("|====================|")
        print(f"-----> OPCIÓN {opc} <-----\n")

        match opc:
            case 1:
                filtrado()
            case 2:
                ordenar()
            case 3:
                borrar()
            case 0:
                print("-----> SALIENDO <-----")
            case _:
                print("-----> OPCIÓN NO DISPONIBLE <-----")


