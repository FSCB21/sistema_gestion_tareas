"""
Módulo: test_gestor.py
Descripción: Pruebas unitarias automatizadas para la clase GestorTareas.
"""
import unittest
from src.tarea import TareaModel
from src.gestor import GestorTareas


class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        """Seeds de la prueba, para asegurar que no falle se generan unas tareas previas"""
        self.gestor = GestorTareas()
        self.t1 = TareaModel("Comprar leche", "Tambien es necesario comprar huevos", "2026-09-15", "pendiente")
        self.t2 = TareaModel("Trabajar hasta tarde", "Para tener dinero es necesario trabajar", "2026-09-20", "completada")
        self.t3 = TareaModel("Estudiar Maestria", "12 horas minimo a la semana.", "2026-09-10", "en progreso")

    def test_cp04_agregar_tarea_exito(self):
        """CP-04: Verificar que las tareas se agreguen correctamente a la colección."""
        self.gestor.agregarTarea(self.t1)
        self.assertEqual(len(self.gestor.obtenerTareas()), 1)
        self.assertIn(self.t1, self.gestor.obtenerTareas())

    def test_agregar_tarea_tipo_invalido(self):
        """Verificar que intentar agregar un objeto que no sea una Tarea lance ERROR."""
        with self.assertRaises(TypeError):
            self.gestor.agregarTarea("Esto no es una Tarea Valida")

    def test_agregar_tarea_nombre_duplicado(self):
        """Verificar que no se permitan tareas con nombres repetidos."""
        self.gestor.agregarTarea(self.t1)
        tareaRepetida = TareaModel("Comprar leche", "Y comprar arroz", "2026-09-25")
        with self.assertRaises(ValueError):
            self.gestor.agregarTarea(tareaRepetida)

    def test_cp05_obtener_todas_las_tareas(self):
        """CP-05: Verificar que se retornen todas las tareas creadas."""
        self.gestor.agregarTarea(self.t1)
        self.gestor.agregarTarea(self.t2)
        
        tareas = self.gestor.obtenerTareas()
        self.assertEqual(len(tareas), 2)

    def test_buscar_por_nombre(self):
        """Verificar la búsqueda por nombre."""
        self.gestor.agregarTarea(self.t1)
        
        encontrada = self.gestor.buscarXNombre("comprar LECHE")
        self.assertIsNotNone(encontrada)
        self.assertEqual(encontrada.nombre, "Comprar leche")
        
        inexistente = self.gestor.buscarXNombre("TareaModel Inexistente")
        self.assertIsNone(inexistente)

    def test_cp06_filtrar_por_estado_valido(self):
        """CP-06: Verificar el filtro correcto de tareas según su estado."""
        self.gestor.agregarTarea(self.t1)  # pendiente
        self.gestor.agregarTarea(self.t2)  # en progreso
        self.gestor.agregarTarea(self.t3)  # completada
        
        pendientes = self.gestor.filtrarXEstado("pendiente")
        self.assertEqual(len(pendientes), 1)
        self.assertEqual(pendientes[0].nombre, "Comprar leche")
        
        completadas = self.gestor.filtrarXEstado("completada")
        self.assertEqual(len(completadas), 1)
        self.assertEqual(completadas[0].nombre, "Trabajar hasta tarde")

    def test_filtrar_por_estado_invalido(self):
        """Verificar que filtrar por un estado no permitido genere ERROR."""
        with self.assertRaises(ValueError):
            self.gestor.filtrarXEstado("estado_desconocido")

    def test_cp07_actualizar_tarea_existente(self):
        """CP-07: Verificar la actualización exitosa de atributos de una tarea."""
        self.gestor.agregarTarea(self.t1)
        
        resultado = self.gestor.actualizarTarea(
            nombre_actual="Comprar leche",
            nuevo_estado="completada",
            nueva_descripcion="Mercado realizado!"
        )
        
        self.assertTrue(resultado)
        self.assertEqual(self.t1.estado, "completada")
        self.assertEqual(self.t1.descripcion, "Mercado realizado!")

    def test_cp08_actualizar_tarea_inexistente(self):
        """CP-08: Verificar que intentar actualizar una tarea que no existe retorne falso."""
        resultado = self.gestor.actualizarTarea(nombre_actual="Inexistente", nuevo_estado="completada")
        self.assertFalse(resultado)

    def test_cp09_eliminar_tarea(self):
        """CP-09: Verificar eliminar tareas existentes e inexistentes."""
        self.gestor.agregarTarea(self.t1)
        self.assertEqual(len(self.gestor.obtenerTareas()), 1)
        
        # Eliminación exitosa
        eliminada = self.gestor.borrarTarea("Comprar leche")
        self.assertTrue(eliminada)
        self.assertEqual(len(self.gestor.obtenerTareas()), 0)
        
        # Intento de eliminar tarea que ya fue removida
        no_eliminada = self.gestor.borrarTarea("Comprar leche")
        self.assertFalse(no_eliminada)


if __name__ == "__main__":
    unittest.main()