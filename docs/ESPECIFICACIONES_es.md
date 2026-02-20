# Especificaciones Técnicas - Aplicación Pomodoro Timer

## 1. Descripción General

Aplicación de escritorio desarrollada en Python para implementar la técnica Pomodoro de gestión del tiempo. La aplicación permitirá a los usuarios alternar entre períodos de trabajo (pomodoros) y descansos (cortos y largos) con un temporizador visual.

## 2. Requisitos Funcionales

### 2.1 Gestión de Tiempos
- **Período de Trabajo (Pomodoro)**: 25 minutos por defecto
- **Descanso Corto**: 5 minutos por defecto
- **Descanso Largo**: 15 minutos por defecto
- Los tiempos deben ser configurables por el usuario.  
- Hay un tiempo no configurable que es "Tiempo de reunion". 
  - Es un tipo de tiempo que indica que esta en una reunion, sin tiempo predefinido.
  - No cuenta como tiempo de "pomodoro", pero sí debe de quedar registrada. 
  - El tiempo es incremental, no decremental. Empieza en 0 y va incrementando. 

### 2.2 Funcionalidades Principales
1. **Iniciar/Pausar Timer**: Botón para controlar el temporizador
2. **Reiniciar**: Botón para resetear el temporizador actual
3. **Cambio de Modo**: Botones para cambiar entre:
   - Modo Trabajo
   - Modo Descanso Corto
   - Modo Descanso Largo
   - Modo Reunión
4. **Visualización del Tiempo**: Reloj digital mostrando tiempo restante/transcurrido en formato MM:SS 
5. **Indicador Visual**: Mostrar claramente el modo actual (Trabajo/Descanso Corto/Descanso Largo/Reunión) con un texto de gran tamaño en la parte superior. 
6. **Notificación**: Alerta sonora o/y visual cuando termina un período. Desactivar el sonido es configurable por el usuario. 
7. **Tarea activa** (Opcional  - Fase 2): un texto debajo del contador indica la tarea actual, para la cual se van acumulando los pomodoros y descansos. Al lado del texto un boton que indica el fin de la tarea actual.


### 2.3 Ciclo Automático (Opcional - Fase 2)
- Después de 4 pomodoros, sugerir descanso largo
- Contador de pomodoros completados en la sesión.
 

### 2.4 Gestion de tareas (Opcional - Fase 3)
- Cada pomodoro debe de quedar registrado con un nombre de tarea.
- Debe de existir un campo de texto que contiene el nombre de la tarea actual y un botón para indicar si la tarea se ha completado.
- Al terminar una tarea (al pulsar el boton de fin de tarea) el texto de borra, pero la tarea y el tiempo empleado (numero de pomodoros + descansos) se almacena en un fichero de texto. El formato puede ser simple texto plano con formato: 
  - "Nombre de la tarea" | <Pomodoros> | <Descansos cortos> | <descansos largos> | <tiempo total> | Hora de inicio | Hora final
- Donde los pomodoros y descansos son un numero y "tiempo total" en formato HH:mm:ss
- Fecha inicio y fecha final en formato "YYYY-MM-DD HH:mm"
- Estas fechas indican cuando se ha asignado una nueva tarea (fecha inicio) y en que momento se ha marcado como finalizada (fecha final).

### 2.4 Registro de Reuniones 
- El registro de reuniones debe de quedar tambien registrado en el fichero de tareas
- Por simplificar, se registra como cualquier otra tarea, pero con el nombre de "REUNION / MEETING". 
- No registra el numero de pomodoros ni descansos. 
- Marcar el inicio de una reunion no cancela una tarea anterior. Por ejemplo, el siguiente caso de uso: 
  - Se inicia un pomodoro : Tarea 1
  - Se para la tarea (pausa o reset)
  - Se cambia a modo reunion y se comienza a contar el tiempo de reunion. 
  - Se pulsa el boton de fin de tiempo de reunion.
  - Se registra como tarea "REUNION" en el fichero
  - Se cambia a modo "Work" y se vuelve a comenzar un ciclo de pomodoro. 
  - Al terminar con la tarea, se queda registrado desde el primer inicio de tarea en el fichero de tarea.
  - 


  

