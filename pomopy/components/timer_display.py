"""
TimerDisplay component - Muestra el timer con ProgressRing animado.
"""
import flet as ft


class TimerDisplay:
    """Componente para mostrar el timer con progreso circular.

    Usa composición para construir un ft.Stack con un ProgressRing
    y un Text centrado. Compatible con Flet 0.82.0+.

    Attributes:
        time_text: Texto del reloj en formato MM:SS.
        progress: Progreso del anillo (0.0-1.0).
        color: Color del anillo de progreso.
    """

    def __init__(self):
        self.time_text = "25:00"
        self.progress = 0.0
        self.color = ft.Colors.BLUE
        self._control = None
        self._progress_ring = None
        self._time_label = None

    def build(self):
        """Construye el componente visual.

        Returns:
            ft.Stack con ProgressRing y Text centrado.
        """
        self._progress_ring = ft.ProgressRing(
            value=self.progress,
            stroke_width=10,
            width=200,
            height=200,
            color=self.color,
        )
        self._time_label = ft.Text(
            value=self.time_text,
            size=48,
            weight=ft.FontWeight.BOLD,
        )
        self._control = ft.Stack(
            controls=[
                self._progress_ring,
                ft.Container(
                    content=self._time_label,
                    width=200,
                    height=200,
                    alignment=ft.Alignment(0, 0),
                ),
            ],
            width=200,
            height=200,
        )
        return self._control

    def update_time(self, time_text):
        """Actualiza el texto del reloj.

        Args:
            time_text: Texto en formato MM:SS.
        """
        self.time_text = time_text
        self._time_label.value = time_text

    def update_progress(self, percentage):
        """Actualiza el progreso del anillo.

        Args:
            percentage: Porcentaje de progreso (0-100). Se convierte a 0.0-1.0.
        """
        self.progress = percentage / 100.0
        self._progress_ring.value = self.progress

    def set_color(self, color):
        """Cambia el color del anillo de progreso.

        Args:
            color: Color del anillo (string de color Flet).
        """
        self.color = color
        self._progress_ring.color = color
