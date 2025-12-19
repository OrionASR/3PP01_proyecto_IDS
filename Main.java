import java.util.ArrayList; // Para la lista
import java.util.List;      // Interfaz de la lista
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Producto miProducto = Inventario.agregarProducto(scanner);

        System.out.println("\n¡Producto agregado con éxito!");
        miProducto.mostrarInfo();

        scanner.close();
    }
}

class Producto {
    // Atributos
    private String nombre;
    private String id;
    private String descripcion;
    private double precio;
    private String lote;
    private String fechaCaducidad;
    private int stock;

    // Constructor vacío
    public Producto() {
    }

    // Constructor con parámetros
    public Producto(String nombre, String id, String descripcion, double precio, String lote, String fechaCaducidad, int stock) {
        this.nombre = nombre;
        this.id = id;
        this.descripcion = descripcion;
        this.precio = precio;
        this.lote = lote;
        this.fechaCaducidad = fechaCaducidad;
        this.stock = stock;
    }

    // Metodo para mostrar la info del producto
    public void mostrarInfo() {
        System.out.println("\n[ID: " + id + "] Producto: " + nombre);
        System.out.println("Precio: $" + precio + " | Stock: " + stock);
        System.out.println("Lote: " + lote + " | Caducidad: " + fechaCaducidad);
    }
}

class Inventario {
    private List<Producto> lista_productos = new ArrayList<>();

    public Inventario(List<Producto> lista_productos) {
        this.lista_productos = lista_productos;
    }

    public static Producto agregarProducto(Scanner scanf) {
        System.out.println("\n--- Registro de Nuevo Producto ---");

        System.out.print("Nombre: ");
        String nombre = scanf.nextLine();

        System.out.print("ID: ");
        String id = scanf.nextLine();

        System.out.print("Descripción: ");
        String descripcion = scanf.nextLine();

        System.out.print("Precio: ");
        double precio = scanf.nextDouble();
        scanf.nextLine(); // Limpiamos el buffer (importante después de nextDouble)

        System.out.print("Lote: ");
        String lote = scanf.nextLine();

        System.out.print("Fecha de Caducidad (DD/MM/AAAA): ");
        String fecha = scanf.nextLine();

        System.out.print("Stock inicial: ");
        int stock = scanf.nextInt();
        scanf.nextLine(); // Limpiamos el buffer

        Producto nuevoProducto = new Producto(nombre, id, descripcion, precio, lote, fecha, stock);
        this.lista_productos.add(nuevoProducto);
        return nuevoProducto;
    }
}