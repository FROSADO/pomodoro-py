# Guía de Configuración - Pomodoro Timer

## Introducción

La aplicación Pomodoro Timer permite personalizar su comportamiento mediante un archivo de configuración YAML. Todos los parámetros son opcionales; si no se especifican, la aplicación usará valores por defecto.

## Archivo de Configuración

El archivo de configuración debe llamarse `config.yaml` y ubicarse en el mismo directorio que la aplicación.

### Crear el Archivo de Configuración

1. Copia el archivo `config.yaml.example` y renómbralo a `config.yaml`
2. Edita los valores según tus preferencias
3. Guarda el archivo
4. Reinicia la aplicación para que los cambios surtan efecto

## Parámetros Configurables

### 1. Tiempos (times)

Configura la duración de cada período en **minutos**.

```yaml
times:
  work_time: 25        # Duración del período de trabajo
  short_break: 5       # Duración del descanso corto
  long_break: 15       # Duración del descanso largo
```

**Valores por defecto:**
- `work_time`: 25 minutos
- `short_break`: 5 minutos
- `long_break`: 15 minutos

**Ejemplo personalizado:**
```yaml
times:
  work_time: 50        # Sesiones de trabajo más largas
  short_break: 10      # Descansos cortos más largos
  long_break: 30       # Descansos largos más largos
```

### 2. Colores (colors)

Personaliza los colores de la interfaz usando formato hexadecimal (#RRGGBB).

```yaml
colors:
  work_color: "#FF6B6B"           # Color para modo trabajo
  short_break_color: "#4ECDC4"    # Color para descanso corto
  long_break_color: "#45B7D1"     # Color para descanso largo
  bg_color: "#2C3E50"             # Color de fondo
  text_color: "#FFFFFF"           # Color del texto
```

**Valores por defecto:**
- `work_color`: #FF6B6B (rojo claro)
- `short_break_color`: #4ECDC4 (verde azulado)
- `long_break_color`: #45B7D1 (azul claro)
- `bg_color`: #2C3E50 (gris oscuro)
- `text_color`: #FFFFFF (blanco)

**Ejemplo con tema oscuro:**
```yaml
colors:
  work_color: "#E74C3C"
  short_break_color: "#2ECC71"
  long_break_color: "#3498DB"
  bg_color: "#1C1C1C"
  text_color: "#ECEFF1"
```

### 3. Ventana (window)

Configura el tamaño y comportamiento de la ventana.

```yaml
window:
  width: 400           # Ancho en píxeles
  height: 500          # Alto en píxeles
  always_on_top: true  # Mantener ventana siempre visible
```

**Valores por defecto:**
- `width`: 400 píxeles
- `height`: 500 píxeles
- `always_on_top`: true

**Ejemplo para ventana más grande:**
```yaml
window:
  width: 500
  height: 400
  always_on_top: false
```

### 4. Sonido (sound)

Activa o desactiva las notificaciones sonoras y configura el archivo de alarma.

```yaml
sound:
  enabled: true                    # true para activar, false para desactivar
  alarm_file: "alarm-digital.mp3"  # Archivo de alarma a reproducir
  ticking_file: "ticking-slow.mp3"  # Archivo de sonido de ticking durante trabajo
```

**Valores por defecto:**
- `enabled`: true
- `alarm_file`: "alarm-digital.mp3"
- `ticking_file`: "ticking-slow.mp3"

**Ejemplo para desactivar sonido:**
```yaml
sound:
  enabled: false
```

**Ejemplo con archivos personalizados:**
```yaml
sound:
  enabled: true
  alarm_file: "mi-alarma.mp3"
  ticking_file: "mi-ticking.mp3"
```

### 5. Tareas (tasks)

Configura el archivo donde se guardan las tareas completadas.

```yaml
tasks:
  file: "tasks.txt"    # Nombre del archivo de tareas
```

**Valor por defecto:**
- `file`: "tasks.txt"

**Ejemplo con ruta personalizada:**
```yaml
tasks:
  file: "mis_tareas.txt"
```

## Ejemplos Completos

### Configuración Minimalista

```yaml
times:
  work_time: 25
  short_break: 5
  long_break: 15
```

### Configuración para Sesiones Largas

```yaml
times:
  work_time: 50
  short_break: 10
  long_break: 30

window:
  always_on_top: false
```

### Configuración Sin Sonido

```yaml
sound:
  enabled: false
```

### Configuración Completa Personalizada

```yaml
times:
  work_time: 30
  short_break: 7
  long_break: 20

colors:
  work_color: "#E74C3C"
  short_break_color: "#2ECC71"
  long_break_color: "#3498DB"
  bg_color: "#1C1C1C"
  text_color: "#ECEFF1"

window:
  width: 450
  height: 550
  always_on_top: true

sound:
  enabled: true
  alarm_file: "mi-alarma.mp3"
  ticking_file: "mi-ticking.mp3"

tasks:
  file: "pomodoros_completados.txt"
```

## Solución de Problemas

### La configuración no se aplica

1. Verifica que el archivo se llame exactamente `config.yaml`
2. Asegúrate de que esté en el mismo directorio que la aplicación
3. Verifica que la sintaxis YAML sea correcta (indentación con espacios, no tabs)
4. Reinicia la aplicación

### Error al cargar la configuración

Si hay un error en el archivo YAML, la aplicación mostrará un mensaje en consola y usará los valores por defecto. Verifica:

- La indentación (usa 2 espacios por nivel)
- Los dos puntos después de cada clave
- Los valores booleanos (true/false en minúsculas)
- Los colores en formato hexadecimal (#RRGGBB)

### Restaurar valores por defecto

Para volver a los valores por defecto:
1. Elimina o renombra el archivo `config.yaml`
2. Reinicia la aplicación

## Notas Adicionales

- Los cambios en `config.yaml` solo se aplican al reiniciar la aplicación
- Puedes omitir cualquier sección que no quieras personalizar
- Los valores deben estar en el formato correcto (números para tiempos, strings para colores, etc.)
- En futuras versiones se añadirá una interfaz gráfica para modificar la configuración
