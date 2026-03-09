# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### In Development
- Migration to Flet for modern interface
- Material Design 3
- Reactive components

---

## [0.2.0] - [Pending]

### Added
- Modern interface with Flet (Flutter for Python)
- Integrated Material Design 3
- Animated ProgressRing for timer visualization
- SnackBar for task completion notifications
- Visual banner when timer finishes
- Reusable modular components (TimerDisplay, ControlButtons, ModeSelector, TaskInput, StatsPanel)
- Dark/light theme switch with animated transition
- Native Flutter animations
- Multiplatform support (Windows, Linux, macOS, Web)
- Individual tests per component

### Changed
- Complete migration from Tkinter to Flet
- Reactive component architecture
- Significant visual experience improvement
- Responsive layout with Material Design
- Folder structure with `pomopy/components/`

### Deprecated
- `gui.py` (Tkinter) - Will be removed in v0.3.0

### Fixed
- [Pending: List of bugs fixed during development]

---

## [0.1.5] - 2024-03-06

### Added
- Functional Pomodoro Timer application with Tkinter
- Countdown timer for work and breaks
- Modes: Work (25 min), Short Break (5 min), Long Break (15 min)
- Meeting mode with incremental time
- Controls: Start/Pause, Reset
- Task management with input field
- Button to complete tasks
- Task persistence in daily files (`records/YYYYMMDD.txt`)
- Session statistics (pomodoros, breaks, times)
- Adjustable volume control (0-100)
- Configurable sound alarm (plays 5 times)
- Ticking sound during work periods
- Configuration via `config.yaml` file
- Configurable always-on-top window
- Differentiated colors per mode
- Module system: config, timer, gui, sounds, tasks, manager
- 101 unit tests distributed across 6 modules
- Complete documentation (README, CONFIG, TEST, TASKS, ALARM)
- Distribution scripts for Windows, Linux, .deb and .rpm
- CI/CD with GitHub Actions
- Support for Windows 10/11 and Linux

### Technical Details
- Python 3.8+
- Tkinter for GUI
- PyYAML 6.0.1 for configuration
- pygame 2.5.2 for sounds
- Modular architecture with separation of concerns
- PomodoroManager for business logic coordination
- TaskManager for task management and persistence
- SoundManager for audio management

---

## Change Types

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Features that will be removed
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security fixes

---

## Links

- [0.2.0]: Pending release
- [0.1.5]: https://github.com/[user]/pomodoro-py/releases/tag/v0.1.5
