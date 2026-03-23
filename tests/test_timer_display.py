"""Tests para el componente TimerDisplay."""
import unittest
import flet as ft

from pomopy.components.timer_display import TimerDisplay


class TestTimerDisplay(unittest.TestCase):
    """Tests para TimerDisplay."""

    def setUp(self):
        """Crea una instancia de TimerDisplay y llama build()."""
        self.display = TimerDisplay()
        self.display.build()

    def test_init_defaults(self):
        """Verifica el estado inicial del componente."""
        self.assertEqual(self.display.time_text, "25:00")
        self.assertEqual(self.display.progress, 0.0)
        self.assertEqual(self.display.color, ft.Colors.BLUE)

    def test_init_progress_ring(self):
        """Verifica que el ProgressRing se crea con valores correctos."""
        ring = self.display._progress_ring
        self.assertEqual(ring.value, 0.0)
        self.assertEqual(ring.stroke_width, 10)
        self.assertEqual(ring.width, 200)
        self.assertEqual(ring.height, 200)
        self.assertEqual(ring.color, ft.Colors.BLUE)

    def test_init_time_label(self):
        """Verifica que el Text se crea con valores correctos."""
        label = self.display._time_label
        self.assertEqual(label.value, "25:00")
        self.assertEqual(label.size, 48)
        self.assertEqual(label.weight, ft.FontWeight.BOLD)

    def test_update_time(self):
        """Verifica que update_time cambia el texto del reloj."""
        self.display.update_time("10:30")
        self.assertEqual(self.display.time_text, "10:30")
        self.assertEqual(self.display._time_label.value, "10:30")

    def test_update_time_zero(self):
        """Verifica update_time con tiempo cero."""
        self.display.update_time("00:00")
        self.assertEqual(self.display.time_text, "00:00")
        self.assertEqual(self.display._time_label.value, "00:00")

    def test_update_progress(self):
        """Verifica que update_progress convierte 0-100 a 0.0-1.0."""
        self.display.update_progress(50)
        self.assertAlmostEqual(self.display.progress, 0.5)
        self.assertAlmostEqual(self.display._progress_ring.value, 0.5)

    def test_update_progress_full(self):
        """Verifica update_progress al 100%."""
        self.display.update_progress(100)
        self.assertAlmostEqual(self.display.progress, 1.0)
        self.assertAlmostEqual(self.display._progress_ring.value, 1.0)

    def test_update_progress_zero(self):
        """Verifica update_progress al 0%."""
        self.display.update_progress(0)
        self.assertAlmostEqual(self.display.progress, 0.0)
        self.assertAlmostEqual(self.display._progress_ring.value, 0.0)

    def test_set_color(self):
        """Verifica que set_color cambia el color del anillo."""
        self.display.set_color(ft.Colors.RED)
        self.assertEqual(self.display.color, ft.Colors.RED)
        self.assertEqual(self.display._progress_ring.color, ft.Colors.RED)

    def test_set_color_green(self):
        """Verifica set_color con otro color."""
        self.display.set_color(ft.Colors.GREEN)
        self.assertEqual(self.display.color, ft.Colors.GREEN)
        self.assertEqual(self.display._progress_ring.color, ft.Colors.GREEN)


if __name__ == "__main__":
    unittest.main()
