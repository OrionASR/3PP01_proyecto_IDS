def ingresar():
    print("INGRESAR")

def mostrar():
    print("MOSTRAR")

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