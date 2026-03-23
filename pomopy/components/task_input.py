"""
TaskInput component - Input para gestión de tareas.
"""
import flet as ft


class TaskInput:
    """Componente para entrada y completado de tareas.

    Usa composición para construir un ft.Column con un TextField
    y un botón Complete. Compatible con Flet 0.82.0+.

    Attributes:
        on_complete: Callback invocado con el nombre de la tarea al completar.
    """

    def __init__(self, on_complete=None):
        """Inicializa el componente de entrada de tareas.

        Args:
            on_complete: Callback invocado con el nombre de la tarea.
        """
        self.on_complete = on_complete
        self._text_field = None
        self._complete_button = None
        self._control = None

    def build(self):
        """Construye el componente visual.

        Returns:
            ft.Column con TextField y botón Complete.
        """
        self._text_field = ft.TextField(
            label="Task name",
            width=300,
            on_change=self._on_change,
        )
        self._complete_button = ft.Button(
            content=ft.Text("✓ Complete"),
            disabled=True,
            on_click=self._handle_complete,
        )
        self._control = ft.Column(
            controls=[self._text_field, self._complete_button],
        )
        return self._control

    def _on_change(self, e):
        """Habilita o deshabilita el botón según el contenido del campo.

        Args:
            e: Evento de cambio de Flet.
        """
        has_text = bool(self._text_field.value and self._text_field.value.strip())
        self._complete_button.disabled = not has_text

    def _handle_complete(self, e):
        """Completa la tarea actual, llama al callback y limpia el campo.

        Args:
            e: Evento de click de Flet.
        """
        task_name = self._text_field.value
        if self.on_complete and task_name:
            self.on_complete(task_name)
        self._text_field.value = ""
        self._complete_button.disabled = True