### 3. Requisitos No Funcionales

### 3.1 Interfaz de Usuario
- Diseño minimalista y fácil de usar
- Ventana siempre visible (opción "always on top")
- Tamaño de ventana compacto (aproximadamente 400x300 px)
- Colores diferenciados para cada modo:
  - Trabajo: Rojo/Naranja
  - Descanso Corto: Verde claro
  - Descanso Largo: Azul
  - Reunion: Naranja

### 3.2 Tecnología
- **Lenguaje**: Python 3.8+
- **Framework GUI**: Tkinter (incluido en Python estándar)
- **Dependencias adicionales**: 
  - PyYAML 6.0.1 (gestión de configuración)
  - pygame 2.5.2 (reproducción de sonidos)

### 3.3 Compatibilidad
- Windows 10/11 obligatorio
- Linux opcional. Indicar "TODO" para adaptar el codigo si no se hace. 
- Ejecutable standalone opcional con PyInstaller. 

### 3.4 Guardado de opciones 
- Las configuraciones tienen un valor por defecto, y están definidas en la clase de configuracion. 
- El codigo siempre usa esa clase para hacer referencias a los valores que debe usar.
- Se pueden sobreescribir si existe un fichero de configuracion 'config.yaml' con cambie estos valores. 
- Este fichero se lee al iniciar la aplicación. 
- En esta fase no existe un dialogo para modificarla.

### Guardado de tareas
- Las tareas se guardan en un fichero  pero identificado por la fecha de creacion
- Estos ficheros estarán en una subcarpeta "records"
- Cada dia se genera un fichero "records/<fecha>.txt" donde fecha tiene formato YYYYMMDD con el dia actual.
- 


## 4. Arquitectura del Sistema

### 4.1 Estructura de Archivos
```
pomodoro-py/
│
├── main.py                 # Punto de entrada de la aplicación
├── pomodoro_timer.py       # Lógica del temporizador
├── gui.py                  # Interfaz gráfica
├── config.py               # Configuración y constantes
├── sounds.py               # Gestión de sonidos y alarmas
├── tasks.py                # Gestión de las tareas y almacenamiento (Fase 3)
├── alarm-digital.mp3       # Archivo de alarma sonora
├── requirements.txt        # Dependencias (PyYAML, pygame)
├── config.yaml.example     # Plantilla de configuración
├── README.md              # Documentación de usuario. Manual de usuario
├── CONFIG.md              # Guía de configuración detallada
├── TEST.md                # Guía de tests y entorno de pruebas
├── ALARM.md               # Documentación sobre alarmas
└── ESPECIFICACIONES.md    # Este documento
```

### 4.2 Componentes Principales

#### 4.2.1 Módulo Timer (pomodoro_timer.py)
- Clase `PomodoroTimer`
  - Gestión del tiempo restante
  - Control de estados (corriendo/pausado)
  - Tipos de período (trabajo/descanso corto/largo)
  - Callback cuando el tiempo termina

#### 4.2.2 Módulo GUI (gui.py)
- Clase `PomodoroApp`
  - Ventana principal con Tkinter
  - Reloj digital (Label grande)
  - Botones de control
  - Actualización visual cada segundo
  - Cambio de colores según modo
  - Integración con SoundManager

#### 4.2.3 Módulo Config (config.py)
- Clase `Config`
  - Constantes de tiempo por defecto
  - Colores de la interfaz
  - Configuraciones generales
  - Carga desde archivo YAML
  - Métodos auxiliares para obtener valores por modo

#### 4.2.4 Módulo Sounds (sounds.py)
- Clase `SoundManager`
  - Inicialización de pygame mixer
  - Reproducción de alarma configurable
  - Control de repeticiones (5 veces por defecto)
  - Fallback a sonido del sistema
  - Gestión de archivos de audio personalizados
  - Control de volumen (0.0 a 1.0)

