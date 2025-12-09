# ---------- Parte 2: Lógica de borrado / manipulación de datos ----------
# --- Responsable: fernanda ---

def borrar_por_rubro_logic(productos, opcion, valor_str):
    """
    Recibe la lista 'productos', la opción elegida, y el valor ingresado (string).
    Devuelve el número de elementos borrados.
    """
    antes = len(productos)

    if opcion == "1":
        # Borrar por ID (suponemos que p.id es comparable como str o int)
        productos[:] = [p for p in productos if str(p.id) != valor_str]

    elif opcion == "2":
        # Borrar por fecha de caducidad
        # (asume que p.fecha_caducidad es string "AAAA-MM-DD" o date; se compara como str)
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
# --- Responsable: Integrante C ---

from dataclasses import dataclass

@dataclass
class Producto:
    id: int
    nombre: str
    fecha_caducidad: str # idealmente 'YYYY-MM-DD' o datetime.date
    precio: float
    # puedes añadir más campos si lo necesitas

def clear():
    """
    Limpia la consola para mejorar la experiencia de usuario.
    Puedes adaptar esto a tu SO (cls o clear).
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
