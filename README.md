# Pomodoro Timer - Desktop Application

Desktop application developed in Python to implement the Pomodoro time management technique.

[Versión en Español](README_es.md)

***IMPORTANT***: This project was started as part of a personal exercise in using Generative AI (Amazon Q with Claude Sonnet 4 / 4.5). With this project, I aim to evaluate the cost in terms of time and effort to achieve a viable, maintainable, and functional project. I will publish the conclusions soon on my blog or in this project itself.

I need to clarify some points if you intend to use this project:
- The code is 99% AI-generated. At least until version 1.0.
- If the result meets my quality expectations, I may start maintaining it. But until version 1.0, I don't intend to introduce a single line of code manually.
- At no time does the application intend to do anything destructive or harmful to your system, so I doubt it's unsafe to use. However, I don't guarantee the application's security.
- For this reason, I decided not to make a web application, but a desktop one, to avoid external attack vectors in case of vulnerability.
- Most of my interactions with the AI are using the prompt and the specification file(s) [Technical Specifications - Pomodoro Timer Application](docs/ESPECIFICACIONES_en.md).
- Improvement requests are accepted, but as part of my project, the AI will generate the code. (at least until version 1.0)


## What is the Pomodoro Technique?

The Pomodoro Technique is a time management method that uses work intervals (pomodoros) of 25 minutes, separated by short breaks of 5 minutes. After 4 pomodoros, a longer break of 15 minutes is taken.

## Features

- ⏱️ Timer with visual countdown
- 🎨 Differentiated colors for each mode (Work/Break)
- ⏯️ Start/Pause/Reset controls
- 🔄 Quick mode switching
- ⏰ Sound alarm that plays 5 times when finished
- 🔊 Ticking sound during work periods
- 🔉 Adjustable volume control
- 📝 Task management with pomodoro tracking
- 💾 Persistence of completed tasks in daily files
- 🤝 Meeting time tracking
- ⚙️ Customizable configuration via YAML file
- 🪟 Always-on-top window

## Requirements

- Python 3.8 or higher
- PyYAML (automatically installed with requirements.txt)
- pygame (automatically installed with requirements.txt)
- Alarm file: `assets/alarm-digital.mp3` (included in project)
- Ticking file: `assets/ticking-slow.mp3` (included in project)

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd pomodoro-py
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Starting the Application

```bash
python main.py
```

### Basic Controls

1. **Start/Pause**: Starts or pauses the current timer
2. **Reset**: Resets the timer to the initial time of the current mode
3. **Work**: Switches to work mode (25 minutes by default)
4. **Short Break**: Switches to short break (5 minutes by default)
5. **Long Break**: Switches to long break (15 minutes by default)
6. **Task field**: Write your task name and press Enter
7. **✓ Complete**: Completes and saves the current task (activates when typing text)
8. **MEETING**: Starts/stops meeting time tracking
9. **Volume control**: Adjusts sound volume (0-100)

### Recommended Workflow

1. Start the application (Work mode by default)
2. Adjust volume according to your preference using the slider
3. Write your task name in the text field
4. Press "Start" to begin your pomodoro
5. Work until the timer reaches 00:00 (counter increments automatically)
6. Switch to "Short Break" and press "Start"
7. Rest for 5 minutes (break counter increments automatically)
8. Repeat the cycle
9. After 4 pomodoros, take a "Long Break"
10. When finishing the task, press "✓ Complete" to save it (automatically pauses timer and saves counters)
11. For meetings, press "MEETING" to start tracking time, press "END MEETING" to save

For more details on task management, see [TASKS.md](docs/TASKS.md).

## Configuration

The application uses default values, but you can customize them by creating a `config.yaml` file in the application directory.

### Creating Configuration File

1. Copy the `config.yaml.example` file and rename it to `config.yaml`
2. Edit the values according to your preferences
3. Restart the application

### Configuration Example

```yaml
# Times in minutes
times:
  work_time: 25
  short_break: 5
  long_break: 15

# Colors (hexadecimal format)
colors:
  work_color: "#FF6B6B"
  short_break_color: "#4ECDC4"
  long_break_color: "#45B7D1"

# Window
window:
  width: 400
  height: 500
  always_on_top: true

# Sound
sound:
  enabled: true
  alarm_file: "assets/alarm-digital.mp3"
  ticking_file: "assets/ticking-slow.mp3"
```

For more configuration details, see [CONFIG.md](docs/CONFIG.md).

## Project Structure

```
pomodoro-py/
├── main.py                    # Entry point
├── pomopy/                    # Source code
│   ├── config.py              # Configuration management
│   ├── gui.py                 # Graphical interface
│   ├── pomodoro_manager.py    # Business logic coordination
│   ├── pomodoro_timer.py      # Timer logic
│   ├── sounds.py              # Sound management
│   └── tasks.py               # Task management
├── tests/                     # Unit tests
│   ├── test_config.py
│   ├── test_gui.py
│   ├── test_pomodoro_manager.py
│   ├── test_pomodoro_timer.py
│   ├── test_sounds.py
│   └── test_tasks.py
├── assets/                    # Application resources
│   ├── alarm-digital.mp3      # Alarm sound file
│   └── ticking-slow.mp3       # Ticking sound file
├── records/                   # Daily task files
├── requirements.txt           # Dependencies
├── config.yaml.example        # Configuration template
├── README.md                  # This file
├── CONFIG.md                  # Configuration guide
├── TEST.md                    # Testing guide
├── TASKS.md                   # Task management guide
└── ESPECIFICACIONES.md        # Technical specifications
```

## Development

### Running Tests

```bash
# Configuration tests
python -m tests.test_config

# Timer tests
python -m tests.test_pomodoro_timer

# GUI tests
python -m tests.test_gui

# Sound management tests
python -m tests.test_sounds

# Task management tests
python -m tests.test_tasks

# Business logic manager tests
python -m tests.test_pomodoro_manager

# All tests
python -m unittest discover -s tests -p "test_*.py"
```

For more information on tests, see [TEST.md](docs/TEST.md).

## Project Status

### ✅ Completed

- [x] Configuration module
- [x] Timer logic
- [x] Graphical interface (GUI)
- [x] GUI + Timer integration
- [x] Unit tests (90 tests: config, timer, sounds, tasks, manager)
- [x] Complete documentation
- [x] Functional application
- [x] Sound alarm (plays 5 times when finished)
- [x] Task management with persistence in daily files
- [x] Adjustable volume control
- [x] Meeting time tracking
- [x] Statistics display (pomodoros, breaks, work time, break time, meeting time)

### 📋 Planned

- [ ] Visualization of completed tasks from daily files
- [ ] Graphical statistics and charts
- [ ] Standalone executable (PyInstaller)

## Contributing

Contributions are welcome. Please:

1. Ensure all tests pass
2. Add tests for new features
3. Update documentation as needed

## License

This project is open source and available under the MIT License.

## Support

To report issues or suggest improvements, please open an issue in the project repository.

## Credits

Developed as a productivity tool based on the Pomodoro Technique created by Francesco Cirillo.