#### 4.2.5 Módulo Tasks (tasks.py)
- Clase `TaskManager`
  - Gestión de tarea actual
  - Contadores de pomodoros y descansos
  - Cálculo de tiempo total basado en contadores y tiempos configurados
  - Persistencia en archivo de texto
  - Carga de tareas guardadas
  - Estadísticas de sesión
  - Usa valores de tiempo de Config para cálculos precisos

#### 4.2.6 Módulo Manager (pomodoro_manager.py)
- Clase `PomodoroManager`
  - Coordinación de lógica de negocio
  - Integración de Timer, Tasks y Sounds
  - Cálculo de tiempos totales
  - Gestión de callbacks
  - Separación de responsabilidades

#### 4.2.7 Main (main.py)
- Inicialización de la aplicación
- Punto de entrada



## 5. Plan de Implementación

### Fase 1: Configuración Inicial ✅ COMPLETADA
1. ✅ Crear estructura de directorios
2. ✅ Crear archivo `config.py` con constantes
3. ✅ Crear `requirements.txt` con PyYAML
4. ✅ Crear tests unitarios para configuración
5. ✅ Crear documentación de configuración (CONFIG.md)
  

### Fase 2: Lógica del Temporizador ✅ COMPLETADA
1. ✅ Implementar clase `PomodoroTimer` en `pomodoro_timer.py`
   - ✅ Constructor con tiempo inicial y callback opcional
   - ✅ Método `start()` para iniciar
   - ✅ Método `pause()` para pausar
   - ✅ Método `reset()` para reiniciar (con opción de nuevo tiempo)
   - ✅ Método `tick()` para decrementar tiempo
   - ✅ Método `get_time_formatted()` para obtener tiempo en formato MM:SS
   - ✅ Propiedad `is_running` para verificar si está corriendo
   - ✅ Método `is_finished()` para verificar si terminó
2. ✅ Crear tests unitarios para el temporizador (16 tests)
3. ✅ Actualizar documentación (TEST.md, README.md)

### Fase 3: Interfaz Gráfica ✅ COMPLETADA
1. ✅ Implementar clase `PomodoroApp` en `gui.py`
   - ✅ Crear ventana principal con Tkinter
   - ✅ Diseñar layout con:
     - ✅ Label para mostrar modo actual
     - ✅ Label grande para el reloj (MM:SS)
     - ✅ Frame con botones de control:
       - ✅ Botón Iniciar/Pausar
       - ✅ Botón Reiniciar
     - ✅ Frame con botones de modo:
       - ✅ Botón "Trabajo"
       - ✅ Botón "Descanso Corto"
       - ✅ Botón "Descanso Largo"
   - ✅ Implementar método `_update_display()` para actualizar cada segundo
   - ✅ Implementar cambio de colores según modo
   - ✅ Conectar botones con lógica del timer
2. ✅ Crear tests unitarios para GUI (16 tests)
3. ✅ Crear `main.py` como punto de entrada

### Fase 4: Integración ✅ COMPLETADA
1. ✅ Crear `main.py` para iniciar la aplicación
2. ✅ Integrar `PomodoroTimer` con `PomodoroApp`
3. ✅ Probar flujo completo
4. ✅ Integración de todos los módulos

### Fase 5: Mejoras y Pulido ✅ COMPLETADA
1. ✅ Agregar notificación sonora al terminar (alarma se reproduce 5 veces)
2. ✅ Agregar opción "always on top" configurable
3. ✅ Crear módulo `sounds.py` para gestión de audio
4. ✅ Archivo de alarma configurable desde config.yaml
5. ✅ Mejorar estética de la interfaz (botones ajustados)
6. ✅ Crear README.md con instrucciones de uso
7. ✅ Crear documentación completa (CONFIG.md, TEST.md, ALARM.md)
8. ✅ Tests unitarios completos (59 tests en total)

