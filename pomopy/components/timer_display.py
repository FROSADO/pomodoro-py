"""
TimerDisplay component - Muestra el timer con ProgressRing animado.
"""
import flet as ft


class TimerDisplay(ft.UserControl):
    """Componente para mostrar el timer con progreso circular."""
    
    def __init__(self):
        super().__init__()
        self.time_text = "25:00"
        self.progress = 0.0
        self.color = ft.colors.BLUE
    
    def build(self):
        """Construye el componente visual."""
        # TODO: Implementar en Fase 2
        pass
