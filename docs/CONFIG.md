# Configuration Guide - Pomodoro Timer

[Versión en Español](CONFIG_es.md)

## Overview

The Pomodoro Timer application uses default values but allows full customization through a `config.yaml` file.

## Quick Start

1. Copy `config.yaml.example` to `config.yaml`
2. Edit the values you want to change
3. Restart the application

## Configuration File

The configuration file uses YAML format and is divided into sections:

### Times

Configure the duration of each period in **minutes**:

```yaml
times:
  work_time: 25        # Work period duration (default: 25)
  short_break: 5       # Short break duration (default: 5)
  long_break: 15       # Long break duration (default: 15)
```

### Colors

Customize interface colors in hexadecimal format:

```yaml
colors:
  work_color: "#FF6B6B"           # Work mode color (default: light red)
  short_break_color: "#4ECDC4"    # Short break color (default: teal)
  long_break_color: "#45B7D1"     # Long break color (default: light blue)
  bg_color: "#2C3E50"             # Background color (default: dark gray)
  text_color: "#FFFFFF"           # Text color (default: white)
```

### Window

Configure window appearance:

```yaml
window:
  width: 400           # Window width in pixels (default: 400)
  height: 500          # Window height in pixels (default: 500)
  always_on_top: true  # Keep window always visible (default: true)
```

### Sound

Configure audio notifications:

```yaml
sound:
  enabled: true        # Enable/disable sound notifications (default: true)
  alarm_file: "assets/alarm-digital.mp3"    # Alarm file (default: assets/alarm-digital.mp3)
  ticking_file: "assets/ticking-slow.mp3"   # Ticking sound file (default: assets/ticking-slow.mp3)
```

### Tasks

Configure task file location:

```yaml
tasks:
  file: "tasks.txt"    # File where completed tasks are saved (default: tasks.txt)
```

## Complete Example

```yaml
# Complete configuration file example
times:
  work_time: 25
  short_break: 5
  long_break: 15

colors:
  work_color: "#FF6B6B"
  short_break_color: "#4ECDC4"
  long_break_color: "#45B7D1"
  bg_color: "#2C3E50"
  text_color: "#FFFFFF"

window:
  width: 400
  height: 500
  always_on_top: true

sound:
  enabled: true
  alarm_file: "assets/alarm-digital.mp3"
  ticking_file: "assets/ticking-slow.mp3"

tasks:
  file: "tasks.txt"
```

## Default Values

If no configuration file exists or a value is not specified, these defaults are used:

- **Work time**: 25 minutes
- **Short break**: 5 minutes
- **Long break**: 15 minutes
- **Work color**: #FF6B6B (light red)
- **Short break color**: #4ECDC4 (teal)
- **Long break color**: #45B7D1 (light blue)
- **Background**: #2C3E50 (dark gray)
- **Text**: #FFFFFF (white)
- **Window**: 400x500 pixels
- **Always on top**: Yes
- **Sound**: Enabled
- **Alarm file**: assets/alarm-digital.mp3
- **Ticking file**: assets/ticking-slow.mp3
- **Tasks file**: tasks.txt

## Tips

### Custom Times

Adjust times to your work style:
- **Short sessions**: 15-20 minutes work, 3-5 minutes break
- **Standard**: 25 minutes work, 5 minutes break (recommended)
- **Long sessions**: 45-50 minutes work, 10-15 minutes break

### Color Themes

**Dark theme** (default):
```yaml
colors:
  bg_color: "#2C3E50"
  text_color: "#FFFFFF"
```

**Light theme**:
```yaml
colors:
  bg_color: "#ECF0F1"
  text_color: "#2C3E50"
```

### Custom Sounds

Replace audio files with your own:
1. Place your MP3 files in the `assets/` folder
2. Update the configuration:
```yaml
sound:
  alarm_file: "assets/my-alarm.mp3"
  ticking_file: "assets/my-ticking.mp3"
```

## Troubleshooting

### Configuration not loading

**Problem**: Changes don't take effect

**Solutions**:
1. Verify the file is named exactly `config.yaml`
2. Check YAML syntax (indentation with spaces, not tabs)
3. Restart the application
4. Check console for error messages

### Invalid colors

**Problem**: Colors don't display correctly

**Solutions**:
1. Use hexadecimal format: `"#RRGGBB"`
2. Include quotes around the value
3. Use valid hex values (0-9, A-F)

### Sound files not found

**Problem**: Sounds don't play

**Solutions**:
1. Verify files exist in `assets/` folder
2. Check file names match configuration
3. Ensure files are valid MP3 format
4. Use relative paths from project root

## Advanced Configuration

### Multiple Configurations

Create different configuration files for different scenarios:

```bash
# Work configuration
config-work.yaml

# Study configuration
config-study.yaml

# Relaxed configuration
config-relaxed.yaml
```

Load specific configuration by renaming the desired file to `config.yaml`.

### Portable Configuration

To make the application portable:
1. Keep all paths relative
2. Include audio files in `assets/`
3. Use `tasks.txt` in the same directory

## See Also

- [README.md](README.md) - General documentation
- [TASKS.md](TASKS.md) - Task management guide
- [TEST.md](TEST.md) - Testing guide
