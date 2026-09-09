"""
Módulo: tarea.py

Responsabilidad: Encapsular estructura y validación de cada tarea
Funcionalidad: Implementar la clase “Tarea” con sus atributos y métodos para actualizar información y validación interna

"""

class TareaModel:
    def __init__(self, nombre: str, descripcion: str = "", fechaVencimiento: str = "", estado: str = "pendiente"):
        """
        Constructor de la clase Tarea.
        Constructor que asigna los valores a los atributos y ejecuta la validación de cada atributo. 
        Lanza un error si el estado ingresado no es válido.
        """
        if not nombre or not nombre.strip():
            raise ValueError("El nombre de la tarea no debe estar vacío.")

        self.nombre = nombre.strip()
        self.descripcion = descripcion.strip()
        self.fechaVencimiento = fechaVencimiento.strip()

        """ Se valida la restricción de "ENUM" del estado """
        estadosValidos = ['pendiente', 'en progreso', 'completada']
        estadoMinusc = estado.lower().strip()
        
        if estadoMinusc not in estadosValidos:
            raise ValueError(f"Estado no válido. Opciones validas: {estadosValidos}")
            
        self.estado = estadoMinusc



    def actualizarDetalles(self, nombre: str = None, descripcion: str = None, fechaVencimiento: str = None, estado: str = None) -> None:
        """
        Método para modificar de forma parcial o total los atributos de la tarea.
        validando nuevamente cada restricción de dominio.
        """
        if nombre is not None:
            if not nombre.strip():
                raise ValueError("El nombre de la tarea no puede estar vacío.")
            self.nombre = nombre.strip()
            
        if descripcion is not None:
            self.descripcion = descripcion.strip()
            
        if fechaVencimiento is not None:
            self.fechaVencimiento = fechaVencimiento.strip()
            
        if estado is not None:
            estadosValidos = ['pendiente', 'en progreso', 'completada']
            estadoMinusc = estado.lower().strip()
            if estadoMinusc not in estadosValidos:
                raise ValueError(f"Estado no válido. Opciones validas: {estadosValidos}")
            self.estado = estadoMinusc

    def __str__(self) -> str:
        """
        Método de formateo que convierte el objeto en una representación en texto clara.
        Para ser desplegada en la interfaz de usuario (CLI)
        """
        valido = "OK" if self.estado == "completada" else ("➔" if self.estado == "en progreso" else "X")
        return f"[{valido} {self.estado.upper()}] {self.nombre} (Vence: {self.fechaVencimiento})\n    Descripción: {self.descripcion}"