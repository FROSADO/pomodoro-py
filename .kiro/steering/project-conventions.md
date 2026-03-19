---
inclusion: always
---

# Pomodoro Timer - Project Conventions

## Project Overview
Desktop Pomodoro timer app built in Python with Tkinter GUI. Manages work/break cycles, task tracking, meeting time logging, and sound notifications.

## Language & Style
- Python 3.8+ compatibility required
- Documentation and code comments are bilingual (Spanish/English mix). Docstrings use English verbs with Spanish descriptions.
- Config class attributes use UPPER_SNAKE_CASE
- Module-level docstrings in Spanish: `"""Module de ... para la aplicación Pomodoro Timer."""`
- Method docstrings follow Google style with `Args:` and `Returns:` sections

## Architecture
- Source code lives in `pomopy/` package, UI components in `pomopy/components/`
- `pomopy/config.py` — Config class loads defaults + optional `config.yaml` overrides via PyYAML
- `pomopy/pomodoro_timer.py` — Timer logic (tick, start, pause, reset)
- `pomopy/pomodoro_manager.py` — Business logic coordinator (integrates timer, tasks, sounds)
- `pomopy/gui.py` — Tkinter GUI (no business logic, delegates to manager)
- `pomopy/sounds.py` — SoundManager wraps pygame.mixer with graceful fallback
- `pomopy/tasks.py` — TaskManager handles task persistence in daily files under `records/`
- `main.py` — Entry point, creates Tk root, Config, and PomodoroApp

## Configuration
- All configurable values have defaults in the `Config` class
- Users override via `config.yaml` (not committed — in `.gitignore`)
- `config.example.yaml` is the committed template
- Config sections: times, colors, window, sound, tasks, theme, animations
- Times are stored in seconds internally, configured in minutes via YAML

## Testing
- Tests live in `tests/` using `unittest`
- Test files: `test_config.py`, `test_pomodoro_timer.py`, `test_gui.py`, `test_sounds.py`, `test_tasks.py`, `test_pomodoro_manager.py`
- Run all: `python -m unittest discover -s tests -p "test_*.py"`
- Run single: `python -m tests.test_config`
- No external test framework (no pytest) — pure unittest

## Dependencies
- PyYAML — config loading
- pygame — sound playback
- coverage — test coverage
- flet — UI framework (components in `pomopy/components/`)
- Tkinter — current main GUI (stdlib)

## File Conventions
- Daily task records: `records/YYYYMMDD.txt`
- Task line format: `"TaskName" | pomodoros | short_breaks | long_breaks | HH:mm:ss | HH:mm:ss`
- Assets (sounds): `assets/` directory
- Build scripts at project root: `build_windows.py`, `build_linux.py`, `build_deb.py`, `build_rpm.py`
- CI/CD: `.github/workflows/build-release.yml`

## Key Patterns
- `get_resource_path()` in config.py resolves paths for both dev and PyInstaller builds
- SoundManager checks `PYGAME_AVAILABLE` flag before any pygame calls
- TaskManager calculates total time from counters × configured durations (not wall clock)
- Meetings are stored as special `"REUNION"` tasks with zero pomodoro/break counts
