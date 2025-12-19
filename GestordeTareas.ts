//IMPORTANTE INSTALAR node.js ANTES DE EJECUTAR11!!!!

// 1. Definimos la estructura de una Tarea usando una Interface
interface Tarea {
    id: number;
    titulo: string;
    descripcion?: string; // El signo '?' hace que sea opcional
    completada: boolean;
    fechaCreacion: Date;
}

// 2. Creamos la clase que gestionará la lógica
class GestorDeTareas {
    private tareas: Tarea[] = [];
    private siguienteId: number = 1;

    /**
     * Agrega una nueva tarea a la lista.
     * @param titulo El título de la tarea
     * @param descripcion Descripción opcional
     */
    public agregarTarea(titulo: string, descripcion: string = ""): void {
        const nuevaTarea: Tarea = {
            id: this.siguienteId++,
            titulo,
            descripcion,
            completada: false,
            fechaCreacion: new Date()
        };
        this.tareas.push(nuevaTarea);
        console.log(`✅ Tarea agregada: "${titulo}" (ID: ${nuevaTarea.id})`);
    }

    /**
     * Marca una tarea como completada buscando por su ID.
     * @param id El ID de la tarea a completar
     */
    public completarTarea(id: number): void {
        const tarea = this.buscarTarea(id);
        
        if (tarea) {
            tarea.completada = true;
            console.log(`🎉 Tarea "${tarea.titulo}" completada.`);
        } else {
            console.error(`❌ Error: No se encontró la tarea con ID ${id}`);
        }
    }

    /**
     * Elimina una tarea de la lista.
     * @param id El ID de la tarea a eliminar
     */
    public eliminarTarea(id: number): void {
        const longitudInicial = this.tareas.length;
        this.tareas = this.tareas.filter(t => t.id !== id);

        if (this.tareas.length < longitudInicial) {
            console.log(`🗑️ Tarea con ID ${id} eliminada.`);
        } else {
            console.error(`❌ Error: No se pudo eliminar, ID ${id} no existe.`);
        }
    }

    /**
     * Muestra todas las tareas en la consola con formato.
     */
    public listarTareas(): void {
        console.log("\n--- LISTA DE TAREAS ---");
        if (this.tareas.length === 0) {
            console.log("(No hay tareas pendientes)");
            return;
        }

        this.tareas.forEach(tarea => {
            const estado = tarea.completada ? "[Completada]" : "[Pendiente]";
            const icono = tarea.completada ? "✅" : "⏳";
            console.log(`${icono} ID: ${tarea.id} | ${estado} ${tarea.titulo}`);
            if (tarea.descripcion) {
                console.log(`   └─ Desc: ${tarea.descripcion}`);
            }
        });
        console.log("-----------------------\n");
    }

    // Método helper privado para buscar
    private buscarTarea(id: number): Tarea | undefined {
        return this.tareas.find(t => t.id === id);
    }
}

// --- EJEMPLO DE USO ---

// 1. Instanciamos el gestor
const miGestor = new GestorDeTareas();

// 2. Agregamos tareas
miGestor.agregarTarea("Aprender TypeScript", "Estudiar interfaces y tipos básicos");
miGestor.agregarTarea("Hacer ejercicio", "30 minutos de cardio");
miGestor.agregarTarea("Comprar leche"); // Descripción opcional vacía

// 3. Listamos el estado inicial
miGestor.listarTareas();

// 4. Completamos una tarea
miGestor.completarTarea(1);

// 5. Eliminamos una tarea
miGestor.eliminarTarea(2);

// 6. Listamos el estado final
miGestor.listarTareas();