### Fase 6: Gestión de Tareas ✅ COMPLETADA
1. ✅ Implementar módulo `tasks.py`
2. ✅ Contador de pomodoros completados
3. ✅ Registro de tareas con tiempos
4. ✅ Cambios en el interfaz de usuario para mostrar el nombre de la tarea en curso
5. ✅ Cambios en el UI para mostrar el botón de fin de Tareas
6. ✅ Persistencia de datos en archivo tasks.txt
7. ✅ Tests unitarios para gestión de tareas (16 tests)
8. ✅ Documentación completa (TASKS.md)

### Fase 7: Mejoras en el interfaz ✅ COMPLETADA
1. ✅ Muestra los totales de pomodoros
2. ✅ Muestra el total de descansos cortos
3. ✅ Muestra el total de descansos largos
4. ✅ Muestra el total de tiempo de trabajo
5. ✅ Muestra el total de tiempo de descanso
6. ✅ Refactorización: Creado pomodoro_manager.py para separar lógica de negocio
7. ✅ GUI simplificada sin lógica de negocio

### Fase 8: Control de volumen ✅ COMPLETADA
1. ✅ Control deslizante de volumen en la interfaz
2. ✅ Métodos set_volume() y get_volume() en SoundManager
3. ✅ Integración con PomodoroManager
4. ✅ Tests unitarios (5 tests adicionales)
5. ✅ Documentación actualizada

### Fase 9: Corrección de cálculo de tiempo ✅ COMPLETADA
1. ✅ TaskManager usa valores de Config para tiempos
2. ✅ Cálculo de tiempo total basado en contadores
3. ✅ Fórmula: (pomodoros × tiempo_trabajo) + (descansos_cortos × tiempo_corto) + (descansos_largos × tiempo_largo)
4. ✅ Respeta configuración personalizada de tiempos
5. ✅ Documentación actualizada con ejemplos de cálculo


### Fase 10: Distribución Windows (Opcional)
1. [ ] Crear ejecutable con PyInstaller
2. [ ] Documentar proceso de instalación
3. [ ] Crear instalador para Windows

### Fase 11: Distribución Linux (Opcional)
1. [ ] Crear ejecutable con PyInstaller para linux
2. [ ] Documentar proceso de instalación
3. [ ] Crear instalador para Linux en debian (.deb)
4. [ ] Crear instalador para linux en RedHat (.rpm)


### Fase 12: Configurar CICD 
1. [ ] Crear un fichero de action para github 
2. [ ] Debe de lanzar todos los tests automáticamente
3. [ ] debe de lanzar el instalador de la fase 10
4. [ ] Debe de lanzar los instaladores de la fase 11
5. [ ] Debe de poner disponible los instaladores en GitHub como release
6. [ ] La gestion de versiones a través de tags de git
7. [ ] La gestion version de los instaladores 



## 6. Casos de Uso

### 6.1 Caso de Uso Principal
1. Usuario inicia la aplicación
2. Por defecto aparece en modo "Trabajo" con 25:00
3. Usuario presiona "Iniciar"
4. El temporizador comienza la cuenta regresiva
5. Usuario puede pausar en cualquier momento
6. Cuando llega a 00:00, se muestra notificación
7. Usuario cambia a "Descanso Corto" (5:00)
8. Repite el ciclo

### 6.2 Caso de Uso Alternativo
1. Usuario inicia la aplicación
2. Usuario cambia directamente a "Descanso Largo"
3. Usuario presiona "Iniciar"
4. Durante la cuenta regresiva, usuario presiona "Reiniciar"
5. El tiempo vuelve a 15:00
6. Usuario continúa

## 7. Interfaz de Usuario (Mockup Textual)

