# Guía de Configuración del Entorno de Pruebas

## Requisitos Previos

- Python 3.8 o superior instalado
- pip (gestor de paquetes de Python)
- Acceso a terminal/línea de comandos

## Verificar Instalación de Python

Antes de comenzar, verifica que Python está instalado correctamente:

```bash
python --version
```

o en algunos sistemas:

```bash
python3 --version
```

Deberías ver una versión 3.8 o superior.

## Configuración del Entorno de Pruebas

### 1. Navegar al Directorio del Proyecto

```bash
cd c:\Users\eferosa\workspace\pomodoro-py
```

### 2. (Opcional) Crear Entorno Virtual

Se recomienda usar un entorno virtual para aislar las dependencias:

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Cuando el entorno virtual esté activado, verás `(venv)` al inicio de tu línea de comandos.

### 3. Instalar Dependencias

Instala todas las dependencias necesarias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Esto instalará:
- PyYAML==6.0.1 (para leer archivos de configuración YAML)
- pygame==2.5.2 (para reproducir sonido de alarma)

### 4. Verificar Instalación

Verifica que PyYAML se instaló correctamente:

```bash
pip list
```

Deberías ver `PyYAML` en la lista de paquetes instalados.

## Ejecutar Pruebas Unitarias

### Ejecutar Todos los Tests

Para ejecutar todos los tests del módulo de configuración:

```bash
python test_config.py
```

### Ejecutar Tests con Modo Verbose

Para ver información detallada de cada test:

```bash
python test_config.py -v
```

### Ejecutar un Test Específico

Para ejecutar solo un test específico:

```bash
python -m unittest test_config.TestConfig.test_default_values
```

### Ejecutar Tests con Coverage (Opcional)

Si deseas ver la cobertura de código, primero instala coverage:

```bash
pip install coverage
```

Luego ejecuta:

```bash
coverage run -m unittest test_config.py
coverage report
```

Para un reporte HTML más detallado:

```bash
coverage html
```

Esto creará una carpeta `htmlcov/` con un reporte visual. Abre `htmlcov/index.html` en tu navegador.

## Estructura de Tests

### Tests Disponibles

#### test_config.py (11 tests)

Tests para el módulo de configuración:

1. **test_default_values**: Verifica valores por defecto
2. **test_load_custom_times**: Verifica carga de tiempos personalizados
3. **test_load_custom_colors**: Verifica carga de colores personalizados
4. **test_load_custom_window**: Verifica configuración de ventana
5. **test_load_custom_sound**: Verifica configuración de sonido
6. **test_load_custom_tasks**: Verifica configuración de tareas
7. **test_partial_config**: Verifica configuraciones parciales
8. **test_empty_config_file**: Verifica manejo de archivo vacío
9. **test_invalid_yaml**: Verifica manejo de YAML inválido
10. **test_get_time_for_mode**: Verifica método get_time_for_mode
11. **test_get_color_for_mode**: Verifica método get_color_for_mode

#### test_pomodoro_timer.py (16 tests)

Tests para el módulo del temporizador:

1. **test_initialization**: Verifica inicialización correcta
2. **test_initialization_with_callback**: Verifica asignación de callback
3. **test_start**: Verifica que start() activa el temporizador
4. **test_pause**: Verifica que pause() detiene el temporizador
5. **test_reset_without_new_time**: Verifica reset al tiempo inicial
6. **test_reset_with_new_time**: Verifica reset con nuevo tiempo
7. **test_tick_when_not_running**: Verifica que tick() no decrementa si está pausado
8. **test_tick_when_running**: Verifica que tick() decrementa correctamente
9. **test_tick_reaches_zero**: Verifica comportamiento al llegar a 0
10. **test_tick_calls_callback**: Verifica ejecución de callback
11. **test_tick_stops_at_zero**: Verifica que no decrementa por debajo de 0
12. **test_get_time_formatted**: Verifica formato MM:SS
13. **test_is_finished**: Verifica detección de finalización
14. **test_pause_and_resume**: Verifica pausar y reanudar
15. **test_multiple_resets**: Verifica múltiples resets
#### test_gui.py (16 tests)

Tests para el módulo de interfaz gráfica:

1. **test_initialization**: Verifica inicialización correcta de la app
2. **test_window_configuration**: Verifica configuración de ventana
3. **test_widgets_created**: Verifica creación de todos los widgets
4. **test_initial_display**: Verifica visualización inicial
5. **test_toggle_timer_start**: Verifica inicio del temporizador
6. **test_toggle_timer_pause**: Verifica pausa del temporizador
7. **test_reset_timer**: Verifica reinicio del temporizador
8. **test_change_mode_to_short_break**: Verifica cambio a descanso corto
9. **test_change_mode_to_long_break**: Verifica cambio a descanso largo
10. **test_change_mode_to_work**: Verifica cambio a modo trabajo
11. **test_change_mode_stops_timer**: Verifica que cambiar modo detiene timer
12. **test_color_changes_with_mode**: Verifica cambios de color por modo
13. **test_on_timer_finish**: Verifica comportamiento al terminar
14. **test_update_display**: Verifica actualización de visualización
15. **test_timer_integration**: Verifica integración GUI-Timer
#### test_sounds.py (16 tests)

Tests para el módulo de gestión de sonidos:

