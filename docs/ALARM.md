# Sound and Alarm Guide - Pomodoro Timer

[Versión en Español](ALARM_es.md)

## Overview

The Pomodoro Timer includes two types of sounds:
1. **Alarm**: Plays when a period (work or break) finishes
2. **Ticking**: Continuous sound during work periods

## Alarm Sound

### Behavior

- Plays **5 times** when timer reaches 00:00
- 2-second interval between repetitions
- Plays for both work periods and breaks
- Can be disabled in configuration

### Configuration

```yaml
sound:
  enabled: true
  alarm_file: "assets/alarm-digital.mp3"
```

### Custom Alarm

To use your own alarm sound:

1. Place your MP3 file in the `assets/` folder
2. Update `config.yaml`:
```yaml
sound:
  alarm_file: "assets/my-custom-alarm.mp3"
```
3. Restart the application

## Ticking Sound

### Behavior

- Plays continuously during work periods only
- Stops when:
  - Timer is paused
  - Timer is reset
  - Mode is changed
  - Timer finishes
- Does NOT play during breaks

### Configuration

```yaml
sound:
  ticking_file: "assets/ticking-slow.mp3"
```

### Custom Ticking

To use your own ticking sound:

1. Place your MP3 file in the `assets/` folder
2. Update `config.yaml`:
```yaml
sound:
  ticking_file: "assets/my-ticking.mp3"
```
3. Restart the application

## Volume Control

### Adjusting Volume

- Use the slider at the bottom of the window
- Range: 0-100
- Affects both alarm and ticking sounds
- Changes take effect immediately

### Configuration

Volume is controlled through the GUI and is not saved in configuration.

## Disabling Sounds

### Disable All Sounds

```yaml
sound:
  enabled: false
```

### Disable Only Ticking

Keep alarm but remove ticking:
```yaml
sound:
  ticking_file: ""
```

### Disable Only Alarm

Not directly supported, but you can:
1. Set volume to 0 using the slider
2. Or replace alarm file with a silent MP3

## Audio File Requirements

### Format
- **Required**: MP3 format
- **Recommended**: 
  - Sample rate: 44.1 kHz
  - Bitrate: 128-320 kbps
  - Mono or stereo

### File Size
- Alarm: Recommended < 1 MB
- Ticking: Recommended < 500 KB (will loop)

### Duration
- Alarm: 1-3 seconds recommended
- Ticking: 1-5 seconds (will loop seamlessly)

## Troubleshooting

### No Sound Playing

**Problem:** Sounds don't play

**Solutions:**
1. Check `sound.enabled` is `true` in config
2. Verify audio files exist in `assets/` folder
3. Ensure files are valid MP3 format
4. Check system volume is not muted
5. Verify pygame is installed: `pip install pygame`

### Ticking Not Stopping

**Problem:** Ticking continues after pause

**Solutions:**
1. This is a bug - report it
2. Restart the application
3. Change mode to stop ticking

### Alarm Too Loud/Quiet

**Problem:** Volume is not appropriate

**Solutions:**
1. Use the volume slider in the application
2. Adjust system volume
3. Edit the MP3 file to change its base volume

### Choppy Sound

**Problem:** Sound stutters or skips

**Solutions:**
1. Use lower bitrate MP3 files
2. Close other applications using audio
3. Check CPU usage

## Finding Sound Files

### Free Sound Resources

- **Freesound.org**: Creative Commons sounds
- **Zapsplat.com**: Free sound effects
- **Incompetech.com**: Royalty-free music

### Creating Custom Sounds

1. Record or generate your sound
2. Export as MP3
3. Keep duration short (1-5 seconds)
4. Test in the application

## Technical Details

### Sound System

- Uses **pygame.mixer** for audio playback
- Supports MP3, OGG, WAV formats (MP3 recommended)
- Single channel for music (alarm and ticking share)
- Volume range: 0.0 to 1.0 internally (0-100 in GUI)

### Alarm Implementation

```python
# Plays 5 times with 2-second intervals
sound_manager.play_alarm(times=5, interval=2000)
```

### Ticking Implementation

```python
# Infinite loop playback
pygame.mixer.music.play(-1)
```

## See Also

- [README.md](README.md) - General documentation
- [CONFIG.md](CONFIG.md) - Configuration guide
