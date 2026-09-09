"""
Módulo: test_tarea.py
Descripción: Pruebas unitarias automatizadas para la clase "TareaModel".
"""
import unittest
from src.tarea import TareaModel


class TestModeloTarea(unittest.TestCase):

    def test_cp01_creacion_tarea_estado_por_defecto(self):
        """CP-01: Validar que la tarea se cree con el estado por defecto 'pendiente'."""
        tarea = TareaModel("Probar tareas automaticamnete", "Las tareas se deben probar solas", "2026-09-28")
        
        self.assertEqual(tarea.nombre, "Probar tareas automaticamnete")
        self.assertEqual(tarea.descripcion, "Las tareas se deben probar solas")
        self.assertEqual(tarea.fechaVencimiento, "2026-09-28")
        self.assertEqual(tarea.estado, "pendiente")

    def test_cp02_validacion_estado_invalido(self):
        """CP-02: Verificar que instanciar con un estado no permitido genere ERROR."""
        with self.assertRaises(ValueError):
            TareaModel("Tarea con ERROR", "Descripción de una tarea con ERROR", "2026-09-28", estado="urgente")

    def test_cp03_actualizacion_exitosa_de_atributos(self):
        """CP-03: Verificar la actualización de los detalles de la tarea."""
        tarea = TareaModel("Una tarea de validacion", "Borrador inicial", "2026-09-25", estado="pendiente")
        
        """ Se actualiza únicamente el estado """
        tarea.actualizarDetalles(estado="en progreso")
        self.assertEqual(tarea.estado, "en progreso")
        
        """ Se actualiza tambien el nombre y fecha """
        tarea.actualizarDetalles(nombre="TareaModel completada", fechaVencimiento="2026-09-30")
        self.assertEqual(tarea.nombre, "TareaModel completada")
        self.assertEqual(tarea.fechaVencimiento, "2026-09-30")

    def test_actualizacion_estado_invalido_lanza_excepcion(self):
        """Verificar que al intentar actualizar a un estado inválido mantenga la regla de validacion del "ENUM"."""
        tarea = TareaModel("Test Estado", "Desc", "2026-09-20")
        with self.assertRaises(ValueError):
            tarea.actualizarDetalles(estado="desconocido")

    def test_validacion_nombre_vacio(self):
        """Verificar que no se permita crear una tarea con el nombre en blanco."""
        with self.assertRaises(ValueError):
            TareaModel("   ", "Descripción OKOK", "2026-09-20")

    def test_representacion_cadena(self):
        """Verificar que el método __str__ retorne el texto esperado."""
        tarea = TareaModel("Revisar código", "Revisión de PRs", "2026-09-15", estado="completada")
        cadena = str(tarea)
        
        self.assertIn("[OK COMPLETADA]", cadena)
        self.assertIn("Revisar código", cadena)
        self.assertIn("Revisión de PRs", cadena)


if __name__ == "__main__":
    unittest.main()