1. **test_initialization_default**: Verifica inicialización por defecto
2. **test_initialization_custom**: Verifica inicialización personalizada
3. **test_initialization_with_pygame**: Verifica inicialización con pygame
4. **test_initialization_disabled**: Verifica inicialización deshabilitada
5. **test_play_alarm_when_disabled**: Verifica que no reproduce si está deshabilitado
6. **test_play_alarm_sets_parameters**: Verifica configuración de parámetros
7. **test_play_alarm_with_callback**: Verifica uso de callbacks
8. **test_stop**: Verifica detención de reproducción
9. **test_is_available_without_file**: Verifica disponibilidad sin archivo
10. **test_is_available_with_file**: Verifica disponibilidad con archivo
11. **test_is_available_when_disabled**: Verifica disponibilidad deshabilitada
12. **test_play_once_increments_count**: Verifica incremento de contador
13. **test_play_once_stops_at_limit**: Verifica detención al límite
14. **test_multiple_play_calls**: Verifica múltiples llamadas
15. **test_callback_execution**: Verifica ejecución de callbacks
16. **test_sound_manager_integration**: Verifica integración completa

#### test_pomodoro_manager.py (20 tests)

Tests para el módulo de coordinación de lógica de negocio:

1. **test_initialization**: Verifica inicialización correcta
2. **test_start_timer**: Verifica inicio del temporizador
3. **test_pause_timer**: Verifica pausa del temporizador
4. **test_reset_timer**: Verifica reinicio del temporizador
5. **test_change_mode_to_short_break**: Verifica cambio a descanso corto
6. **test_change_mode_to_long_break**: Verifica cambio a descanso largo
7. **test_tick**: Verifica decremento de tiempo
8. **test_get_time_formatted**: Verifica formato de tiempo
9. **test_set_and_get_task**: Verifica gestión de tareas
10. **test_complete_task**: Verifica completar tarea
11. **test_get_stats**: Verifica obtención de estadísticas
12. **test_get_total_work_time_zero**: Verifica tiempo de trabajo inicial
13. **test_get_total_work_time_with_pomodoros**: Verifica cálculo de tiempo de trabajo
14. **test_get_total_break_time_zero**: Verifica tiempo de descanso inicial
15. **test_get_total_break_time_with_breaks**: Verifica cálculo de tiempo de descanso
16. **test_set_finish_callback**: Verifica establecer callback
17. **test_on_timer_finish_increments_work**: Verifica incremento de trabajo
18. **test_on_timer_finish_increments_short_break**: Verifica incremento de descanso corto
19. **test_on_timer_finish_increments_long_break**: Verifica incremento de descanso largo
20. **test_on_timer_finish_calls_callback**: Verifica ejecución de callback

## Resultados Esperados

### Tests Individuales

Si todos los tests de un módulo pasan correctamente, deberías ver:

**test_config.py:**
```
...........
----------------------------------------------------------------------
Ran 11 tests in 0.XXXs

OK
```

**test_pomodoro_timer.py:**
```
................
----------------------------------------------------------------------
Ran 16 tests in 0.XXXs

OK
```

**test_gui.py:**
```
................
----------------------------------------------------------------------
Ran 16 tests in 0.XXXs

OK
```

**test_sounds.py:**
```
................
----------------------------------------------------------------------
Ran 16 tests in 0.XXXs

OK
```

**test_tasks.py:**
```
.................
----------------------------------------------------------------------
Ran 17 tests in 0.XXXs

OK
```

**test_pomodoro_manager.py:**
```
....................
----------------------------------------------------------------------
Ran 20 tests in 0.XXXs

OK
```

### Todos los Tests

Al ejecutar todos los tests con unittest discover:
```
....................................................................................................
----------------------------------------------------------------------
Ran 96 tests in 0.XXXs

OK
```

Si algún test falla, verás:

```
F..........
======================================================================
FAIL: test_nombre_del_test (test_config.TestConfig)
----------------------------------------------------------------------
...
```

## Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'yaml'"

**Solución:** Instala PyYAML:
```bash
pip install PyYAML
```

### Error: "ModuleNotFoundError: No module named 'config'"

**Solución:** Asegúrate de estar en el directorio correcto:
```bash
cd c:\Users\eferosa\workspace\pomodoro-py
```

### Error: "python: command not found"

**Solución:** En algunos sistemas, usa `python3` en lugar de `python`:
```bash
python3 test_config.py
```

### Tests fallan con errores de permisos

**Solución:** Verifica que tienes permisos de escritura en el directorio temporal del sistema.

### Error al crear archivos temporales en Windows

**Solución:** Los tests crean archivos temporales. Si hay problemas, verifica que la variable de entorno `TEMP` esté configurada correctamente.

## Agregar Nuevos Tests

Para agregar nuevos tests al archivo `test_config.py`:

1. Crea un nuevo método en la clase `TestConfig`
2. El nombre del método debe comenzar con `test_`
3. Usa métodos de aserción como `assertEqual`, `assertTrue`, etc.

Ejemplo:

```python
def test_mi_nuevo_test(self):
    """Descripción del test."""
    config = Config()
    self.assertEqual(config.WORK_TIME, 25 * 60)
```

## Integración Continua (Futuro)

En el futuro, estos tests pueden integrarse con sistemas de CI/CD como:
- GitHub Actions
- GitLab CI
- Jenkins

## Comandos Rápidos

```bash
# Activar entorno virtual (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar todos los tests
python test_config.py
python test_pomodoro_timer.py
python test_gui.py
python test_sounds.py
python test_tasks.py
python test_pomodoro_manager.py

# Ejecutar tests verbose
python test_config.py -v
python test_pomodoro_timer.py -v
python test_gui.py -v
python test_sounds.py -v
python test_tasks.py -v
python test_pomodoro_manager.py -v

# Ejecutar todos los tests con unittest discover
python -m unittest discover -s . -p "test_*.py"

# Desactivar entorno virtual
deactivate
```

## Notas Adicionales

- Los tests son independientes y pueden ejecutarse en cualquier orden
- Los tests crean archivos temporales que se eliminan automáticamente
- No es necesario tener un archivo `config.yaml` para ejecutar los tests
- Los tests verifican tanto casos válidos como casos de error
