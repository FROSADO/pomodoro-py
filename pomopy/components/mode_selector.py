"""
ModeSelector component - Selector de modos (Work, Short Break, Long Break).
"""
import flet as ft


class ModeSelector(ft.UserControl):
    """Componente para seleccionar el modo del timer."""
    
    def __init__(self, on_mode_change):
        super().__init__()
        self.on_mode_change = on_mode_change
        self.current_mode = 'work'
    
    def build(self):
        """Construye el componente visual."""
        # TODO: Implementar en Fase 2
        pass
