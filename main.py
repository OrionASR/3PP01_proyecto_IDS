"""
    No te vayas a cansar fer nmms
"""

import os
from datetime import datetime, timedelta

#Hecho por Karev: clase para los productos de la tienda
class Item:
    def __init__(self, nombre: str, id: int, descripcion: str, precio: float, lote: str, fecha_caducidad: str):
        self.nombre = nombre
        self.id = id
        self.desc = descripcion
        self.precio = precio
        self.lote = lote
        self.fechaCad = fecha_caducidad
        self.cantidad = 999
    
    def __str__(self):
        return f"({self.id}) - Producto: {self.nombre} | '{self.desc}'\
                \n | Precio: {self.precio} | Lote y fecha de caducidad: {self.lote}, {self.fechaCad}\
                \n | Stock disponible: {self.cantidad} |\n | "

# Lista de productos
productos = []

# Función por Pedro
def ingresar():
    print("=====/ INGRESAR PRODUCTO \\=====")
    try:
        id_producto = int(input("Ingresa el ID del nuevo producto: "))
        nombre = input("Ingresa el nombre del producto: ")
        precio = float(input("Ingresa el precio del producto: "))
        desc = input("Descripción: ")
        lote = input("Lote: ")
        fechaInput = input("Fecha de Caducidad (DDMMAAAA): ")
        
    except ValueError: #esta nueva excepción detecta errores para el ID y para el precio
        print("ERROR!: Ingresaste uno o más valores erroneos. Inténtalo de nuevo.")

    else:
        # Agregado por javier valida id duplicado
        if buscar(id_producto): 
            print(f"ERROR! Ya existe un producto de ID {id_producto}. Inténtalo de nuevo.")
            return
        
        # Hecho por Karev, para validar fecha 
        if fechaInput.isdigit() and len(fechaInput) == 8:
            fechaCad = f"{fechaInput[:2]}/{fechaInput[2:4]}/{fechaInput[4:]}"

        else:
            fechaNoFormat = datetime.now().date() + timedelta(weeks=8)
            fechaCad = fechaNoFormat.strftime("%d/%m/%Y")
            # ^^^ si ingresó una fecha erronea, se establecerá una fecha
            #     de caducidad default de 2 meses

        productos.append(Item(nombre, id_producto, desc, precio, lote, fechaCad))
        
        print("\nProducto registrado exitosamente!")

# Función por Pedro
def mostrar():
    print("MOSTRAR")
    print("=====/ LISTA DE PRODUCTOS \\=====")
    if not productos:
        print("\nNo hay productos registrados.\n")
        return
    
    for i, prod in enumerate(productos, 1):
        print(f"\n--- Producto {i} ---\
              \n{prod}")
    
    print(f"\n\nTotal de productos: {len(productos)}")

# Función por Karev
def buscar(id: int):
    if not productos: return None

    for p in productos:
        if p.id == id:
            return p
    return None

# Funcion por Danny  
def borrar():
    print("BORRAR")
    if len(productos) == 0:
        print("\nNo hay productos registrados\n")
        return
    
    try:
        id_borrar = int(input("Ingrese el ID del producto a borrar: "))

    except ValueError:
        print("ERROR! Tipo de dato para 'Product_ID' incorrecto")
    
    else:
        # Borrar producto por ID
        itemBorrar = buscar(id_borrar)
        if itemBorrar:
            productos.remove(itemBorrar)

            print(f"\n  ✓ Producto con ID {id_borrar} borrado exitosamente.")
        else:
            print(f"ERROR!: No se encontró un producto con ID {id_borrar}.")  # correccion por javier
  
# Función por Pavel
def modificar():
    print("MODIFICAR")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return
    
    try:
        id_buscar = int(input("Ingrese el ID del producto a modificar: "))
    
    except ValueError:
        print("ERROR! Tipo de dato para 'Product_ID' incorrecto")
    
    else:
        prodModificar = buscar(id_buscar)
        if prodModificar:
            print("\nProducto encontrado. Deje vacío cualquier campo para NO modificarlo.\n")
            
            nuevo_nombre = input(f"Nuevo nombre: ")
            nuevo_precio = input(f"Nuevo precio: ")
            nueva_desc = input(f"Nueva descripción: ")
            nuevo_lote = input(f"Nuevo lote: ")
            nueva_fecha_input = input(f"Nueva fecha de caducidad (DDMMAAAA): ")

            if nuevo_precio:
                try:
                    nuevo_precio = float(nuevo_precio)

                except ValueError:
                    print("ERROR! Tipo de dato para 'Product_Price' incorrecto.")
                    return
                
                else:
                    prodModificar.precio = nuevo_precio

            if nueva_fecha_input:
                try:
                    nueva_fecha_try = int(nueva_fecha_input)

                except ValueError:
                    print("ERROR! Tipo de dato para 'Product_ExpDate' incorrecto.")
                
                else:
                    if nueva_fecha_input.isdigit() and len(nueva_fecha_input) == 8:
                        nueva_fecha = f"{nueva_fecha_input[:2]}/{nueva_fecha_input[2:4]}/{nueva_fecha_input[4:]}"
                    else:
                        nueva_fecha_NoFormat = datetime.now().date() + timedelta(weeks=8)
                        nueva_fecha = nueva_fecha_NoFormat.strftime("%d/%m/%Y")

                    prodModificar.fechaCad = nueva_fecha

            if nuevo_nombre:
                prodModificar.nombre = nuevo_nombre
            if nueva_desc:
                prodModificar.desc = nueva_desc
            if nuevo_lote:
                prodModificar.lote = nuevo_lote
            
            print("\n   Producto modificado exitosamente!")
            return

        else:
            print(f"ERROR!: No se encontró un producto con ID {id_buscar}.")

# Función también por Danny
def ordenar():
    print("ORDENAR")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return
    
    # creamos una copia de la lista original para no modificar esta misma
    productosOrd = productos.copy()

    # usamos metodo burbuja
    for i in range(len(productosOrd)):
        for j in range(len(productosOrd)-1):
            if productosOrd[j].id > productosOrd[j+1].id: # intercambiamos orden de los productos
                productosOrd[j], productosOrd[j+1] = productosOrd[j+1], productosOrd[j]
        
    print("=====/ LISTA DE PRODUCTOS (ordenados) \\=====")
    for p in productosOrd: print(p)


#Función por Karev: limpiar pantalla
def clear():
    return os.system("cls" if os.name == "nt" else "clear")


        # ------------------ FUNCION MAIN ------------------ # 
def Main():
    opc = 1 # variable de control de opciones

    clear()
    while opc!=0: #menú por Orión
        print("|====================|")
        print("===== MENU =====\
              \n1. Ingresar Producto\
              \n2. Mostrar\
              \n3. Modificar lo ingresado\
              \n4. Ordenar\
              \n5. Borrar\
              \n0. Salir")
        
        try:
            opc = int(input(" \n    --> "))

        except ValueError:
            clear()
            print("|====================|\n")
            print("ERROR! Tipo de dato incorrecto. Inténtalo de nuevo.\n")

        else:
            print("|====================|")
            print(f"-----> OPCIÓN {opc} <-----")

            match opc:
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

                case 0:
                    print("-----> SALIENDO <-----")

                case _:
                    print("-----> OPCION NO DISPONIBLE <-----")

if __name__ == '__main__':
    Main()