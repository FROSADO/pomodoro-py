"""
ControlButtons component - Botones de control Start/Pause y Reset.
"""
import flet as ft


class ControlButtons:
    """Componente para los botones de control del timer.

    Usa composición para construir un ft.Row con botones Start/Pause
    y Reset. Compatible con Flet 0.82.0+.

    Attributes:
        is_running: Estado del timer (True=corriendo, False=pausado).
        on_start_pause: Callback al pulsar Start/Pause.
        on_reset: Callback al pulsar Reset.
    """

    def __init__(self, on_start_pause=None, on_reset=None):
        """Inicializa el componente de botones de control.

        Args:
            on_start_pause: Callback invocado al pulsar Start/Pause.
            on_reset: Callback invocado al pulsar Reset.
        """
        self.on_start_pause = on_start_pause
        self.on_reset = on_reset
        self.is_running = False
        self._start_pause_button = None
        self._reset_button = None
        self._control = None

    def build(self):
        """Construye el componente visual.

        Returns:
            ft.Row con botones Start/Pause y Reset.
        """
        self._start_pause_button = ft.Button(
            content=ft.Text("Start"),
            icon=ft.Icons.PLAY_ARROW,
            on_click=self._handle_start_pause,
        )
        self._reset_button = ft.OutlinedButton(
            content=ft.Text("Reset"),
            icon=ft.Icons.REFRESH,
            on_click=self._handle_reset,
        )
        self._control = ft.Row(
            controls=[self._start_pause_button, self._reset_button],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        return self._control

    def _handle_start_pause(self, e):
        """Alterna entre Start y Pause.

        Cambia el estado is_running, actualiza texto e icono del botón,
        y llama al callback on_start_pause.

        Args:
            e: Evento de click de Flet.
        """
        self.is_running = not self.is_running
        if self.is_running:
            self._start_pause_button.content = ft.Text("Pause")
            self._start_pause_button.icon = ft.Icons.PAUSE
        else:
            self._start_pause_button.content = ft.Text("Start")
            self._start_pause_button.icon = ft.Icons.PLAY_ARROW
        if self.on_start_pause:
            self.on_start_pause(e)

    def _handle_reset(self, e):
        """Maneja el click en Reset.

        Args:
            e: Evento de click de Flet.
        """
        if self.on_reset:
            self.on_reset(e)
