"""
Módulo: gestor.py
Responsabilidad: Administrar el conjunto de tareas y ejecutar 
operaciones sobre la colección de datos

Funcionalidad: Implementa la clase y las funciones del “gestor” 
para realizar la CRUD sobre la tarea,
también filtrar tareas según su estado.

"""
from typing import List, Optional
from src.tarea import TareaModel


class GestorTareas:

    def __init__(self):
        """Se genera el constructor del gestor con un array vacio de tareas."""
        self.tareas: List[TareaModel] = []

    def agregarTarea(self, tarea: TareaModel) -> None:
        """
        Añade una nueva tarea a la colección.
        Lanza ERROR de tipo si el objeto no es una instancia de Tarea.
        Lanza ERROR de value si ya existe una tarea con el mismo nombre.
        """
        if not isinstance(tarea, TareaModel):
            raise TypeError("El objeto a agregar debe ser un objeto de la clase Tarea.")

        if self.buscarXNombre(tarea.nombre) is not None:
            raise ValueError(f"Ya existe una tarea registrada con el nombre '{tarea.nombre}'.")

        self.tareas.append(tarea)

    def obtenerTareas(self) -> List[TareaModel]:
        """Retorna el arreglo completo de tareas registradas."""
        return self.tareas

    def buscarXNombre(self, nombre: str) -> Optional[TareaModel]:
        """
        Busca y retorna una tarea por su nombre.
        Retorna None si no la encuentra.
        """
        nombreMinusc = nombre.strip().lower()
        for tarea in self.tareas:
            if tarea.nombre.lower() == nombreMinusc:
                return tarea
        return None

    def filtrarXEstado(self, estado: str) -> List[TareaModel]:
        """
        Retorna una lista con las tareas que coinciden con el estado especificado.
        Lanza ERROR de value si el estado no es válido.
        """
        estadosValidos = ['pendiente', 'en progreso', 'completada']
        estadoMinusc = estado.strip().lower()

        if estadoMinusc not in estadosValidos:
            raise ValueError(f"Estado inválido. Opciones permitidas: {estadosValidos}")

        return [t for t in self.tareas if t.estado == estadoMinusc]

    def actualizarTarea(
        self,
        nombreActual: str,
        nuevoNombre: Optional[str] = None,
        nuevaDescripcion: Optional[str] = None,
        nuevaFecha: Optional[str] = None,
        nuevoEstado: Optional[str] = None
    ) -> bool:
        """
        Busca una tarea por su nombre actual y actualiza sus atributos.
        Retorna Verdadero si la tarea fue encontrada y actualizada.
        """
        tarea = self.buscarXNombre(nombreActual)
        if tarea is not None:
            tarea.actualizarDetalles(
                nombre=nuevoNombre,
                descripcion=nuevaDescripcion,
                fechaVencimiento=nuevaFecha,
                estado=nuevoEstado
            )
            return True
        return False

    def borrarTarea(self, nombre: str) -> bool:
        """
        Busca una tarea por su nombre y la borra de la colección.
        Retorna Verdadero si la eliminó.
        """
        tarea = self.buscarXNombre(nombre)
        if tarea is not None:
            self.tareas.remove(tarea)
            return True
            return False