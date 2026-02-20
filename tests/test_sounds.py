"""
Unit tests for module sounds.
"""
import unittest
import os
import tempfile
from pomopy.sounds import SoundManager, PYGAME_AVAILABLE


class TestSoundManager(unittest.TestCase):
    """Tests for class SoundManager."""
    
    def test_initialization_default(self):
        """Verifies that the manager initializes with default values."""
        manager = SoundManager()
        
        self.assertEqual(manager.alarm_file, 'alarm-digital.mp3')
        self.assertTrue(manager.enabled)
        self.assertEqual(manager.alarm_count, 0)
    
    def test_initialization_custom(self):
        """Verifies that the manager initializes with custom values."""
        manager = SoundManager(alarm_file='custom.mp3', enabled=False)
        
        self.assertEqual(manager.alarm_file, 'custom.mp3')
        self.assertFalse(manager.enabled)
    
    def test_initialization_with_pygame(self):
        """Verifies the initialization when pygame is available."""
        manager = SoundManager(enabled=True)
        
        if PYGAME_AVAILABLE:
            self.assertTrue(manager.initialized)
        else:
            self.assertFalse(manager.initialized)
    
    def test_initialization_disabled(self):
        """Verifies that does not initialize pygame if disabled."""
        manager = SoundManager(enabled=False)
        
        self.assertFalse(manager.initialized)
    
    def test_play_alarm_when_disabled(self):
        """Verifies that does not play if disabled."""
        manager = SoundManager(enabled=False)
        
        # Should not raise exception
        manager.play_alarm(times=3)
        
        self.assertEqual(manager.alarm_count, 0)
    
    def test_play_alarm_sets_parameters(self):
        """Verifies that play_alarm configures the parameters correctly."""
        manager = SoundManager(enabled=True)
        
        manager.play_alarm(times=3, interval=1000)
        
        self.assertEqual(manager.times, 3)
        self.assertEqual(manager.interval, 1000)
    
    def test_play_alarm_with_callback(self):
        """Verifies that play_alarm accepts callback."""
        manager = SoundManager(enabled=True)
        callback_calls = []
        
        def callback(count, next_fn):
            callback_calls.append(count)
        
        manager.play_alarm(times=2, callback=callback)
        
        self.assertIsNotNone(manager.callback)
    
    def test_stop(self):
        """Verifies that stop stops the playback."""
        manager = SoundManager(enabled=True)
        manager.alarm_count = 3
        
        manager.stop()
        
        self.assertEqual(manager.alarm_count, 0)
    
    def test_is_available_without_file(self):
        """Verifies that is_available returns False without file."""
        manager = SoundManager(alarm_file='nonexistent.mp3', enabled=True)
        
        self.assertFalse(manager.is_available())
    
    def test_is_available_with_file(self):
        """Verifies that is_available returns True with existing file."""
        # Create temporary file
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
            temp_file = f.name
        
        try:
            manager = SoundManager(alarm_file=temp_file, enabled=True)
            
            if PYGAME_AVAILABLE:
                self.assertTrue(manager.is_available())
            else:
                self.assertFalse(manager.is_available())
        finally:
            os.unlink(temp_file)
    
    def test_is_available_when_disabled(self):
        """Verifies that is_available returns False when disabled."""
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
            temp_file = f.name
        
        try:
            manager = SoundManager(alarm_file=temp_file, enabled=False)
            
            self.assertFalse(manager.is_available())
        finally:
            os.unlink(temp_file)
    
    def test_play_once_increments_count(self):
        """Verifies that _play_once increments the counter."""
        manager = SoundManager(enabled=True)
        manager.times = 3
        manager.alarm_count = 0
        
        manager._play_once()
        
        self.assertEqual(manager.alarm_count, 1)
    
    def test_play_once_stops_at_limit(self):
        """Verifies that _play_once stops when reaching the limit."""
        manager = SoundManager(enabled=True)
        manager.times = 2
        manager.alarm_count = 2
        
        manager._play_once()
        
        self.assertEqual(manager.alarm_count, 0)  # Resets
    
    def test_multiple_play_calls(self):
        """Verifies that can make multiple calls to play_alarm."""
        manager = SoundManager(enabled=True)
        
        manager.play_alarm(times=2)
        manager.play_alarm(times=3)
        
        self.assertEqual(manager.times, 3)
    
    def test_set_volume(self):
        """Verifies that can set the volume."""
        manager = SoundManager(enabled=True)
        manager.set_volume(0.5)
        # Should not raise exception
    
    def test_get_volume_default(self):
        """Verifies that get_volume returns a valid value."""
        manager = SoundManager(enabled=True)
        volume = manager.get_volume()
        self.assertGreaterEqual(volume, 0.0)
        self.assertLessEqual(volume, 1.0)
    
    def test_get_volume_when_disabled(self):
        """Verifies that get_volume returns 1.0 when disabled."""
        manager = SoundManager(enabled=False)
        volume = manager.get_volume()
        self.assertEqual(volume, 1.0)


if __name__ == '__main__':
    unittest.main()
