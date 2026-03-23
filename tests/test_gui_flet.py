"""
Unit tests for module gui_flet.
"""
import unittest
from unittest.mock import MagicMock, patch, PropertyMock
import tempfile
import shutil


class TestPomodoroAppInit(unittest.TestCase):
    """Tests for PomodoroApp initialization and setup."""

    def setUp(self):
        """Sets up mock page and config for each test."""
        self.temp_dir = tempfile.mkdtemp()

        self.mock_page = MagicMock()
        self.mock_page.overlay = []
        self.mock_page.window = MagicMock()
        self.mock_page.theme_mode = None
        self.mock_page.theme = None

        from pomopy.config import Config
        self.config = Config(config_file="nonexistent.yaml", silent=True)
        self.config.TASKS_FOLDER = self.temp_dir
        self.config.SOUND_ENABLED = False

    def tearDown(self):
        """Cleans up temp directory."""
        try:
            shutil.rmtree(self.temp_dir)
        except Exception:
            pass

    @patch("pomopy.gui_flet.ft")
    def test_app_instantiation(self, mock_ft):
        """Verifies that PomodoroApp instantiates without errors."""
        mock_ft.ThemeMode.DARK = "dark"
        mock_ft.ThemeMode.LIGHT = "light"
        mock_ft.Theme = MagicMock()
        mock_ft.Switch = MagicMock(return_value=MagicMock(value=True))
        mock_ft.Slider = MagicMock(return_value=MagicMock())
        mock_ft.ElevatedButton = MagicMock(return_value=MagicMock())
        mock_ft.Text = MagicMock(return_value=MagicMock())
        mock_ft.SnackBar = MagicMock(return_value=MagicMock())
        mock_ft.Icons = MagicMock()
        mock_ft.ButtonStyle = MagicMock(return_value=MagicMock())
        mock_ft.Column = MagicMock(return_value=MagicMock())
        mock_ft.Container = MagicMock(return_value=MagicMock())
        mock_ft.Row = MagicMock(return_value=MagicMock())
        mock_ft.Divider = MagicMock(return_value=MagicMock())
        mock_ft.ScrollMode = MagicMock()
        mock_ft.CrossAxisAlignment = MagicMock()
        mock_ft.MainAxisAlignment = MagicMock()
        mock_ft.alignment = MagicMock()
        mock_ft.padding = MagicMock()
        mock_ft.Colors = MagicMock()

        from pomopy.gui_flet import PomodoroApp
        app = PomodoroApp(self.mock_page, self.config)

        self.assertIsNotNone(app.manager)
        self.assertIsNotNone(app.timer_display)
        self.assertIsNotNone(app.control_buttons)
        self.assertIsNotNone(app.mode_selector)
        self.assertIsNotNone(app.task_input)
        self.assertIsNotNone(app.stats_panel)
        self.assertFalse(app.meeting_active)
        self.assertFalse(app._tick_running)


class TestPomodoroAppHandlers(unittest.TestCase):
    """Tests for PomodoroApp handler methods."""

    def setUp(self):
        """Sets up a PomodoroApp with mocked Flet dependencies."""
        self.temp_dir = tempfile.mkdtemp()

        self.mock_page = MagicMock()
        self.mock_page.overlay = []
        self.mock_page.window = MagicMock()
        self.mock_page.theme_mode = None
        self.mock_page.theme = None

        from pomopy.config import Config
        self.config = Config(config_file="nonexistent.yaml", silent=True)
        self.config.TASKS_FOLDER = self.temp_dir
        self.config.SOUND_ENABLED = False

        with patch("pomopy.gui_flet.ft") as mock_ft:
            mock_ft.ThemeMode.DARK = "dark"
            mock_ft.ThemeMode.LIGHT = "light"
            mock_ft.Theme = MagicMock()
            mock_ft.Switch = MagicMock(return_value=MagicMock(value=True))
            mock_ft.Slider = MagicMock(return_value=MagicMock())
            mock_ft.ElevatedButton = MagicMock(return_value=MagicMock())
            mock_ft.Text = MagicMock(return_value=MagicMock())
            mock_ft.SnackBar = MagicMock(return_value=MagicMock())
            mock_ft.Icons = MagicMock()
            mock_ft.ButtonStyle = MagicMock(return_value=MagicMock())
            mock_ft.Column = MagicMock(return_value=MagicMock())
            mock_ft.Container = MagicMock(return_value=MagicMock())
            mock_ft.Row = MagicMock(return_value=MagicMock())
            mock_ft.Divider = MagicMock(return_value=MagicMock())
            mock_ft.ScrollMode = MagicMock()
            mock_ft.CrossAxisAlignment = MagicMock()
            mock_ft.MainAxisAlignment = MagicMock()
            mock_ft.alignment = MagicMock()
            mock_ft.padding = MagicMock()
            mock_ft.Colors = MagicMock()
            self._mock_ft = mock_ft

            from pomopy.gui_flet import PomodoroApp
            self.app = PomodoroApp(self.mock_page, self.config)

    def tearDown(self):
        """Cleans up temp directory."""
        try:
            shutil.rmtree(self.temp_dir)
        except Exception:
            pass

    def test_toggle_timer_starts(self):
        """Verifies toggle_timer starts the timer when not running."""
        self.assertFalse(self.app.manager.is_running())
        self.app.toggle_timer(None)
        self.assertTrue(self.app.manager.is_running())

    def test_toggle_timer_pauses(self):
        """Verifies toggle_timer pauses the timer when running."""
        self.app.manager.start_timer()
        self.app.toggle_timer(None)
        self.assertFalse(self.app.manager.is_running())

    def test_reset_timer(self):
        """Verifies reset_timer resets manager state."""
        self.app.manager.start_timer()
        self.app.manager.tick()
        self.app.reset_timer(None)
        self.assertFalse(self.app.manager.is_running())
        self.assertEqual(self.app.manager.get_time_formatted(), "25:00")

    def test_change_mode(self):
        """Verifies change_mode updates the manager mode."""
        self.app.change_mode("short_break")
        self.assertEqual(self.app.manager.get_current_mode(), "short_break")
        self.assertEqual(self.app.manager.get_time_formatted(), "05:00")

    def test_complete_task(self):
        """Verifies complete_task sets and completes the task."""
        self.app.complete_task("Test task")
        self.assertFalse(self.app.manager.is_running())

    def test_toggle_meeting_on(self):
        """Verifies toggle_meeting activates meeting mode."""
        self.assertFalse(self.app.meeting_active)
        self.app.toggle_meeting(None)
        self.assertTrue(self.app.meeting_active)

    def test_toggle_meeting_off(self):
        """Verifies toggle_meeting deactivates meeting mode and saves."""
        self.app.meeting_active = True
        self.app.manager.increment_meeting_time(60)
        self.app.toggle_meeting(None)
        self.assertFalse(self.app.meeting_active)

    def test_on_volume_change(self):
        """Verifies volume change handler calls manager."""
        mock_event = MagicMock()
        mock_event.control.value = 50
        self.app._on_volume_change(mock_event)
        # Should not raise

    def test_update_stats(self):
        """Verifies _update_stats calls stats_panel.update_stats."""
        self.app._update_stats()
        # Should not raise

    def test_on_timer_finish(self):
        """Verifies _on_timer_finish resets button state."""
        self.app._on_timer_finish()
        self.assertFalse(self.app.control_buttons.is_running)
        self.assertFalse(self.app._tick_running)


if __name__ == "__main__":
    unittest.main()
