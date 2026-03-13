"""
StatsPanel component - Panel de estadísticas de la sesión.
"""
import flet as ft


class StatsPanel(ft.UserControl):
    """Componente para mostrar estadísticas de pomodoros y tiempos."""
    
    def __init__(self):
        super().__init__()
        self.stats = {
            'work': 0,
            'short_break': 0,
            'long_break': 0,
            'work_time': '00:00',
            'break_time': '00:00',
            'meeting_time': '00:00:00'
        }
    
    def build(self):
        """Construye el componente visual."""
        # TODO: Implementar en Fase 2
        pass
