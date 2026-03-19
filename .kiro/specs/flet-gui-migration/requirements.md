# Requisitos - Release 0.2: Migración GUI a Flet

## Contexto

Basado en las especificaciones del proyecto #[[file:docs/ESPECIFICACIONES_es.md]] y la especificación de la release 0.2 #[[file:docs/specs-by-version/spec-v0.2_es.md]], esta release moderniza la interfaz gráfica migrando de Tkinter a Flet (Flutter para Python).

## Requisitos Funcionales

### RF-1: Mantener funcionalidad existente
Todas las funcionalidades de v0.1 deben seguir funcionando:
- Timer con cuenta regresiva (work, short break, long break)
- Modo reunión con tiempo incremental
- Controles: Start/Pause, Reset
- Gestión de tareas con persistencia en archivos diarios (`records/YYYYMMDD.txt`)
- Estadísticas de sesión (pomodoros, descansos, tiempos)
- Control de volumen
- Alarmas sonoras y ticking
- Configuración via `config.yaml`

### RF-2: Migración a Flet
- Reescribir la GUI usando Flet 0.82.0 en `pomopy/gui_flet.py`
- Arquitectura de componentes en `pomopy/components/`
- Mantener separación UI / lógica de negocio (PomodoroManager)

### RF-3: Componentes Flet
Cinco componentes independientes y reutilizables:
- `TimerDisplay`: ProgressRing circular + texto digital del tiempo
- `ControlButtons`: Botones Start/Pause y Reset con iconos Material
- `ModeSelector`: Chips para Work, Short Break, Long Break
- `TaskInput`: TextField + botón Complete
- `StatsPanel`: Panel con pomodoros, descansos y tiempos

### RF-4: Selector de tema
- Switch Material Design para tema oscuro/claro
- Cambio sin reiniciar la aplicación
- Persistencia del tema en `config.yaml`

### RF-5: Display del timer mejorado
- ProgressRing de Flet con animación nativa
- Display digital con fuente grande
- Color dinámico según modo activo

### RF-6: Animaciones y transiciones
- Animaciones implícitas de Flutter
- Transiciones suaves entre modos
- Efectos Material (ripple, elevation)

### RF-7: Notificaciones visuales
- SnackBar al completar tareas
- Banner visual al terminar timer

## Requisitos No Funcionales

### RNF-1: Rendimiento
- Inicio de aplicación < 2 segundos
- Animaciones fluidas (60 FPS nativo Flutter)
- Uso de memoria < 120 MB

### RNF-2: Compatibilidad
- Windows 10/11 (obligatorio)
- Linux (soporte nativo Flet)
- macOS (soporte nativo Flet)

### RNF-3: Dependencias
- Python 3.8+
- flet == 0.82.0
- PyYAML == 6.0.1
- pygame == 2.6.1

### RNF-4: Testing
- Tests unitarios con `unittest` (un archivo por componente)
- Cobertura > 85%
- Tests existentes no deben romperse

### RNF-5: Mantenibilidad
- Código modular con componentes reutilizables
- Documentación actualizada
- PEP 8

## Acceptance Criteria

1. La aplicación arranca con Flet sin errores
2. Todos los modos (work, short break, long break, meeting) funcionan
3. Las tareas se guardan correctamente en `records/`
4. El tema oscuro/claro se puede cambiar en runtime
5. Los tests existentes siguen pasando
6. Los nuevos tests de componentes pasan con cobertura > 85%
7. La documentación (README, CONFIG, CHANGELOG) está actualizada
