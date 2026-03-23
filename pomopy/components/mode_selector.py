"""
ModeSelector component - Selector de modos (Work, Short Break, Long Break).
"""
import flet as ft


class ModeSelector:
    """Componente para seleccionar el modo del timer.

    Usa composición para construir un ft.Row con 3 ft.Chip
    para cada modo. Compatible con Flet 0.82.0+.

    Attributes:
        current_mode: Modo actual ('work', 'short_break', 'long_break').
        on_mode_change: Callback invocado al cambiar de modo.
    """

    MODES = [
        ("work", "Work"),
        ("short_break", "Short Break"),
        ("long_break", "Long Break"),
    ]

    def __init__(self, on_mode_change=None):
        """Inicializa el componente selector de modos.

        Args:
            on_mode_change: Callback invocado con el nuevo modo al cambiar.
        """
        self.on_mode_change = on_mode_change
        self.current_mode = "work"
        self._chips = {}
        self._control = None

    def build(self):
        """Construye el componente visual.

        Returns:
            ft.Row con 3 ft.Chip para Work, Short Break y Long Break.
        """
        self._chips = {}
        for mode_key, mode_label in self.MODES:
            chip = ft.Chip(
                label=ft.Text(mode_label),
                selected=mode_key == self.current_mode,
                on_select=lambda e, m=mode_key: self._change_mode(m),
            )
            self._chips[mode_key] = chip

        self._control = ft.Row(
            controls=list(self._chips.values()),
            alignment=ft.MainAxisAlignment.CENTER,
        )
        return self._control

    def _change_mode(self, mode):
        """Cambia el modo actual y actualiza el estado visual de los chips.

        Args:
            mode: Nuevo modo ('work', 'short_break' o 'long_break').
        """
        self.current_mode = mode
        for mode_key, chip in self._chips.items():
            chip.selected = mode_key == mode
        if self.on_mode_change:
            self.on_mode_change(mode)
