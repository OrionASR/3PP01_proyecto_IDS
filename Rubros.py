# ===========================
#  Restruturado por Simmel y Juan Isaac
# ===========================

import os
from modelos import Item, productos
from readchar import readkey, key


# ---------------------------
# FUNCIONES BÁSICAS
# ---------------------------

def clear():
    return os.system("cls" if os.name == "nt" else "clear")

def pausa():
    while True:
        clear()
        print("Presiona 'Enter' para continuar...", end="")
        tecla = readkey()
        if tecla == key.ENTER: break


# ===========================
#   2.1 FILTRADO
# ===========================

def filtrar_por_precio():
    clear()
    print("=== FILTRAR POR PRECIO (LEONEL) ===")

    try:
        minimo = float(input("Precio mínimo: "))
        maximo = float(input("Precio máximo: "))
    except:
        print("ERROR: introduce números válidos.")
        pausa()
        return

    print("\nProductos encontrados:\n")
    for p in productos:
        if p.precio >= minimo and p.precio <= maximo:
            print(p)

    pausa()

def filtrar_por_id():
    clear()
    print("=== FILTRAR POR ID ===")

    try:
        buscar = int(input("Ingresa el ID: "))
    except:
        print("ERROR: ID inválido.")
        pausa()
        return

    encontrado = False
    for p in productos:
        if p.id == buscar:
            print("\nProducto encontrado:\n")
            print(p)
            encontrado = True
            break

    if not encontrado:
        print("\nNo se encontró un producto con ese ID.")

    pausa()

def filtrar_por_fecha():
    clear()
    print("=== FILTRAR POR FECHA (OMAR) ===")
    print("Formato: DD/MM/AAAA\n")

    fecha_min = input("Fecha mínima: ").strip()
    fecha_max = input("Fecha máxima: ").strip()

    print("\nProductos encontrados:\n")
    for p in productos:
        fecha = p.fechaCad.strip()
        if fecha >= fecha_min and fecha <= fecha_max:
            print(p)

    pausa()


def filtrado_menu():
    opcion = -1
    while opcion != 0:
        clear()
        print("===== MENÚ FILTRADO =====")
        print("1. Filtrar por Precio (Leonel)")
        print("2. Filtrar por ID")
        print("3. Filtrar por Fecha (Omar)")
        print("0. Regresar")

        try:
            opcion = int(input("\n--> "))

        except:
            opcion = -1

        else:
            match opcion:
                case 1:
                    filtrar_por_id()
                
                case 2:
                    filtrar_por_precio()
                
                case 3:
                    filtrar_por_fecha()
                
                case 0:
                    clear()
                    print("Saliendo del sub-módulo 'Filtrar'...")
                    pausa()
                
                case _:
                    clear()
                    print("Opción no disponible o desconocida.")


# ===========================
#   2.2 ORDENAR (JUAN ISAAC, YULIX, SANCHEZ)
# ===========================
def ordenar_por_id():
    productos.sort(key=lambda p: p.id)
    print("\nProductos ordenados por ID:\n")
    for p in productos: print(p)


#  ORDENAR POR ID JUAN ISAAC
def ordenar_por_fecha():
    productos.sort(key=lambda p: p.fechaCad)
    print("\nProductos ordenados por Fecha:\n")
    for p in productos: print(p)

def ordenar_por_precio():
    productos.sort(key=lambda p: p.precio)
    print("\nProductos ordenados por Precio:\n")
    for p in productos: print(p)


# -------- JUAN ISAAC: MENÚ ORDENAR --------
def ordenar_menu():
    opcion = -1
    while opcion != 0:
        clear()
        print("===== ORDENAR (Juan isaac) =====")
        print("1. Ordenar por ID")
        print("2. Ordenar por Fecha de Caducidad")
        print("3. Ordenar por Precio")
        print("0. Regresar")

        try:
            opcion = int(input("\n--> "))
        except:
            opcion = -1

        else:
            clear()

            match opcion:
                case 1:
                    ordenar_por_id()
                
                case 2:
                    ordenar_por_precio()
                
                case 3:
                    ordenar_por_fecha()
                
                case 0:
                    clear()
                    print("Saliendo del sub-módulo 'Ordenar'...")
                    pausa()
                
                case _:
                    clear()
                    print("Opción no disponible o desconocida.")

        pausa()


# ===========================
#   2.3 BORRAR (SANCHES, GERMAN, FERNANDA)
# ===========================

# -------- GERMAN: BORRAR POR ID --------
def borrar_por_id():
    clear()
    print("=== BORRAR POR ID ===")
    try:
        bus = int(input("ID a borrar: "))
    except:
        print("ID inválido.")
        pausa()
        return

    for p in productos:
        if p.id == bus:
            productos.remove(p)
            print("\nProducto borrado.")
            pausa()
            return

    print("\nProducto no encontrado.")
    pausa()


# -------- SANCHEZ BORRAR POR PRECIO --------
def borrar_por_precio():
    clear()
    print("=== BORRAR POR PRECIO ===")
    try:
        limite = float(input("Borrar productos con precio menor a: "))
    except:
        print("Valor inválido.")
        pausa()
        return

    productos[:] = [p for p in productos if p.precio >= limite]
    print("\nProductos eliminados.")
    pausa()


# -------- FERNANDA BORRAR POR FECHA --------
def borrar_por_fecha():
    clear()
    print("=== BORRAR POR FECHA ===")
    fecha = input("Fecha exacta (DD/MM/AAAA): ")

    productos[:] = [p for p in productos if p.fechaCad.strip() != fecha]
    print("\nProductos eliminados.")
    pausa()


# -------- GERMAN MENÚ BORRAR --------
def borrar_menu():
    opcion = -1
    while opcion != 0:
        clear()
        print("===== BORRAR =====")
        print("1. Borrar por ID")
        print("2. Borrar por Precio")
        print("3. Borrar por Fecha")
        print("0. Regresar")

        try:
            opcion = int(input("\n--> "))
        except:
            opcion = -1

        else:
            match opcion:
                case 1:
                    borrar_por_id()
                
                case 2:
                    borrar_por_precio()
                
                case 3:
                    borrar_por_fecha()
                
                case 0:
                    clear()
                    print("Saliendo del sub-módulo 'Borrar'...")
                    pausa()
                
                case _:
                    clear()
                    print("Opción no disponible o desconocida.")


# ===========================
#   MENÚ PRINCIPAL RUBROS (SIMMEL)
# ===========================

def Rubros_menu():
    opcion = -1

    while True:
        clear()
        print("===== RUBROS =====")
        print("1. Filtrar productos\
              \n2. Ordenar productos\
              \n3. Borrar productos")

        try:
            opcion = int(input("\n--> "))

        except:
            opcion = -1

        else:
            match opcion:
                case 1:
                    filtrado_menu()
                
                case 2:
                    ordenar_menu()
                
                case 3:
                    borrar_menu()
                
                case 0:
                    clear()
                    print("     Saliendo del módulo 'Rubros'...")
                    pausa()
                    break
                    
                case _:
                    clear()
                    print("Opción no disponible o desconocida.")
