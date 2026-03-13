"""
TaskInput component - Input para gestión de tareas.
"""
import flet as ft


class TaskInput(ft.UserControl):
    """Componente para entrada y completado de tareas."""
    
    def __init__(self, on_complete):
        super().__init__()
        self.on_complete = on_complete
    
    def build(self):
        """Construye el componente visual."""
        # TODO: Implementar en Fase 2
        pass
