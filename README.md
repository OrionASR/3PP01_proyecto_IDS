# 3PP01_proyecto_IDS: 📦 Sistema de Gestión de Inventario 📦 <3
## (versión 1.40)

Un sistema de consola desarrollado en Python para gestionar el inventario de una tienda. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar) sobre productos, incluyendo validaciones de fechas y ordenamiento.

## 📋 Características

El sistema cuenta *(por ahora)* con las siguientes funcionalidades:

* **Ingresar Productos:** Registro de ID, nombre, precio, descripción, lote y fecha de caducidad.
    * *Validación automática:* Si la fecha ingresada es incorrecta, se asigna una fecha de caducidad por defecto (2 meses).
    * *Protección:* Evita IDs duplicados, entradas de datos incorrectas, etc.
* **Mostrar Inventario:** Listado completo de productos con formato legible.
* **Modificar Productos:** Edición selectiva de campos (puedes editar solo el precio y dejar el resto igual).
* **filtrar:** Permite acotar la lista de productos por **Precio, ID, o Fecha de Caducidad**.
* **Ordenar:** Ordenamiento de productos por ID utilizando el método de burbuja.
* **Borrar:** Eliminación de productos por su ID.
* **Buscar:** Busca productos por coincidencia en el nombre
* **Venta:**  Se simula el consumo del stock.
* **Reporte de ventas:** Se visualiza detalladamente todas las ventas realizadas. 
* **Kcarlos moment:** kcarlos se une al equipo por desision de la catedra. 
* **
* ***Persistencia:*** Los datos se mantienen en memoria durante la ejecución (Listas y Objetos).

## 🛠️ Requisitos
* Python **3.0** en adelante
* **No** requiere librerías externas (usa módulos nativos `os` y `datetime`).
