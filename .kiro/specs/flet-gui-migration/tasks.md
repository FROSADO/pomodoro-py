# Tareas - Release 0.2: Migración GUI a Flet

Basado en #[[file:docs/specs-by-version/PLAN_v0.2_es.md]]

## Fase 1: Preparación y Configuración

- [x] 1. Preparación del proyecto
  - [x] 1.1 Añadir `flet==0.82.0` a `requirements.txt` y verificar instalación
  - [x] 1.2 Crear estructura `pomopy/components/` con `__init__.py` y archivos stub para los 5 componentes (timer_display, control_buttons, mode_selector, task_input, stats_panel)
  - [x] 1.3 Añadir atributos THEME_MODE, COLOR_SEED, ANIMATIONS_ENABLED, ANIMATION_DURATION y WINDOW_RESIZABLE a la clase Config en `pomopy/config.py`, con carga desde YAML (secciones theme, animations, window.resizable)
  - [x] 1.4 Actualizar `config.example.yaml` con las nuevas secciones theme, animations y window.resizable
  - [x] 1.5 Añadir tests `test_load_custom_theme` y `test_load_custom_animations` en `tests/test_config.py`
  - [x] 1.6 Crear `docs/MIGRATION_v0.2_es.md` documentando cambios de arquitectura Tkinter→Flet, diferencias de API y guía de actualización

## Fase 2: Componentes Flet Base (RF-3, RF-5)

- [ ] 2. Implementar componentes Flet
  - [ ] 2.1 Implementar `TimerDisplay` en `pomopy/components/timer_display.py`: clase hereda `ft.UserControl`, método `build()` retorna `ft.Stack` con `ft.ProgressRing` (value 0.0-1.0, stroke_width=10, 200x200) y `ft.Text` centrado (size=48, bold). Métodos públicos: `update_time(time_text)`, `update_progress(percentage)` (0-100→0.0-1.0), `set_color(color)`. Crear `tests/test_timer_display.py` con tests para init, update_time, update_progress y set_color.
  - [ ] 2.2 Implementar `ControlButtons` en `pomopy/components/control_buttons.py`: clase hereda `ft.UserControl`, `build()` retorna `ft.Row` con `ft.ElevatedButton` Start/Pause (icono PLAY_ARROW/PAUSE, toggle via `_handle_start_pause`) y `ft.OutlinedButton` Reset (icono REFRESH). Estado `is_running` para toggle. Callbacks `on_start_pause`, `on_reset`. Crear `tests/test_control_buttons.py` con tests para init (is_running=False) y asignación de callbacks.
  - [ ] 2.3 Implementar `ModeSelector` en `pomopy/components/mode_selector.py`: clase hereda `ft.UserControl`, `build()` retorna `ft.Row` con 3 `ft.Chip` (Work, Short Break, Long Break). Estado `current_mode`. Método `_change_mode(mode)` actualiza estado y llama `on_mode_change(mode)`. Crear `tests/test_mode_selector.py` con tests para init (current_mode='work') y cambio de modo.
  - [ ] 2.4 Implementar `TaskInput` en `pomopy/components/task_input.py`: clase hereda `ft.UserControl`, `build()` retorna `ft.Column` con `ft.TextField` (label "Task name", width=300) y `ft.ElevatedButton` "✓ Complete" (disabled cuando campo vacío). `_on_change` habilita/deshabilita botón. `_handle_complete` llama `on_complete(task_name)` y limpia campo. Crear `tests/test_task_input.py` con tests para init y callback.
  - [ ] 2.5 Implementar `StatsPanel` en `pomopy/components/stats_panel.py`: clase hereda `ft.UserControl`, `build()` retorna `ft.Column` con filas: Pomodoros/Work time, Short breaks/Break time, Long breaks/Meeting time. Método `update_stats(stats)` actualiza dict interno. Crear `tests/test_stats_panel.py` con tests para init (valores en 0) y update_stats.

## Fase 3: GUI Principal con Flet (RF-1, RF-2, RF-4)

