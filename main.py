"""
Módulo: main.py
Responsabilidad: Controlar la interacción directa con el usuario a través de la consola / línea de comandos
Funcionalidad: Despliega un menú interactivo, captura entradas de teclado y muestra información según corresponda 

"""
from src.tarea import TareaModel
from src.gestor import GestorTareas


def mostrarMenu() -> None:
    """Muestra las opciones del menú principal."""
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("SISTEMA DE GESTIÓN DE TAREAS")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("1. Crear Tarea")
    print("2. Listar Todas las Tareas")
    print("3. Filtrar Tareas por Estado")
    print("4. Editar Tarea")
    print("5. Eliminar Tarea")
    print("6. Salir")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")


def main() -> None:
    # Se llama a el gestor de tareas
    gestor = GestorTareas()

    while True:
        mostrarMenu()
        opcion = input("Escriba una opción (1-6): ").strip()

        if opcion == "1":
            print("\n\n\n--- Crear Nueva Tarea ---")
            nombre = input("Nombre de la tarea *: ").strip()
            descripcion = input("Descripción: ").strip()
            fecha = input("Fecha de vencimiento (YYYY-MM-DD): ").strip()
            
            estadoInput = input("Estado (pendiente/en progreso/completada) [por defecto: pendiente]: ").strip()
            if not estadoInput:
                estadoInput = "pendiente"

            try:
                nuevaTarea = TareaModel(nombre, descripcion, fecha, estadoInput)
                gestor.agregarTarea(nuevaTarea)
                print(f"OK Tarea '{nombre}' creada exitosamente.")
            except (ValueError, TypeError) as e:
                print(f"X Error al crear la tarea: {e}")

        elif opcion == "2":
            print("\n\n\n--- Lista de Tareas ---")
            tareas = gestor.obtenerTareas()
            if not tareas:
                print("No hay tareas registradas.")
            else:
                for t in tareas:
                    print(t)

        elif opcion == "3":
            print("\n\n\n--- Filtrar Tareas por Estado ---")
            estadoFiltro = input("Ingrese el estado a filtrar (pendiente/en progreso/completada): ").strip()
            try:
                filtradas = gestor.filtrarXEstado(estadoFiltro)
                if not filtradas:
                    print(f"No se encontraron tareas con el estado '{estadoFiltro}'.")
                else:
                    for t in filtradas:
                        print(t)
                        
            except ValueError as e:
                print(f"X Error de filtro: {e}")

        elif opcion == "4":
            print("\n\n\n--- Editar Tarea ---")
            nombreActual = input("Nombre exacto de la tarea a editar: ").strip()
            tareaExistente = gestor.buscarXNombre(nombreActual)

            if not tareaExistente:
                print(f"=X No se encontró ninguna tarea con el nombre '{nombreActual}'.")
            else:
                print("\n(Presione ENTER sin escribir nada para mantener el valor actual):")
                nuevoNombre = input(f"Nuevo nombre [{tareaExistente.nombre}]: ").strip() or None
                nuevaDesc = input("Nueva descripción: ").strip() or None
                nuevaFecha = input(f"Nueva fecha [{tareaExistente.fechaVencimiento}]: ").strip() or None
                nuevoEstado = input(f"Nuevo estado [{tareaExistente.estado}]: ").strip() or None

                try:
                    gestor.actualizarTarea(
                        nombreActual=nombreActual,
                        nuevoNombre=nuevoNombre,
                        nuevaDescripcion=nuevaDesc,
                        nuevaFecha=nuevaFecha,
                        nuevoEstado=nuevoEstado
                    )
                    print("OK Tarea actualizada correctamente.")
                except ValueError as e:
                    print(f"X Error al actualizar: {e}")

        elif opcion == "5":
            print("\n\n\n--- Eliminar Tarea ---")
            nombreEliminar = input("Nombre de la tarea a eliminar: ").strip()
            if gestor.borrarTarea(nombreEliminar):
                print(f"OK Tarea '{nombreEliminar}' eliminada exitosamente.")
            else:
                print(f"X No se encontró la tarea '{nombreEliminar}'.")

        elif opcion == "6":
            print("\n¡Saliendo del Sistema de Gestión de Tareas!.")
            break
        else:
            print("X Opción inválida. Ingrese un número entre 1 y 6.")


if __name__ == "__main__":
    main()