```
┌─────────────────────────────────────┐
│         POMODORO TIMER              │
│                                     │
│         [MODO: TRABAJO]             │
│                                     │
│            25:00                    │
│         (Reloj Grande)              │
│                                     │
│    [Iniciar]    [Reiniciar]         │
│                                     │
│       (Texto con la tarea)          |
│      [✅ tarea completada]         |
|                                     │
│  [Trabajo] [Descanso] [Descanso]    │
│            [Corto   ] [Largo   ]    |
|                                     │
|            [ REUNION ]              │
│                                     |
│  Pomodoros completados: 0           |
│  Descansos cortos: 0                |
│  Descansos largos: 0                |
|  Tiempo de trabajo:  xx:xx          |
|  Tiempo de descanso: xx:xx          |
|                                     |
|  Volumen: [=========>    ] 75       |
└─────────────────────────────────────┘
```

## 8. Configuración por Defecto

```python
# Tiempos en segundos
WORK_TIME = 25 * 60      # 25 minutos
SHORT_BREAK = 5 * 60     # 5 minutos
LONG_BREAK = 15 * 60     # 15 minutos

# Colores
WORK_COLOR = "#FF6B6B"        # Rojo claro
SHORT_BREAK_COLOR = "#4ECDC4" # Verde azulado
LONG_BREAK_COLOR = "#45B7D1"  # Azul claro
BG_COLOR = "#2C3E50"          # Fondo oscuro
TEXT_COLOR = "#FFFFFF"        # Texto blanco

# Ventana
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
ALWAYS_ON_TOP = True

# Sonido
SOUND_ENABLED = True
ALARM_FILE = "alarm-digital.mp3"
TICKING_FILE = "ticking-slow.mp3"

# Tareas
TASKS_FILE = "tasks.txt"
```

## 9. Pruebas

### 9.1 Cobertura de Tests

La aplicación cuenta con **101 tests unitarios** distribuidos en 6 módulos:

- **test_config.py** (11 tests): Configuración y carga desde YAML
- **test_pomodoro_timer.py** (16 tests): Lógica del temporizador
- **test_gui.py** (16 tests): Interfaz gráfica y widgets
- **test_sounds.py** (19 tests): Gestión de sonidos, alarmas y volumen
- **test_tasks.py** (17 tests): Gestión de tareas y persistencia
- **test_pomodoro_manager.py** (22 tests): Lógica de negocio y coordinación

### 9.2 Pruebas Funcionales
- ✅ Verificar que el temporizador cuenta correctamente
- ✅ Verificar que pausa funciona correctamente
- ✅ Verificar que reiniciar restaura el tiempo
- ✅ Verificar cambio entre modos
- ✅ Verificar notificación al terminar
- ✅ Verificar reproducción de alarma 5 veces
- ✅ Verificar carga de configuración desde YAML
- ✅ Verificar archivo de alarma personalizado

### 9.3 Pruebas de Interfaz
- ✅ Verificar que todos los botones responden
- ✅ Verificar que los colores cambian según modo
- ✅ Verificar que el reloj se actualiza cada segundo
- ✅ Verificar que la ventana es responsive
- ✅ Verificar integración GUI-Timer
- ✅ Verificar callbacks de finalización

### 9.4 Ejecutar Tests

```bash
# Tests individuales
python test_config.py
python test_pomodoro_timer.py
python test_gui.py
python test_sounds.py
python test_tasks.py
python test_pomodoro_manager.py

# Todos los tests
python -m unittest discover -s . -p "test_*.py"
```

## 10. Mejoras Futuras (Backlog)

### Prioridad Alta
1. Visualización de tareas completadas en la aplicación
2. Estadísticas gráficas de productividad
3. Filtrar tareas por fecha

### Prioridad Media
4. Estadísticas y gráficos de productividad
5. Integración con notificaciones del sistema
6. Atajos de teclado
7. Minimizar a bandeja del sistema

### Prioridad Baja
8. Temas de color personalizables desde GUI
9. Modo oscuro/claro
10. Sincronización en la nube (opcional)
11. Exportar estadísticas a CSV/PDF
12. Múltiples perfiles de usuario

## 11. Cronograma Estimado

