class Queso {
    constructor(nombre, tipo, sabor) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.sabor = sabor;
    }

    describir() {
        return `El queso ${this.nombre} es un ${this.tipo} con un sabor ${this.sabor}.`;
    }
}

// Ejemplo de uso
const quesoCheddar = new Queso('Cheddar', 'duro', 'salado');
console.log(quesoCheddar.describir());