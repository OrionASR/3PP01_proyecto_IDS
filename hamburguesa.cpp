#include <iostream>
#include <string>

class Hamburguesa {
public:
    Hamburguesa(std::string nombre, double precio)
        : nombre(nombre), precio(precio) {}

    void mostrarDetalles() {
        std::cout << "Hamburguesa: " << nombre << std::endl;
        std::cout << "Precio: $" << precio << std::endl;
    }

private:
    std::string nombre;
    double precio;
};

int main() {
    Hamburguesa hamburguesa1("Hamburguesa Clásica", 5.99);
    hamburguesa1.mostrarDetalles();

    Hamburguesa hamburguesa2("Hamburguesa Doble", 7.99);
    hamburguesa2.mostrarDetalles();

    return 0;
}