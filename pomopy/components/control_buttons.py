"""
ControlButtons component - Botones de control Start/Pause y Reset.
"""
import flet as ft


class ControlButtons(ft.UserControl):
    """Componente para los botones de control del timer."""
    
    def __init__(self, on_start_pause, on_reset):
        super().__init__()
        self.on_start_pause = on_start_pause
        self.on_reset = on_reset
        self.is_running = False
    
    def build(self):
        """Construye el componente visual."""
        # TODO: Implementar en Fase 2
        pass
