-- 1. Primero creamos al Padre
CREATE TABLE Clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100)
);

-- 2. Luego creamos al Hijo
CREATE TABLE Pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    producto VARCHAR(100),
    cliente_id INT, -- Esta columna guardará el ID del cliente
    
    -- Aquí definimos la FOREIGN KEY
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);

CREATE TABLE Tickets (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    nombre_cliente VARCHAR(50) NOT NULL UNIQUE,
    fecha_factura DATE DEFAULT(CURRENT_DATE);
    domicilio_factura VARCHAR(50) NOT NULL UNIQUE,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);

SELECT c.id, c.nombre, p.id, p.producto,
        t.fecha_factura, t.domicilio_factura
FROM Clientes c
INNER JOIN Pedidos p
    ON p.cliente_id = c.id
INNER JOIN Tickets t
    ON t.cliente_id = c.id;