- [ ] 3. Crear GUI principal y conectar componentes
  - [ ] 3.1 Crear `pomopy/gui_flet.py` con clase `PomodoroApp(page, config)`: en `__init__` instanciar `PomodoroManager(config)`, llamar `_setup_page()` (título, dimensiones, tema desde config), `_create_components()` (los 5 componentes + `ft.Switch` para tema + `ft.Slider` para volumen), `_build_layout()` (Column vertical con todos los elementos).
  - [ ] 3.2 Implementar `toggle_timer(e)`: si `manager.is_running()` llamar `manager.pause_timer()`, sino `manager.start_timer()`. Actualizar texto/icono del botón via `control_buttons`. Implementar `reset_timer(e)`: llamar `manager.reset_timer()`, actualizar display y resetear botón a "Start".
  - [ ] 3.3 Implementar `change_mode(mode)`: llamar `manager.change_mode(mode)`, actualizar `timer_display` con nuevo tiempo y color (`config.get_color_for_mode(mode)`), resetear botón a "Start".
  - [ ] 3.4 Implementar `complete_task(task_name)`: llamar `manager.set_task(task_name)` y `manager.complete_task()`, mostrar `ft.SnackBar` con confirmación, actualizar stats panel.
  - [ ] 3.5 Implementar `toggle_meeting(e)`: toggle entre modo reunión (timer incremental) y modo normal. Cuando activo, incrementar `manager.increment_meeting_time()` cada segundo. Al terminar, llamar `manager.save_meeting()`.
  - [ ] 3.6 Implementar `_tick()`: cada segundo llamar `manager.tick()`, actualizar `timer_display.update_time()` y `timer_display.update_progress()` (porcentaje = tiempo transcurrido / tiempo total del modo). Usar `page.run_task` o `threading.Timer` para el loop.
  - [ ] 3.7 Implementar `_toggle_theme(e)`: cambiar `page.theme_mode` entre DARK/LIGHT según switch. Implementar `_on_volume_change(e)`: llamar `manager.set_volume(value/100.0)`.
  - [ ] 3.8 Actualizar `main.py`: cambiar import a `from pomopy.gui_flet import main as flet_main`, punto de entrada `ft.app(target=flet_main)`. Mantener `pomopy/gui.py` sin cambios como fallback.

## Fase 4: Animaciones y Efectos (RF-6, RF-7)

- [ ] 4. Añadir animaciones y feedback visual
  - [ ] 4.1 Envolver el contenedor principal del timer en `ft.AnimatedContainer` con `animate=ft.Animation(duration=config.ANIMATION_DURATION)` para transiciones de color suaves al cambiar de modo. Respetar `config.ANIMATIONS_ENABLED` (si False, sin animaciones).
  - [ ] 4.2 Implementar `ft.SnackBar` al completar tareas (mostrar nombre de tarea guardada) y `ft.Banner` al terminar timer (con botón para cerrar y texto del modo completado).
  - [ ] 4.3 Implementar botón MEETING con toggle visual: texto cambia entre "MEETING" / "END MEETING", color cambia a `config.MEETING_COLOR` cuando activo.
  - [ ] 4.4 Aplicar `ft.Card` con elevation en el panel de estadísticas y en el contenedor del timer para efecto Material Design.

## Fase 5: Testing y Refinamiento (RNF-4)

- [ ] 5. Testing completo y corrección de bugs
  - [ ] 5.1 Crear `tests/test_gui_flet.py` con tests de integración: verificar que `PomodoroApp` se instancia sin errores con un mock de `ft.Page`, verificar que `toggle_timer`/`reset_timer`/`change_mode` actualizan el estado del manager correctamente.
  - [ ] 5.2 Ejecutar `python -m unittest discover -s tests -p "test_*.py"` y corregir todos los fallos. Verificar que los 6 test files existentes (config, timer, gui, sounds, tasks, manager) siguen pasando sin regresiones.
  - [ ] 5.3 Ejecutar `coverage run -m unittest discover -s tests -p "test_*.py"` y verificar cobertura > 85%. Añadir tests adicionales si hay gaps.
  - [ ] 5.4 Testing manual: arrancar la app con `python main.py`, verificar todos los modos, cambio de tema, volumen, completar tarea, reunión, y que las tareas se guardan en `records/`.

## Fase 6: Documentación y Release

- [ ] 6. Documentación y preparación de release
  - [ ] 6.1 Actualizar `README.md` y `README_es.md`: añadir sección "Nuevas Características v0.2" (Flet, Material Design 3, ProgressRing, animaciones, multiplataforma), actualizar requisitos (flet==0.82.0), actualizar estructura del proyecto.
  - [ ] 6.2 Actualizar `docs/CONFIG.md` y `docs/CONFIG_es.md`: documentar nuevas opciones theme (mode, color_seed) y animations (enabled, duration) con ejemplos YAML.
  - [ ] 6.3 Actualizar `CHANGELOG.md` con entrada `[0.2.0]`: listar Added (Flet GUI, Material Design, ProgressRing, SnackBar, tema oscuro/claro, multiplataforma), Changed (migración Tkinter→Flet, arquitectura componentes), Deprecated (gui.py).
  - [ ] 6.4 Actualizar `build_windows.py` y `build_linux.py`: añadir `flet` a las dependencias de PyInstaller, verificar que los builds generan ejecutables funcionales con la nueva GUI.eme (mode, color_seed) y animations (enabled, duration) con ejemplos YAML.
ir `flet` a las dependencias de PyInstaller, verificar que los builds generan ejecutables funcionales con la nueva GUI.
  - [ ] 6.3 Actualizar `CHANGELOG.md` con entrada `[0.2.0]`: listar Added (Flet GUI, Material Design, ProgressRing, SnackBar, tema oscuro/claro, multiplataforma), Changed (migración Tkinter→Flet, arquitectura componentes), Deprecated (gui.py).
  - [ ] 6.4 Actualizar `build_windows.py` y `build_linux.py`: añad