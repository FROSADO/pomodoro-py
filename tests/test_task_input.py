"""Tests para el componente TaskInput."""
import unittest
import flet as ft

from pomopy.components.task_input import TaskInput


class TestTaskInput(unittest.TestCase):
    """Tests para TaskInput."""

    def setUp(self):
        """Crea una instancia de TaskInput y llama build()."""
        self.completed_tasks = []
        self.task_input = TaskInput(
            on_complete=lambda name: self.completed_tasks.append(name),
        )
        self.task_input.build()

    def test_init_callback_assigned(self):
        """Verifica que el callback se asigna correctamente."""
        self.assertIsNotNone(self.task_input.on_complete)

    def test_init_no_callback(self):
        """Verifica que se puede crear sin callback."""
        task_input = TaskInput()
        self.assertIsNone(task_input.on_complete)

    def test_build_returns_column(self):
        """Verifica que build() retorna un ft.Column."""
        task_input = TaskInput()
        result = task_input.build()
        self.assertIsInstance(result, ft.Column)

    def test_build_creates_text_field_and_button(self):
        """Verifica que build() crea TextField y Button."""
        col = self.task_input._control
        self.assertEqual(len(col.controls), 2)
        self.assertIsInstance(col.controls[0], ft.TextField)
        self.assertIsInstance(col.controls[1], ft.Button)

    def test_text_field_label(self):
        """Verifica que el TextField tiene label 'Task name'."""
        self.assertEqual(self.task_input._text_field.label, "Task name")

    def test_text_field_width(self):
        """Verifica que el TextField tiene width=300."""
        self.assertEqual(self.task_input._text_field.width, 300)

    def test_button_text(self):
        """Verifica que el botón tiene texto '✓ Complete'."""
        self.assertEqual(self.task_input._complete_button.content.value, "✓ Complete")

    def test_button_disabled_by_default(self):
        """Verifica que el botón está deshabilitado por defecto."""
        self.assertTrue(self.task_input._complete_button.disabled)

    def test_on_change_enables_button_with_text(self):
        """Verifica que _on_change habilita el botón cuando hay texto."""
        self.task_input._text_field.value = "Study"
        self.task_input._on_change(None)
        self.assertFalse(self.task_input._complete_button.disabled)

    def test_on_change_disables_button_when_cleared(self):
        """Verifica que _on_change deshabilita el botón al limpiar."""
        self.task_input._text_field.value = "Study"
        self.task_input._on_change(None)
        self.task_input._text_field.value = ""
        self.task_input._on_change(None)
        self.assertTrue(self.task_input._complete_button.disabled)

    def test_on_change_disables_button_with_whitespace(self):
        """Verifica que solo espacios en blanco no habilitan el botón."""
        self.task_input._text_field.value = "   "
        self.task_input._on_change(None)
        self.assertTrue(self.task_input._complete_button.disabled)

    def test_handle_complete_calls_callback(self):
        """Verifica que _handle_complete invoca on_complete con el nombre."""
        self.task_input._text_field.value = "Study Python"
        self.task_input._handle_complete(None)
        self.assertEqual(self.completed_tasks, ["Study Python"])

    def test_handle_complete_clears_field(self):
        """Verifica que _handle_complete limpia el campo de texto."""
        self.task_input._text_field.value = "Study Python"
        self.task_input._handle_complete(None)
        self.assertEqual(self.task_input._text_field.value, "")

    def test_handle_complete_disables_button(self):
        """Verifica que _handle_complete deshabilita el botón."""
        self.task_input._text_field.value = "Study Python"
        self.task_input._on_change(None)
        self.task_input._handle_complete(None)
        self.assertTrue(self.task_input._complete_button.disabled)

    def test_handle_complete_no_callback(self):
        """Verifica que no falla sin callback asignado."""
        task_input = TaskInput()
        task_input.build()
        task_input._text_field.value = "Study"
        task_input._handle_complete(None)  # No debe lanzar excepción
        self.assertEqual(task_input._text_field.value, "")


if __name__ == "__main__":
    unittest.main()
