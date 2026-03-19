# Guía de Migración v0.1 → v0.2: Tkinter a Flet

## Resumen

La versión 0.2 migra la interfaz gráfica de Tkinter a [Flet](https://flet.dev/) (Flutter para Python), manteniendo intacta la lógica de negocio (`PomodoroManager`, `PomodoroTimer`, `TaskManager`, `SoundManager`).

## Cambios de Arquitectura

### Antes (v0.1)

```
main.py → tk.Tk() → PomodoroApp(root, config)
                         ├── Tkinter widgets directos en gui.py
                         └── PomodoroManager (lógica de negocio)
```

- GUI monolítica en `pomopy/gui.py` (~380 líneas)
- Widgets Tkinter creados en `_create_widgets()`
- Loop de actualización via `root.after(1000, self._tick)`
- Punto de entrada: `root.mainloop()`

### Después (v0.2)

```
main.py → ft.app(target=main) → PomodoroApp(page, config)
                                      ├── Componentes Flet en pomopy/components/
                                      │     ├── TimerDisplay
                                      │     ├── ControlButtons
                                      │     ├── ModeSelector
                                      │     ├── TaskInput
                                      │     └── StatsPanel
                                      └── PomodoroManager (sin cambios)
```

- GUI modular en `pomopy/gui_flet.py` + 5 componentes independientes
- Cada componente hereda de `ft.UserControl` con su propio `build()`
- Loop de actualización via `page.run_task` o `threading.Timer`
- Punto de entrada: `ft.app(target=main)`

### Módulos sin cambios

Estos módulos no se modifican en la migración:

| Módulo | Descripción |
|--------|-------------|
| `pomopy/config.py` | Ya actualizado en Fase 1 (theme, animations) |
| `pomopy/pomodoro_manager.py` | Lógica de negocio, misma API |
| `pomopy/pomodoro_timer.py` | Timer, misma API |
| `pomopy/tasks.py` | Gestión de tareas, misma API |
| `pomopy/sounds.py` | Sonidos, misma API |

## Diferencias de API: Tkinter vs Flet

### Punto de entrada

```python
# v0.1 (Tkinter)
root = tk.Tk()
config = Config()
app = PomodoroApp(root, config)
app.run()  # root.mainloop()

# v0.2 (Flet)
import flet as ft
def main(page: ft.Page):
    app = PomodoroApp(page, Config())
ft.app(target=main)
```

### Configuración de ventana

```python
# v0.1 (Tkinter)
self.root.title("Pomodoro Timer")
self.root.geometry(f"{width}x{height}")
self.root.resizable(False, False)
self.root.attributes('-topmost', config.ALWAYS_ON_TOP)

# v0.2 (Flet)
self.page.title = "Pomodoro Timer"
self.page.window_width = config.WINDOW_WIDTH
self.page.window_height = config.WINDOW_HEIGHT
self.page.window_resizable = config.WINDOW_RESIZABLE
self.page.window_always_on_top = config.ALWAYS_ON_TOP
self.page.theme_mode = ft.ThemeMode.DARK  # Nuevo en v0.2
```

### Widgets → Componentes

| Tkinter (v0.1) | Flet (v0.2) | Notas |
|-----------------|-------------|-------|
| `tk.Label` (modo) | `ft.Text` | size, weight, color |
| `tk.Label` (reloj) | `TimerDisplay` (componente) | ProgressRing + Text |
| `tk.Button` Start/Reset | `ControlButtons` (componente) | ElevatedButton + OutlinedButton |
| `tk.Button` Work/Break | `ModeSelector` (componente) | ft.Chip |
| `tk.Entry` + `tk.Button` | `TaskInput` (componente) | TextField + ElevatedButton |
| `tk.Label` × N (stats) | `StatsPanel` (componente) | Column con Rows |
| `tk.Scale` (volumen) | `ft.Slider` | min/max/value/on_change |
| N/A | `ft.Switch` (tema) | Nuevo en v0.2 |

### Actualización del display

```python
# v0.1 (Tkinter) - callback con root.after
def _tick(self):
    if self.manager.is_running():
        self.manager.tick()
        self._update_display()
    self.root.after(1000, self._tick)

# v0.2 (Flet) - async o threading
async def _tick(self):
    while True:
        if self.manager.is_running():
            self.manager.tick()
            self.timer_display.update_time(self.manager.get_time_formatted())
            self.timer_display.update_progress(percentage)
            self.page.update()
        await asyncio.sleep(1)
```

### Colores y temas

```python
# v0.1 (Tkinter) - colores manuales por widget
self.root.configure(bg=color)
self.time_label.configure(bg=color, fg=text_color)

# v0.2 (Flet) - Material Design automático
self.page.theme_mode = ft.ThemeMode.DARK  # o LIGHT
self.page.theme = ft.Theme(color_scheme_seed=config.COLOR_SEED)
# Los colores de modo se aplican solo al ProgressRing y contenedores específicos
```

### Notificaciones

```python
# v0.1 (Tkinter) - solo alarma sonora
self.sound_manager.play_alarm(times=5)

# v0.2 (Flet) - alarma + SnackBar + Banner
self.sound_manager.play_alarm(times=5)
self.page.snack_bar = ft.SnackBar(ft.Text("Timer finished!"))
self.page.snack_bar.open = True
self.page.update()
```

## Estructura de archivos nueva

```
pomopy/
├── gui_flet.py              # NUEVO: GUI principal Flet
├── gui.py                   # DEPRECADO: mantener como fallback
├── components/
│   ├── __init__.py
│   ├── timer_display.py     # ProgressRing + Text
│   ├── control_buttons.py   # Start/Pause + Reset
│   ├── mode_selector.py     # Chips Work/Break
│   ├── task_input.py        # TextField + Complete
│   └── stats_panel.py       # Estadísticas
└── (resto sin cambios)

tests/
├── test_timer_display.py    # NUEVO
├── test_control_buttons.py  # NUEVO
├── test_mode_selector.py    # NUEVO
├── test_task_input.py       # NUEVO
├── test_stats_panel.py      # NUEVO
├── test_gui_flet.py         # NUEVO
└── (tests existentes sin cambios)
```

## Configuración nueva (config.yaml)

Secciones añadidas en v0.2:

```yaml
# Tema (Flet)
theme:
  mode: "dark"         # "dark" o "light"
  color_seed: "blue"   # Color base Material Design

# Animaciones (Flet)
animations:
  enabled: true        # Habilitar/deshabilitar animaciones
  duration: 300        # Duración en milisegundos

# Ventana (actualizado)
window:
  resizable: false     # Permitir redimensionar ventana
```

## Dependencias

```
# Nuevas en v0.2
flet==0.82.0

# Sin cambios
PyYAML==6.0.1
pygame==2.6.1
coverage==7.13.4
```

Instalar: `pip install -r requirements.txt`

## Guía de actualización para desarrolladores

1. Instalar nueva dependencia: `pip install flet==0.82.0`
2. Los cambios en lógica de negocio se hacen en `PomodoroManager` (sin cambios en la API)
3. Para modificar la UI, editar los componentes en `pomopy/components/` o `pomopy/gui_flet.py`
4. `pomopy/gui.py` (Tkinter) se mantiene temporalmente y se eliminará en v0.3
5. Los tests de componentes Flet instancian las clases directamente sin necesidad de una página Flet real
6. Ejecutar tests: `python -m unittest discover -s tests -p "test_*.py"`

## Notas importantes

- La lógica de negocio (`PomodoroManager`) no cambia. La migración es exclusivamente de la capa de presentación.
- `gui.py` (Tkinter) se mantiene como fallback durante la transición. Se eliminará en v0.3.
- Los builds con PyInstaller necesitarán flags adicionales para Flet (`--collect-all=flet`).
