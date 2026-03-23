"""Tests para el componente StatsPanel."""
import unittest
import flet as ft

from pomopy.components.stats_panel import StatsPanel


class TestStatsPanel(unittest.TestCase):
    """Tests para StatsPanel."""

    def setUp(self):
        """Crea una instancia de StatsPanel y llama build()."""
        self.panel = StatsPanel()
        self.panel.build()

    def test_init_defaults(self):
        """Verifica el estado inicial con todos los valores en cero."""
        self.assertEqual(self.panel.stats['work'], 0)
        self.assertEqual(self.panel.stats['short_break'], 0)
        self.assertEqual(self.panel.stats['long_break'], 0)
        self.assertEqual(self.panel.stats['work_time'], '00:00')
        self.assertEqual(self.panel.stats['break_time'], '00:00')
        self.assertEqual(self.panel.stats['meeting_time'], '00:00:00')

    def test_init_label_values(self):
        """Verifica que los labels muestran los valores iniciales."""
        self.assertEqual(self.panel._labels['work'].value, '0')
        self.assertEqual(self.panel._labels['short_break'].value, '0')
        self.assertEqual(self.panel._labels['long_break'].value, '0')
        self.assertEqual(self.panel._labels['work_time'].value, '00:00')
        self.assertEqual(self.panel._labels['break_time'].value, '00:00')
        self.assertEqual(self.panel._labels['meeting_time'].value, '00:00:00')

    def test_build_returns_column(self):
        """Verifica que build() retorna un ft.Column."""
        panel = StatsPanel()
        result = panel.build()
        self.assertIsInstance(result, ft.Column)

    def test_build_creates_three_rows(self):
        """Verifica que build() crea exactamente 3 filas."""
        column = self.panel._control
        self.assertEqual(len(column.controls), 3)
        for row in column.controls:
            self.assertIsInstance(row, ft.Row)

    def test_build_row_labels(self):
        """Verifica que cada fila tiene las etiquetas correctas."""
        rows = self.panel._control.controls
        # Row 1: Pomodoros / Work time
        self.assertEqual(rows[0].controls[0].value, "Pomodoros:")
        self.assertEqual(rows[0].controls[2].value, "Work time:")
        # Row 2: Short breaks / Break time
        self.assertEqual(rows[1].controls[0].value, "Short breaks:")
        self.assertEqual(rows[1].controls[2].value, "Break time:")
        # Row 3: Long breaks / Meeting time
        self.assertEqual(rows[2].controls[0].value, "Long breaks:")
        self.assertEqual(rows[2].controls[2].value, "Meeting time:")

    def test_update_stats_full(self):
        """Verifica que update_stats actualiza el dict interno completo."""
        new_stats = {
            'work': 3,
            'short_break': 2,
            'long_break': 1,
            'work_time': '01:15',
            'break_time': '00:10',
            'meeting_time': '00:30:00',
        }
        self.panel.update_stats(new_stats)
        self.assertEqual(self.panel.stats['work'], 3)
        self.assertEqual(self.panel.stats['short_break'], 2)
        self.assertEqual(self.panel.stats['long_break'], 1)
        self.assertEqual(self.panel.stats['work_time'], '01:15')
        self.assertEqual(self.panel.stats['break_time'], '00:10')
        self.assertEqual(self.panel.stats['meeting_time'], '00:30:00')

    def test_update_stats_updates_labels(self):
        """Verifica que update_stats actualiza los textos mostrados."""
        self.panel.update_stats({
            'work': 5,
            'short_break': 4,
            'long_break': 2,
            'work_time': '02:05',
            'break_time': '00:20',
            'meeting_time': '01:00:00',
        })
        self.assertEqual(self.panel._labels['work'].value, '5')
        self.assertEqual(self.panel._labels['short_break'].value, '4')
        self.assertEqual(self.panel._labels['long_break'].value, '2')
        self.assertEqual(self.panel._labels['work_time'].value, '02:05')
        self.assertEqual(self.panel._labels['break_time'].value, '00:20')
        self.assertEqual(self.panel._labels['meeting_time'].value, '01:00:00')

    def test_update_stats_partial(self):
        """Verifica que update_stats acepta actualizaciones parciales."""
        self.panel.update_stats({'work': 1, 'work_time': '00:25'})
        # Updated keys
        self.assertEqual(self.panel.stats['work'], 1)
        self.assertEqual(self.panel.stats['work_time'], '00:25')
        self.assertEqual(self.panel._labels['work'].value, '1')
        self.assertEqual(self.panel._labels['work_time'].value, '00:25')
        # Unchanged keys
        self.assertEqual(self.panel.stats['short_break'], 0)
        self.assertEqual(self.panel.stats['break_time'], '00:00')
        self.assertEqual(self.panel._labels['short_break'].value, '0')
        self.assertEqual(self.panel._labels['break_time'].value, '00:00')


if __name__ == "__main__":
    unittest.main()
