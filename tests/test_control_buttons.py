"""Tests para el componente ControlButtons."""
import unittest
import flet as ft

from pomopy.components.control_buttons import ControlButtons


class TestControlButtons(unittest.TestCase):
    """Tests para ControlButtons."""

    def setUp(self):
        """Crea una instancia de ControlButtons y llama build()."""
        self.callback_calls = []
        self.buttons = ControlButtons(
            on_start_pause=lambda e: self.callback_calls.append("start_pause"),
            on_reset=lambda e: self.callback_calls.append("reset"),
        )
        self.buttons.build()

    def test_init_defaults(self):
        """Verifica el estado inicial del componente."""
        self.assertFalse(self.buttons.is_running)

    def test_init_callbacks_assigned(self):
        """Verifica que los callbacks se asignan correctamente."""
        self.assertIsNotNone(self.buttons.on_start_pause)
        self.assertIsNotNone(self.buttons.on_reset)

    def test_init_no_callbacks(self):
        """Verifica que se puede crear sin callbacks."""
        buttons = ControlButtons()
        self.assertIsNone(buttons.on_start_pause)
        self.assertIsNone(buttons.on_reset)
        self.assertFalse(buttons.is_running)

    def test_build_returns_row(self):
        """Verifica que build() retorna un ft.Row."""
        buttons = ControlButtons()
        result = buttons.build()
        self.assertIsInstance(result, ft.Row)

    def test_build_start_pause_button(self):
        """Verifica que el botón Start/Pause se crea correctamente."""
        btn = self.buttons._start_pause_button
        self.assertIsInstance(btn, ft.Button)
        self.assertEqual(btn.content.value, "Start")
        self.assertEqual(btn.icon, ft.Icons.PLAY_ARROW)

    def test_build_reset_button(self):
        """Verifica que el botón Reset se crea correctamente."""
        btn = self.buttons._reset_button
        self.assertIsInstance(btn, ft.OutlinedButton)
        self.assertEqual(btn.content.value, "Reset")
        self.assertEqual(btn.icon, ft.Icons.REFRESH)

    def test_build_row_has_two_controls(self):
        """Verifica que el Row contiene exactamente 2 botones."""
        row = self.buttons._control
        self.assertEqual(len(row.controls), 2)

    def test_handle_start_pause_toggles_to_running(self):
        """Verifica que _handle_start_pause cambia a estado running."""
        self.buttons._handle_start_pause(None)
        self.assertTrue(self.buttons.is_running)
        self.assertEqual(self.buttons._start_pause_button.content.value, "Pause")
        self.assertEqual(self.buttons._start_pause_button.icon, ft.Icons.PAUSE)

    def test_handle_start_pause_toggles_back_to_stopped(self):
        """Verifica que un segundo click vuelve a estado stopped."""
        self.buttons._handle_start_pause(None)
        self.buttons._handle_start_pause(None)
        self.assertFalse(self.buttons.is_running)
        self.assertEqual(self.buttons._start_pause_button.content.value, "Start")
        self.assertEqual(self.buttons._start_pause_button.icon, ft.Icons.PLAY_ARROW)

    def test_handle_start_pause_calls_callback(self):
        """Verifica que _handle_start_pause invoca el callback."""
        self.buttons._handle_start_pause(None)
        self.assertIn("start_pause", self.callback_calls)

    def test_handle_reset_calls_callback(self):
        """Verifica que _handle_reset invoca el callback."""
        self.buttons._handle_reset(None)
        self.assertIn("reset", self.callback_calls)

    def test_handle_start_pause_no_callback(self):
        """Verifica que no falla sin callback asignado."""
        buttons = ControlButtons()
        buttons.build()
        buttons._handle_start_pause(None)
        self.assertTrue(buttons.is_running)

    def test_handle_reset_no_callback(self):
        """Verifica que no falla sin callback de reset."""
        buttons = ControlButtons()
        buttons.build()
        buttons._handle_reset(None)  # No debe lanzar excepción


if __name__ == "__main__":
    unittest.main()