- **Fase 1**: 30 minutos ✅ COMPLETADA
- **Fase 2**: 1-2 horas ✅ COMPLETADA
- **Fase 3**: 2-3 horas ✅ COMPLETADA
- **Fase 4**: 1 hora ✅ COMPLETADA
- **Fase 5**: 2-3 horas ✅ COMPLETADA
- **Fase 6**: 3-4 horas ✅ COMPLETADA
- **Fase 7**: 2-3 horas (Opcional)
- **Total completado**: 9.5-13.5 horas
- **Total estimado**: 11.5-16.5 horas

## 12. Estado Actual del Proyecto

### ✅ Funcionalidades Implementadas

1. **Configuración completa**
   - Carga desde archivo YAML
   - Valores por defecto
   - Configuración de tiempos, colores, ventana, sonido
   - 11 tests unitarios

2. **Temporizador funcional**
   - Inicio, pausa, reinicio
   - Cuenta regresiva precisa
   - Callbacks al terminar
   - 16 tests unitarios

3. **Interfaz gráfica completa**
   - Ventana con Tkinter
   - Botones de control y modo
   - Reloj digital con colores por modo
   - Always on top configurable
   - 16 tests unitarios

4. **Sistema de sonido**
   - Módulo independiente (sounds.py)
   - Alarma se reproduce 5 veces
   - Archivo de alarma configurable
   - Fallback a sonido del sistema
   - 16 tests unitarios

5. **Documentación completa**
   - README.md (manual de usuario)
   - CONFIG.md (guía de configuración)
   - TEST.md (guía de tests)
   - ALARM.md (documentación de alarmas)
   - TASKS.md (guía de gestión de tareas)
   - ESPECIFICACIONES.md (este documento)

6. **Gestión de tareas**
   - Módulo independiente (tasks.py)
   - Campo de entrada para nombre de tarea
   - Botón de completar tarea (activo al escribir texto)
   - Contadores automáticos de pomodoros y descansos
   - Persistencia en archivo tasks.txt
   - Formato: "Nombre" | Pomodoros | Descansos cortos | Descansos largos | Tiempo total
   - Cálculo de tiempo basado en contadores y valores de Config
   - 17 tests unitarios

7. **Coordinación de lógica de negocio**
   - Módulo independiente (pomodoro_manager.py)
   - Separación de responsabilidades
   - Integración de timer, tasks y sounds
   - Cálculo de tiempos totales
   - Gestión de callbacks
   - 20 tests unitarios

8. **Interfaz con estadísticas completas**
   - Visualización de pomodoros completados
   - Visualización de descansos cortos y largos
   - Tiempo total de trabajo
   - Tiempo total de descanso
   - Layout en dos columnas

### 🚧 En Desarrollo

- Ninguno actualmente

### 📋 Planificado

- Gestión de tareas
- Contador de pomodoros
- Estadísticas
- Ejecutable standalone

## 13. Conclusión

Esta especificación documenta una aplicación Pomodoro completamente funcional con:
- ✅ 6 módulos principales (config, timer, gui, sounds, tasks, manager)
- ✅ 101 tests unitarios (100% cobertura de funcionalidades críticas)
- ✅ Configuración flexible mediante YAML
- ✅ Interfaz gráfica intuitiva con estadísticas completas
- ✅ Sistema de alarmas robusto con control de volumen
- ✅ Gestión completa de tareas con persistencia
- ✅ Arquitectura limpia con separación de responsabilidades
- ✅ Documentación completa

La aplicación está lista para uso en producción y preparada para futuras extensiones.ama Estimado

- **Fase 1**: 30 minutos
- **Fase 2**: 1-2 horas
- **Fase 3**: 2-3 horas
- **Fase 4**: 1 hora
- **Fase 5**: 1-2 horas
- **Total**: 5-8 horas de desarrollo

## 12. Conclusión

Esta especificación proporciona una guía completa para desarrollar una aplicación Pomodoro funcional y fácil de usar. El enfoque es mantener la simplicidad mientras se proporciona todas las funcionalidades esenciales de la técnica Pomodoro.
