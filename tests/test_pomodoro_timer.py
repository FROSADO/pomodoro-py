"""
Unit tests for module pomodoro_timer.
"""
import unittest
from pomopy.pomodoro_timer import PomodoroTimer


class TestPomodoroTimer(unittest.TestCase):
    """Tests for class PomodoroTimer."""
    
    def test_initialization(self):
        """Verifies that the timer initializes correctly."""
        timer = PomodoroTimer(1500)
        
        self.assertEqual(timer.initial_time, 1500)
        self.assertEqual(timer.time_left, 1500)
        self.assertFalse(timer.is_running)
        self.assertIsNone(timer.on_finish)
    
    def test_initialization_with_callback(self):
        """Verifies that the callback assigns correctly."""
        callback_called = []
        
        def callback():
            callback_called.append(True)
        
        timer = PomodoroTimer(10, on_finish=callback)
        self.assertEqual(timer.on_finish, callback)
    
    def test_start(self):
        """Verifies that start() activates the timer."""
        timer = PomodoroTimer(1500)
        timer.start()
        
        self.assertTrue(timer.is_running)
    
    def test_pause(self):
        """Verifies that pause() stops the timer."""
        timer = PomodoroTimer(1500)
        timer.start()
        timer.pause()
        
        self.assertFalse(timer.is_running)
    
    def test_reset_without_new_time(self):
        """Verifies that reset() restores the initial time."""
        timer = PomodoroTimer(1500)
        timer.start()
        timer.tick()
        timer.tick()
        
        timer.reset()
        
        self.assertEqual(timer.time_left, 1500)
        self.assertFalse(timer.is_running)
    
    def test_reset_with_new_time(self):
        """Verifies that reset() can change the initial time."""
        timer = PomodoroTimer(1500)
        timer.reset(300)
        
        self.assertEqual(timer.initial_time, 300)
        self.assertEqual(timer.time_left, 300)
        self.assertFalse(timer.is_running)
    
    def test_tick_when_not_running(self):
        """Verifies that tick() does not decrement if not running."""
        timer = PomodoroTimer(1500)
        result = timer.tick()
        
        self.assertEqual(timer.time_left, 1500)
        self.assertFalse(result)
    
    def test_tick_when_running(self):
        """Verifies that tick() decrements the time when running."""
        timer = PomodoroTimer(10)
        timer.start()
        
        timer.tick()
        self.assertEqual(timer.time_left, 9)
        
        timer.tick()
        self.assertEqual(timer.time_left, 8)
    
    def test_tick_reaches_zero(self):
        """Verifies that tick() returns True when reaches 0."""
        timer = PomodoroTimer(2)
        timer.start()
        
        result1 = timer.tick()
        self.assertFalse(result1)
        self.assertEqual(timer.time_left, 1)
        
        result2 = timer.tick()
        self.assertTrue(result2)
        self.assertEqual(timer.time_left, 0)
        self.assertFalse(timer.is_running)
    
    def test_tick_calls_callback(self):
        """Verifies that tick() executes the callback when reaches 0."""
        callback_called = []
        
        def callback():
            callback_called.append(True)
        
        timer = PomodoroTimer(1, on_finish=callback)
        timer.start()
        timer.tick()
        
        self.assertEqual(len(callback_called), 1)
        self.assertEqual(timer.time_left, 0)
    
    def test_tick_stops_at_zero(self):
        """Verifies that tick() does not decrement below 0."""
        timer = PomodoroTimer(1)
        timer.start()
        
        timer.tick()
        timer.tick()
        timer.tick()
        
        self.assertEqual(timer.time_left, 0)
    
    def test_get_time_formatted(self):
        """Verifies that get_time_formatted() returns the correct format."""
        timer = PomodoroTimer(1500)  # 25 minutes
        self.assertEqual(timer.get_time_formatted(), "25:00")
        
        timer.time_left = 305  # 5:05
        self.assertEqual(timer.get_time_formatted(), "05:05")
        
        timer.time_left = 59  # 0:59
        self.assertEqual(timer.get_time_formatted(), "00:59")
        
        timer.time_left = 0  # 0:00
        self.assertEqual(timer.get_time_formatted(), "00:00")
    
    def test_is_finished(self):
        """Verifies that is_finished() returns the correct state."""
        timer = PomodoroTimer(2)
        
        self.assertFalse(timer.is_finished())
        
        timer.start()
        timer.tick()
        self.assertFalse(timer.is_finished())
        
        timer.tick()
        self.assertTrue(timer.is_finished())
    
    def test_pause_and_resume(self):
        """Verifies that can pause and resume the timer."""
        timer = PomodoroTimer(10)
        timer.start()
        
        timer.tick()
        self.assertEqual(timer.time_left, 9)
        
        timer.pause()
        timer.tick()
        timer.tick()
        self.assertEqual(timer.time_left, 9)  # Should not change
        
        timer.start()
        timer.tick()
        self.assertEqual(timer.time_left, 8)
    
    def test_multiple_resets(self):
        """Verifies that can do multiple resets."""
        timer = PomodoroTimer(100)
        timer.start()
        
        for _ in range(10):
            timer.tick()
        
        self.assertEqual(timer.time_left, 90)
        
        timer.reset()
        self.assertEqual(timer.time_left, 100)
        
        timer.reset(50)
        self.assertEqual(timer.time_left, 50)
        self.assertEqual(timer.initial_time, 50)


if __name__ == '__main__':
    unittest.main()
