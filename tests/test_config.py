"""
Unit tests for module of configuration.
"""
import unittest
import os
import tempfile
from pomopy.config import Config


class TestConfig(unittest.TestCase):
    """Tests for class Config."""
    
    def test_default_values(self):
        """Verifies that the default values load correctly."""
        config = Config(config_file="nonexistent.yaml", silent=False)
        
        self.assertEqual(config.WORK_TIME, 25 * 60)
        self.assertEqual(config.SHORT_BREAK, 5 * 60)
        self.assertEqual(config.LONG_BREAK, 15 * 60)
        self.assertEqual(config.WORK_COLOR, "#FF6B6B")
        self.assertEqual(config.SHORT_BREAK_COLOR, "#4ECDC4")
        self.assertEqual(config.LONG_BREAK_COLOR, "#45B7D1")
        self.assertEqual(config.BG_COLOR, "#2C3E50")
        self.assertEqual(config.TEXT_COLOR, "#FFFFFF")
        self.assertEqual(config.WINDOW_WIDTH, 400)
        self.assertEqual(config.WINDOW_HEIGHT, 500)
        self.assertTrue(config.ALWAYS_ON_TOP)
        self.assertTrue(config.SOUND_ENABLED)
        self.assertEqual(config.TASKS_FILE, "tasks.txt")
    
    def test_load_custom_times(self):
        """Verifies that load correctly the custom times."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            f.write("""
times:
  work_time: 30
  short_break: 10
  long_break: 20
""")
            temp_file = f.name
        
        try:
            config = Config(config_file=temp_file, silent=False)
            self.assertEqual(config.WORK_TIME, 30 * 60)
            self.assertEqual(config.SHORT_BREAK, 10 * 60)
            self.assertEqual(config.LONG_BREAK, 20 * 60)
        finally:
            os.unlink(temp_file)
    
    def test_load_custom_colors(self):
        """Verifies that load correctly the custom colors."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            f.write("""
colors:
  work_color: "#FF0000"
  short_break_color: "#00FF00"
  long_break_color: "#0000FF"
  bg_color: "#000000"
  text_color: "#AAAAAA"
""")
            temp_file = f.name
        
        try:
            config = Config(config_file=temp_file, silent=False)
            self.assertEqual(config.WORK_COLOR, "#FF0000")
            self.assertEqual(config.SHORT_BREAK_COLOR, "#00FF00")
            self.assertEqual(config.LONG_BREAK_COLOR, "#0000FF")
            self.assertEqual(config.BG_COLOR, "#000000")
            self.assertEqual(config.TEXT_COLOR, "#AAAAAA")
        finally:
            os.unlink(temp_file)
    
    def test_load_custom_window(self):
        """Verifies that load correctly the window configuration."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            f.write("""
window:
  width: 500
  height: 400
  always_on_top: false
""")
            temp_file = f.name
        
        try:
            config = Config(config_file=temp_file, silent=False)
            self.assertEqual(config.WINDOW_WIDTH, 500)
            self.assertEqual(config.WINDOW_HEIGHT, 400)
            self.assertFalse(config.ALWAYS_ON_TOP)
        finally:
            os.unlink(temp_file)
    
    def test_load_custom_sound(self):
        """Verifies that load correctly the sound configuration."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            f.write("""
sound:
  enabled: false
""")
            temp_file = f.name
        
        try:
            config = Config(config_file=temp_file, silent=False)
            self.assertFalse(config.SOUND_ENABLED)
        finally:
            os.unlink(temp_file)
    
    def test_load_custom_tasks(self):
        """Verifies that load correctly the tasks configuration."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            f.write("""
tasks:
  file: "custom_tasks.txt"
""")
            temp_file = f.name
        
        try:
            config = Config(config_file=temp_file)
            self.assertEqual(config.TASKS_FILE, "custom_tasks.txt")
        finally:
            os.unlink(temp_file)
    
    def test_partial_config(self):
        """Verifies that can load partial configurations."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            f.write("""
times:
  work_time: 50
""")
            temp_file = f.name
        
        try:
            config = Config(config_file=temp_file)
            self.assertEqual(config.WORK_TIME, 50 * 60)
            self.assertEqual(config.SHORT_BREAK, 5 * 60)  # Default value
            self.assertEqual(config.LONG_BREAK, 15 * 60)  # Default value
        finally:
            os.unlink(temp_file)
    
    def test_empty_config_file(self):
        """Verifies that an empty file does not cause errors."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            f.write("")
            temp_file = f.name
        
        try:
            config = Config(config_file=temp_file)
            self.assertEqual(config.WORK_TIME, 25 * 60)  # Default values
        finally:
            os.unlink(temp_file)
    
    def test_invalid_yaml(self):
        """Verifies that invalid YAML does not break the application."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            f.write("[invalid yaml content")
            temp_file = f.name
        
        try:
            config = Config(config_file=temp_file)
            self.assertEqual(config.WORK_TIME, 25 * 60)  # Default values
        finally:
            os.unlink(temp_file)
    
    def test_get_time_for_mode(self):
        """Verifies that get_time_for_mode returns the correct times."""
        config = Config(config_file="nonexistent.yaml")
        
        self.assertEqual(config.get_time_for_mode('work'), 25 * 60)
        self.assertEqual(config.get_time_for_mode('short_break'), 5 * 60)
        self.assertEqual(config.get_time_for_mode('long_break'), 15 * 60)
        self.assertEqual(config.get_time_for_mode('invalid'), 25 * 60)  # Default
    
    def test_get_color_for_mode(self):
        """Verifies that get_color_for_mode returns the correct colors."""
        config = Config(config_file="nonexistent.yaml")
        
        self.assertEqual(config.get_color_for_mode('work'), "#FF6B6B")
        self.assertEqual(config.get_color_for_mode('short_break'), "#4ECDC4")
        self.assertEqual(config.get_color_for_mode('long_break'), "#45B7D1")
        self.assertEqual(config.get_color_for_mode('invalid'), "#FF6B6B")  # Default


if __name__ == '__main__':
    unittest.main()
