# Pomodoro Timer - Aplicación de Escritorio

Aplicación de escritorio desarrollada en Python para implementar la técnica Pomodoro de gestión del tiempo.

## ¿Qué es la Técnica Pomodoro?

La técnica Pomodoro es un método de gestión del tiempo que utiliza intervalos de trabajo (pomodoros) de 25 minutos, separados por breves descansos de 5 minutos. Después de 4 pomodoros, se toma un descanso más largo de 15 minutos.

## Características

- ⏱️ Temporizador con cuenta regresiva visual
- 🎨 Colores diferenciados para cada modo (Trabajo/Descanso)
- ⏯️ Controles de Iniciar/Pausar/Reiniciar
- 🔄 Cambio rápido entre modos
- ⏰ Alarma sonora que se reproduce 5 veces al terminar
- 🔊 Sonido de ticking durante períodos de trabajo
- 🔉 Control de volumen ajustable
- 📝 Gestión de tareas con seguimiento de pomodoros
- 💾 Persistencia de tareas completadas
- ⚙️ Configuración personalizable mediante archivo YAML
- 🪟 Ventana siempre visible (always on top)

## Requisitos

- Python 3.8 o superior
- PyYAML (instalado automáticamente con requirements.txt)
- pygame (instalado automáticamente con requirements.txt)
- Archivo de alarma: `assets/alarm-digital.mp3` (incluido en el proyecto)
- Archivo de ticking: `assets/ticking-slow.mp3` (incluido en el proyecto)

## Instalación

1. Clona o descarga este repositorio
2. Navega al directorio del proyecto:
   ```bash
   cd pomodoro-py
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Iniciar la Aplicación

```bash
python main.py
```

### Controles Básicos

1. **Iniciar/Pausar**: Inicia o pausa el temporizador actual
2. **Reiniciar**: Reinicia el temporizador al tiempo inicial del modo actual
3. **Trabajo**: Cambia a modo trabajo (25 minutos por defecto)
4. **Descanso Corto**: Cambia a descanso corto (5 minutos por defecto)
5. **Descanso Largo**: Cambia a descanso largo (15 minutos por defecto)
6. **Campo de tarea**: Escribe el nombre de tu tarea y presiona Enter
7. **✓ Completar**: Completa y guarda la tarea actual (se activa al escribir texto)
8. **Control de volumen**: Ajusta el volumen de los sonidos (0-100)

### Flujo de Trabajo Recomendado

1. Inicia la aplicación (modo Trabajo por defecto)
2. Ajusta el volumen según tu preferencia usando el control deslizante
3. Escribe el nombre de tu tarea en el campo de texto
4. Presiona "Iniciar" para comenzar tu pomodoro
5. Trabaja hasta que el temporizador llegue a 00:00 (el contador se incrementa automáticamente)
6. Cambia a "Descanso Corto" y presiona "Iniciar"
7. Descansa durante 5 minutos (el contador de descansos se incrementa automáticamente)
8. Repite el ciclo
9. Después de 4 pomodoros, toma un "Descanso Largo"
10. Al terminar la tarea, presiona "✓ Completar" para guardarla (pausa automáticamente el temporizador y guarda los contadores)

Para más detalles sobre gestión de tareas, consulta [TASKS.md](docs/TASKS.md).

## Configuración

La aplicación usa valores por defecto, pero puedes personalizarlos creando un archivo `config.yaml` en el directorio de la aplicación.

### Crear Archivo de Configuración

1. Copia el archivo `config.yaml.example` y renómbralo a `config.yaml`
2. Edita los valores según tus preferencias
3. Reinicia la aplicación

### Ejemplo de Configuración

```yaml
# Tiempos en minutos
times:
  work_time: 25
  short_break: 5
  long_break: 15

# Colores (formato hexadecimal)
colors:
  work_color: "#FF6B6B"
  short_break_color: "#4ECDC4"
  long_break_color: "#45B7D1"

# Ventana
window:
  width: 400
  height: 300
  always_on_top: true

# Sonido
sound:
  enabled: true
  alarm_file: "alarm-digital.mp3"
```

Para más detalles sobre configuración, consulta [CONFIG.md](docs/CONFIG.md).

## Estructura del Proyecto

```
pomodoro-py/
├── main.py                    # Punto de entrada
├── pomopy/                    # Código fuente
│   ├── config.py              # Gestión de configuración
│   ├── gui.py                 # Interfaz gráfica
│   ├── pomodoro_manager.py    # Coordinación de lógica de negocio
│   ├── pomodoro_timer.py      # Lógica del temporizador
│   ├── sounds.py              # Gestión de sonidos
│   └── tasks.py               # Gestión de tareas
├── tests/                     # Tests unitarios
│   ├── test_config.py
│   ├── test_gui.py
│   ├── test_pomodoro_manager.py
│   ├── test_pomodoro_timer.py
│   ├── test_sounds.py
│   └── test_tasks.py
├── assets/                    # Recursos de la aplicación
│   ├── alarm-digital.mp3      # Archivo de alarma sonora
│   └── ticking-slow.mp3       # Archivo de sonido de ticking
├── requirements.txt           # Dependencias
├── config.yaml.example        # Plantilla de configuración
├── README.md                  # Este archivo
├── CONFIG.md                  # Guía de configuración
├── TEST.md                    # Guía de tests
├── TASKS.md                   # Guía de gestión de tareas
└── ESPECIFICACIONES.md        # Especificaciones técnicas
```

## Desarrollo

### Ejecutar Tests

```bash
# Tests de configuración
python -m tests.test_config

# Tests del temporizador
python -m tests.test_pomodoro_timer

# Tests de la interfaz gráfica
python -m tests.test_gui

# Tests de gestión de sonidos
python -m tests.test_sounds

# Tests de gestión de tareas
python -m tests.test_tasks

# Tests del gestor de lógica de negocio
python -m tests.test_pomodoro_manager

# Todos los tests
python -m unittest discover -s tests -p "test_*.py"
```

Para más información sobre tests, consulta [TEST.md](docs/TEST.md).

## Estado del Proyecto

### ✅ Completado

- [x] Módulo de configuración
- [x] Lógica del temporizador
- [x] Interfaz gráfica (GUI)
- [x] Integración GUI + Timer
- [x] Tests unitarios (config, timer, GUI, sounds, tasks y manager - 101 tests)
- [x] Documentación completa
- [x] Aplicación funcional
- [x] Alarma sonora (se reproduce 5 veces al terminar)
- [x] Gestión de tareas con persistencia
- [x] Control de volumen ajustable

### 🚧 En Desarrollo

- [ ] Visualización de tareas completadas
- [ ] Estadísticas gráficas

### 📋 Planificado

- [ ] Gestión de tareas
- [ ] Contador de pomodoros completados
- [ ] Estadísticas
- [ ] Ejecutable standalone

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Asegúrate de que todos los tests pasen
2. Añade tests para nuevas funcionalidades
3. Actualiza la documentación según sea necesario

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Soporte

Para reportar problemas o sugerir mejoras, por favor abre un issue en el repositorio del proyecto.

## Créditos

Desarrollado como una herramienta de productividad basada en la técnica Pomodoro creada por Francesco Cirillo.
