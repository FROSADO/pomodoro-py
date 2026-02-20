"""
Unit tests for module pomodoro_manager.
"""
import unittest
import tempfile
import shutil
from pomopy.pomodoro_manager import PomodoroManager
from pomopy.config import Config


class TestPomodoroManager(unittest.TestCase):
    """Tests for class PomodoroManager."""
    
    def setUp(self):
        """Sets up the test environment before each test."""
        self.temp_dir = tempfile.mkdtemp()
        self.config = Config(config_file="nonexistent.yaml", silent=True)
        self.config.TASKS_FOLDER = self.temp_dir
        self.manager = PomodoroManager(self.config)
    
    def tearDown(self):
        """Cleans up after each test."""
        try:
            shutil.rmtree(self.temp_dir)
        except:
            pass
    
    def test_initialization(self):
        """Verifies that the manager initializes correctly."""
        self.assertEqual(self.manager.current_mode, 'work')
        self.assertIsNotNone(self.manager.timer)
        self.assertIsNotNone(self.manager.task_manager)
        self.assertIsNotNone(self.manager.sound_manager)
        self.assertIsNone(self.manager.on_finish_callback)
    
    def test_set_finish_callback(self):
        """Verifies setting finish callback."""
        callback_calls = []
        
        def callback():
            callback_calls.append(True)
        
        self.manager.set_finish_callback(callback)
        self.assertEqual(self.manager.on_finish_callback, callback)
    
    def test_start_timer(self):
        """Verifies that can start the timer."""
        self.manager.start_timer()
        self.assertTrue(self.manager.is_running())
    
    def test_pause_timer(self):
        """Verifies that can pause the timer."""
        self.manager.start_timer()
        self.manager.pause_timer()
        self.assertFalse(self.manager.is_running())
    
    def test_reset_timer(self):
        """Verifies that can reset the timer."""
        self.manager.start_timer()
        self.manager.tick()
        self.manager.reset_timer()
        self.assertEqual(self.manager.get_time_formatted(), "25:00")
        self.assertFalse(self.manager.is_running())
    
    def test_change_mode_to_short_break(self):
        """Verifies change to short break mode."""
        self.manager.change_mode('short_break')
        self.assertEqual(self.manager.get_current_mode(), 'short_break')
        self.assertEqual(self.manager.get_time_formatted(), "05:00")
    
    def test_change_mode_to_long_break(self):
        """Verifies change to long break mode."""
        self.manager.change_mode('long_break')
        self.assertEqual(self.manager.get_current_mode(), 'long_break')
        self.assertEqual(self.manager.get_time_formatted(), "15:00")
    
    def test_tick(self):
        """Verifies that tick decrements the time."""
        self.manager.start_timer()
        initial_time = self.manager.timer.time_left
        self.manager.tick()
        self.assertEqual(self.manager.timer.time_left, initial_time - 1)
    
    def test_get_time_formatted(self):
        """Verifies the time format."""
        time = self.manager.get_time_formatted()
        self.assertEqual(time, "25:00")
    
    def test_set_and_get_task(self):
        """Verifies setting and getting task."""
        self.manager.set_task("Test task")
        self.assertEqual(self.manager.get_task(), "Test task")
    
    def test_complete_task(self):
        """Verifies completing task."""
        self.manager.set_task("Task to complete")
        result = self.manager.complete_task()
        self.assertTrue(result)
        self.assertEqual(self.manager.get_task(), "")
    
    def test_get_stats(self):
        """Verifies getting statistics."""
        stats = self.manager.get_stats()
        self.assertIn('task', stats)
        self.assertIn('work', stats)
        self.assertIn('short_break', stats)
        self.assertIn('long_break', stats)
        self.assertIn('total_time', stats)
        self.assertIn('meeting_time', stats)
    
    def test_get_total_work_time_zero(self):
        """Verifies initial work time."""
        time = self.manager.get_total_work_time()
        self.assertEqual(time, "00:00")
    
    def test_get_total_work_time_with_pomodoros(self):
        """Verifies work time calculation."""
        self.manager.task_manager.increment_work()
        self.manager.task_manager.increment_work()
        time = self.manager.get_total_work_time()
        self.assertEqual(time, "50:00")  # 2 * 25 minutes
    
    def test_get_total_break_time_zero(self):
        """Verifies initial break time."""
        time = self.manager.get_total_break_time()
        self.assertEqual(time, "00:00")
    
    def test_get_total_break_time_with_breaks(self):
        """Verifies break time calculation."""
        self.manager.task_manager.increment_short_break()
        self.manager.task_manager.increment_long_break()
        time = self.manager.get_total_break_time()
        self.assertEqual(time, "20:00")  # 5 + 15 minutes
    
    def test_on_timer_finish_increments_work(self):
        """Verifies that finishing increments the work counter."""
        self.manager.current_mode = 'work'
        initial_count = self.manager.task_manager.work_count
        self.manager._on_timer_finish()
        self.assertEqual(self.manager.task_manager.work_count, initial_count + 1)
    
    def test_on_timer_finish_increments_short_break(self):
        """Verifies that finishing increments the short break counter."""
        self.manager.current_mode = 'short_break'
        initial_count = self.manager.task_manager.short_break_count
        self.manager._on_timer_finish()
        self.assertEqual(self.manager.task_manager.short_break_count, initial_count + 1)
    
    def test_on_timer_finish_increments_long_break(self):
        """Verifies that finishing increments the long break counter."""
        self.manager.current_mode = 'long_break'
        initial_count = self.manager.task_manager.long_break_count
        self.manager._on_timer_finish()
        self.assertEqual(self.manager.task_manager.long_break_count, initial_count + 1)
    
    def test_on_timer_finish_calls_callback(self):
        """Verifies that finishing calls the callback."""
        callback_calls = []
        
        def callback():
            callback_calls.append(True)
        
        self.manager.set_finish_callback(callback)
        self.manager._on_timer_finish()
        self.assertEqual(len(callback_calls), 1)
    
    def test_set_volume(self):
        """Verifies that can set the volume."""
        self.manager.set_volume(0.5)
        # Should not raise exception
    
    def test_get_volume(self):
        """Verifies that can get the volume."""
        volume = self.manager.get_volume()
        self.assertGreaterEqual(volume, 0.0)
        self.assertLessEqual(volume, 1.0)
    
    def test_increment_meeting_time(self):
        """Verifies incrementing meeting time."""
        self.manager.increment_meeting_time(60)
        self.assertEqual(self.manager.task_manager.meeting_time, 60)
    
    def test_get_meeting_time(self):
        """Verifies getting meeting time formatted."""
        self.manager.increment_meeting_time(3661)  # 1 hour, 1 minute, 1 second
        time = self.manager.get_meeting_time()
        self.assertEqual(time, "01:01:01")
    
    def test_save_meeting(self):
        """Verifies saving meeting."""
        self.manager.increment_meeting_time(1800)  # 30 minutes
        result = self.manager.save_meeting()
        self.assertTrue(result)
        self.assertEqual(self.manager.task_manager.meeting_time, 0)
    
    def test_save_meeting_without_time(self):
        """Verifies that meeting without time is not saved."""
        result = self.manager.save_meeting()
        self.assertFalse(result)
    
    def test_meeting_time_resets_after_save(self):
        """Verifies that meeting time resets after saving."""
        self.manager.increment_meeting_time(600)
        self.manager.save_meeting()
        time = self.manager.get_meeting_time()
        self.assertEqual(time, "00:00:00")


if __name__ == '__main__':
    unittest.main()
