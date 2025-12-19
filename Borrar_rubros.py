# y la parte 1?

# ---------- Parte 2: Lógica de borrado / manipulación de datos ----------

def borrar_por_rubro_logic(productos, opcion, valor_str):
    antes = len(productos)

    if opcion == "1":
        # Borrar por ID
        productos[:] = [p for p in productos if str(p.id) != valor_str]

    elif opcion == "2":
        # Borrar por fecha de caducidad
        productos[:] = [p for p in productos if str(p.fecha_caducidad) != valor_str]

    elif opcion == "3":
        # Borrar por precio exacto
        try:
            valor = float(valor_str)
        except ValueError:
            print("\nPrecio inválido — no se borró nada.\n")
            return 0

        productos[:] = [p for p in productos if p.precio != valor]

    return antes - len(productos)


# ---------- Parte 3: Datos, estructura y utilidades generales ----------

from dataclasses import dataclass

@dataclass
class Producto:
    id: int
    nombre: str
    fecha_caducidad: str
    precio: float

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
