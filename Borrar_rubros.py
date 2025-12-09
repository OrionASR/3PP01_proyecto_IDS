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
