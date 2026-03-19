# Diseño Técnico - Release 0.2: Migración GUI a Flet

## Referencia

- Especificaciones generales: #[[file:docs/ESPECIFICACIONES_es.md]]
- Spec v0.2: #[[file:docs/specs-by-version/spec-v0.2_es.md]]
- Plan v0.2: #[[file:docs/specs-by-version/PLAN_v0.2_es.md]]

## Arquitectura

### Estructura de archivos (cambios respecto a v0.1)

```
pomopy/
├── gui_flet.py              # NUEVO: GUI principal con Flet
├── gui.py                   # DEPRECADO: mantener temporalmente como fallback
├── components/
│   ├── __init__.py          # YA EXISTE (stub)
│   ├── timer_display.py     # YA EXISTE (stub) → implementar
│   ├── control_buttons.py   # YA EXISTE (stub) → implementar
│   ├── mode_selector.py     # YA EXISTE (stub) → implementar
│   ├── task_input.py        # YA EXISTE (stub) → implementar
│   └── stats_panel.py       # YA EXISTE (stub) → implementar
├── config.py                # YA ACTUALIZADO con theme/animations
├── pomodoro_manager.py      # SIN CAMBIOS
├── pomodoro_timer.py        # SIN CAMBIOS
├── sounds.py                # SIN CAMBIOS
└── tasks.py                 # SIN CAMBIOS

tests/
├── test_timer_display.py    # NUEVO
├── test_control_buttons.py  # NUEVO
├── test_mode_selector.py    # NUEVO
├── test_task_input.py       # NUEVO
├── test_stats_panel.py      # NUEVO
├── test_gui_flet.py         # NUEVO
└── (tests existentes sin cambios)

main.py                      # ACTUALIZAR: punto de entrada a Flet
```

### Diagrama de dependencias

```
main.py
  └── gui_flet.py (PomodoroApp)
        ├── Config
        ├── PomodoroManager
        │     ├── PomodoroTimer
        │     ├── TaskManager
        │     └── SoundManager
        └── Components (Flet)
              ├── TimerDisplay
              ├── ControlButtons
              ├── ModeSelector
              ├── TaskInput
              └── StatsPanel
```

## Diseño de componentes

### TimerDisplay (`pomopy/components/timer_display.py`)

Hereda de `ft.UserControl`. Muestra un `ft.Stack` con:
- `ft.ProgressRing` (progreso circular, valor 0.0-1.0)
- `ft.Text` centrado (tiempo en formato MM:SS, size=48, bold)

Métodos públicos:
- `update_time(time_text: str)` — actualiza el texto del reloj
- `update_progress(percentage: float)` — actualiza el anillo (0-100 → 0.0-1.0)
- `set_color(color: str)` — cambia el color del anillo según modo

### ControlButtons (`pomopy/components/control_buttons.py`)

Hereda de `ft.UserControl`. Muestra un `ft.Row` con:
- `ft.ElevatedButton` Start/Pause con icono PLAY_ARROW/PAUSE
- `ft.OutlinedButton` Reset con icono REFRESH

Estado interno `is_running` para toggle del botón.
Callbacks: `on_start_pause`, `on_reset`.

### ModeSelector (`pomopy/components/mode_selector.py`)

Hereda de `ft.UserControl`. Muestra un `ft.Row` con `ft.Chip` para cada modo:
- Work, Short Break, Long Break

Estado interno `current_mode`. Callback `on_mode_change(mode)`.

### TaskInput (`pomopy/components/task_input.py`)

Hereda de `ft.UserControl`. Muestra `ft.Column` con:
- `ft.TextField` (label "Task name")
- `ft.ElevatedButton` "✓ Complete" (disabled cuando campo vacío)

Callback `on_complete(task_name)`.

### StatsPanel (`pomopy/components/stats_panel.py`)

Hereda de `ft.UserControl`. Muestra `ft.Column` con filas de estadísticas:
- Pomodoros / Work time
- Short breaks / Break time
- Long breaks / Meeting time

Método `update_stats(stats: dict)`.

### gui_flet.py (PomodoroApp)

Clase principal que:
1. Configura la página Flet (título, dimensiones, tema)
2. Instancia `PomodoroManager` y todos los componentes
3. Construye el layout vertical con todos los componentes
4. Implementa los handlers: `toggle_timer`, `reset_timer`, `change_mode`, `complete_task`, `toggle_meeting`
5. Ejecuta `_tick()` cada segundo via threading o `page.run_task`
6. Gestiona el switch de tema oscuro/claro

### main.py (actualización)

Cambia de Tkinter a Flet:
```python
import flet as ft
from pomopy.gui_flet import main as flet_main

if __name__ == "__main__":
    ft.app(target=flet_main)
```

## Configuración (ya implementada en config.py)

Secciones añadidas en Fase 1:
- `theme.mode`: "dark" | "light"
- `theme.color_seed`: color base Material Design
- `animations.enabled`: bool
- `animations.duration`: ms
- `window.resizable`: bool

## Testing

Cada componente tiene su archivo de test en `tests/`. Los tests instancian los componentes sin necesidad de una página Flet real, verificando:
- Estado inicial correcto
- Métodos de actualización modifican el estado
- Callbacks se asignan correctamente

Los tests existentes (config, timer, manager, tasks, sounds) no se modifican.
