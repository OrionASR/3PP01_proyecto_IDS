# Lista de productos
productos = []
# Función por Pedro
def ingresar():
    print("===== INGRESAR PRODUCTO =====")
    id_producto = input("ID del producto: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    descripcion = input("Descripción: ")
    lote = input("Lote: ")
    fecha_caducidad = input("Fecha de Caducidad (DD/MM/AAAA): ")

    producto = {
        'id': id_producto,
        'nombre': nombre,
        'precio': precio,
        'descripcion': descripcion,
        'lote': lote,
        'fecha_caducidad': fecha_caducidad
    }
    
    productos.append(producto)
    
    print("\n✓ Producto ingresado exitosamente!")

# Función por Pedro
def mostrar():
    print("===== LISTA DE PRODUCTOS =====")
    if len(productos) == 0:
        print("No hay productos registrados.")
        print("|====================|\n")
        return
    
    for i, prod in enumerate(productos, 1):
        print(f"\n--- Producto {i} ---")
        print(f"ID: {prod['id']}")
        print(f"Nombre: {prod['nombre']}")
        print(f"Precio: ${prod['precio']:.2f}")
        print(f"Descripción: {prod['descripcion']}")
        print(f"Lote: {prod['lote']}")
        print(f"Fecha de Caducidad: {prod['fecha_caducidad']}")
    
    print(f"\nTotal de productos: {len(productos)}")
  

def modificar():
    print("MODIFICAR")

def ordenar():
    print("ORDENAR")

def borrar():
    print("BORRAR")



opc = 1 # variable de control de opciones

while opc!=0: #menú por Orión
    print("|====================|")
    print("===== MENU =====")
    print("0. Salir")
    print("1. Ingresar Producto")
    print("2. Mostrar")
    print("3. Modificar lo ingresado")
    print("4. Ordenar")
    print("5. Borrar")
    opc = int(input("----> "))
    print("|====================|")
    print("-----> OPCION: ", opc," <-----")

    match opc:
        case 0:
            print("-----> SALIENDO <-----")
        case 1:
            ingresar()
        case 2:
            mostrar()
        case 3:
            modificar()
        case 4:
            ordenar()
        case 5:
            borrar()
        case _:
            print("-----> OPCION NO DISPONIBLE <-----")