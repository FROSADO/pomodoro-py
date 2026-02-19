# Testing Guide - Pomodoro Timer

[Versión en Español](docs/TEST_es.md)

## Overview

The Pomodoro Timer application includes a comprehensive test suite with **107 unit tests** covering all modules.

## Test Structure

```
tests/
├── test_config.py              # Configuration tests (11 tests)
├── test_pomodoro_timer.py      # Timer logic tests (16 tests)
├── test_gui.py                 # GUI tests (21 tests)
├── test_sounds.py              # Sound management tests (19 tests)
├── test_tasks.py               # Task management tests (17 tests)
└── test_pomodoro_manager.py    # Business logic tests (23 tests)
```

## Running Tests

### All Tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

### Individual Modules

```bash
# Configuration
python -m tests.test_config

# Timer
python -m tests.test_pomodoro_timer

# GUI
python -m tests.test_gui

# Sounds
python -m tests.test_sounds

# Tasks
python -m tests.test_tasks

# Manager
python -m tests.test_pomodoro_manager
```

### Specific Test

```bash
python -m unittest tests.test_config.TestConfig.test_default_values
```

## Test Coverage

### test_config.py (11 tests)
- Default value initialization
- YAML file loading
- Time and color configuration
- Window and sound settings
- Helper methods

### test_pomodoro_timer.py (16 tests)
- Timer start/pause/reset
- Time countdown
- Finish callbacks
- Time formatting
- State management

### test_gui.py (21 tests)
- Widget creation
- Timer controls
- Mode switching
- Task entry
- Volume control
- Statistics display

### test_sounds.py (19 tests)
- Sound initialization
- Alarm playback
- Ticking sound
- Volume control
- File availability

### test_tasks.py (17 tests)
- Task creation
- Counter increments
- Task completion
- File persistence
- Time calculation

### test_pomodoro_manager.py (23 tests)
- Component integration
- Timer coordination
- Task management
- Sound control
- Statistics calculation

## Requirements

Tests use Python's built-in `unittest` framework. No additional dependencies required beyond the application's requirements.

## Writing Tests

### Test Template

```python
import unittest
from pomopy.module import Class

class TestClass(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.instance = Class()
    
    def tearDown(self):
        """Clean up after tests."""
        pass
    
    def test_feature(self):
        """Test description."""
        # Arrange
        expected = "value"
        
        # Act
        result = self.instance.method()
        
        # Assert
        self.assertEqual(result, expected)
```

### Best Practices

1. **One assertion per test** when possible
2. **Descriptive test names** that explain what is being tested
3. **Use setUp/tearDown** for common initialization/cleanup
4. **Test edge cases** and error conditions
5. **Keep tests independent** - no test should depend on another

## Continuous Integration

Tests are designed to run in CI/CD environments:

```yaml
# Example GitHub Actions workflow
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - run: pip install -r requirements.txt
      - run: python -m unittest discover -s tests -p "test_*.py"
```

## Troubleshooting

### Tests Failing

**Problem:** Tests fail unexpectedly

**Solutions:**
1. Ensure all dependencies are installed: `pip install -r requirements.txt`
2. Run from project root directory
3. Check Python version (3.8+)
4. Verify no config.yaml in test directory

### Import Errors

**Problem:** Module not found errors

**Solutions:**
1. Run tests as modules: `python -m tests.test_name`
2. Ensure `__init__.py` exists in tests directory
3. Check PYTHONPATH includes project root

### GUI Tests Hanging

**Problem:** GUI tests don't complete

**Solutions:**
1. Tests use Tkinter - ensure display is available
2. On headless systems, use Xvfb
3. Tests properly destroy Tk instances in tearDown

## Test Metrics

- **Total tests**: 107
- **Coverage**: ~95% of critical functionality
- **Average execution time**: < 5 seconds
- **Modules tested**: 6

## See Also

- [README.md](README.md) - General documentation
- [CONFIG.md](docs/CONFIG.md) - Configuration guide
