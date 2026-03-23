"""Tests para el componente ModeSelector."""
import unittest
import flet as ft

from pomopy.components.mode_selector import ModeSelector


class TestModeSelector(unittest.TestCase):
    """Tests para ModeSelector."""

    def setUp(self):
        """Crea una instancia de ModeSelector y llama build()."""
        self.callback_calls = []
        self.selector = ModeSelector(
            on_mode_change=lambda mode: self.callback_calls.append(mode),
        )
        self.selector.build()

    def test_init_defaults(self):
        """Verifica el estado inicial del componente."""
        self.assertEqual(self.selector.current_mode, "work")

    def test_init_callback_assigned(self):
        """Verifica que el callback se asigna correctamente."""
        self.assertIsNotNone(self.selector.on_mode_change)

    def test_init_no_callback(self):
        """Verifica que se puede crear sin callback."""
        selector = ModeSelector()
        self.assertIsNone(selector.on_mode_change)
        self.assertEqual(selector.current_mode, "work")

    def test_build_returns_row(self):
        """Verifica que build() retorna un ft.Row."""
        selector = ModeSelector()
        result = selector.build()
        self.assertIsInstance(result, ft.Row)

    def test_build_creates_three_chips(self):
        """Verifica que build() crea exactamente 3 chips."""
        row = self.selector._control
        self.assertEqual(len(row.controls), 3)
        for ctrl in row.controls:
            self.assertIsInstance(ctrl, ft.Chip)

    def test_build_chip_labels(self):
        """Verifica que los chips tienen las etiquetas correctas."""
        labels = [
            self.selector._chips["work"].label.value,
            self.selector._chips["short_break"].label.value,
            self.selector._chips["long_break"].label.value,
        ]
        self.assertEqual(labels, ["Work", "Short Break", "Long Break"])

    def test_default_chip_selection(self):
        """Verifica que solo el chip Work está seleccionado por defecto."""
        self.assertTrue(self.selector._chips["work"].selected)
        self.assertFalse(self.selector._chips["short_break"].selected)
        self.assertFalse(self.selector._chips["long_break"].selected)

    def test_change_mode_updates_current_mode(self):
        """Verifica que _change_mode actualiza current_mode."""
        self.selector._change_mode("short_break")
        self.assertEqual(self.selector.current_mode, "short_break")

    def test_change_mode_updates_chip_selection(self):
        """Verifica que _change_mode actualiza el estado selected de los chips."""
        self.selector._change_mode("long_break")
        self.assertFalse(self.selector._chips["work"].selected)
        self.assertFalse(self.selector._chips["short_break"].selected)
        self.assertTrue(self.selector._chips["long_break"].selected)

    def test_change_mode_calls_callback(self):
        """Verifica que _change_mode invoca on_mode_change con el modo."""
        self.selector._change_mode("short_break")
        self.assertEqual(self.callback_calls, ["short_break"])

    def test_change_mode_no_callback(self):
        """Verifica que no falla sin callback asignado."""
        selector = ModeSelector()
        selector.build()
        selector._change_mode("long_break")
        self.assertEqual(selector.current_mode, "long_break")

    def test_change_mode_back_to_work(self):
        """Verifica cambio de modo de vuelta a work."""
        self.selector._change_mode("short_break")
        self.selector._change_mode("work")
        self.assertEqual(self.selector.current_mode, "work")
        self.assertTrue(self.selector._chips["work"].selected)
        self.assertFalse(self.selector._chips["short_break"].selected)


if __name__ == "__main__":
    unittest.main()
