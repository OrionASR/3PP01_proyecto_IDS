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

productos = []

#Desarrollado por Marco Ortega
class Venta:
    def __init__(self, id_venta: int, items_vendidos: dict):
       
        self.id_venta = id_venta
        self.items_vendidos = items_vendidos 

    def obtener_total(self):
        total = 0 
        for item in self.items_vendidos:
            total += item.precio * self.items_vendidos[item]
        return total
    
    def obtenerSubtotales(self):
        subtotales = {}
        for item in self.items_vendidos:
            subtotales[item] = item.precio * self.items_vendidos[item]
        return subtotales

# Lista de ventas
ventas = []

#Funciones para interactuar con la listas de ventas
def agregar_venta(venta_nueva: Venta):
    ventas.append(venta_nueva)

