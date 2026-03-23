"""
StatsPanel component - Panel de estadísticas de la sesión.
"""
import flet as ft


class StatsPanel:
    """Componente para mostrar estadísticas de pomodoros y tiempos.

    Usa composición para construir un ft.Column con filas de
    estadísticas. Compatible con Flet 0.82.0+.

    Attributes:
        stats: Diccionario con contadores y tiempos de la sesión.
    """

    def __init__(self):
        """Inicializa el componente con estadísticas en cero."""
        self.stats = {
            'work': 0,
            'short_break': 0,
            'long_break': 0,
            'work_time': '00:00',
            'break_time': '00:00',
            'meeting_time': '00:00:00',
        }
        self._labels = {}
        self._control = None

    def build(self):
        """Construye el componente visual.

        Returns:
            ft.Column con filas de estadísticas: Pomodoros/Work time,
            Short breaks/Break time, Long breaks/Meeting time.
        """
        self._labels = {
            'work': ft.Text(str(self.stats['work'])),
            'work_time': ft.Text(self.stats['work_time']),
            'short_break': ft.Text(str(self.stats['short_break'])),
            'break_time': ft.Text(self.stats['break_time']),
            'long_break': ft.Text(str(self.stats['long_break'])),
            'meeting_time': ft.Text(self.stats['meeting_time']),
        }

        row1 = ft.Row(
            controls=[
                ft.Text("Pomodoros:"),
                self._labels['work'],
                ft.Text("Work time:"),
                self._labels['work_time'],
            ],
        )
        row2 = ft.Row(
            controls=[
                ft.Text("Short breaks:"),
                self._labels['short_break'],
                ft.Text("Break time:"),
                self._labels['break_time'],
            ],
        )
        row3 = ft.Row(
            controls=[
                ft.Text("Long breaks:"),
                self._labels['long_break'],
                ft.Text("Meeting time:"),
                self._labels['meeting_time'],
            ],
        )

        self._control = ft.Column(controls=[row1, row2, row3])
        return self._control

    def update_stats(self, stats):
        """Actualiza las estadísticas internas y los textos mostrados.

        Args:
            stats: Diccionario con claves a actualizar. Acepta
                actualizaciones parciales (solo las claves presentes
                se modifican).
        """
        self.stats.update(stats)
        for key, label in self._labels.items():
            label.value = str(self.stats[key])
