# Guía de Gestión de Tareas - Pomodoro Timer

## Introducción

La funcionalidad de gestión de tareas permite registrar y hacer seguimiento de tus pomodoros asociados a tareas específicas. Cada tarea registra el número de pomodoros de trabajo, descansos cortos y largos, así como el tiempo total invertido.

## Cómo Usar

### 1. Establecer una Tarea

1. En el campo de texto central, haz clic y escribe el nombre de tu tarea
2. Presiona **Enter** para establecer la tarea
3. El botón "✓ Completar" se activará

### 2. Trabajar en la Tarea

1. Presiona "Iniciar" para comenzar un pomodoro
2. Trabaja hasta que el temporizador llegue a 00:00
3. El contador de pomodoros se incrementará automáticamente
4. Toma descansos cortos o largos según necesites
5. Los descansos también se contabilizan automáticamente

### 3. Completar una Tarea

1. Cuando termines la tarea, presiona el botón **"✓ Completar"**
2. La tarea se guardará en el archivo `tasks.txt`
3. Los contadores se resetearán para la siguiente tarea

## Formato del Archivo de Tareas

Las tareas completadas se guardan en `tasks.txt` con el siguiente formato:

```
"Nombre de la tarea" | Pomodoros | Descansos cortos | Descansos largos | Tiempo total
```

### Ejemplos:

```
"Asamblea CCOO" | 1 | 0 | 0 | 00:25:00
"Tarea ejemplo" | 2 | 2 | 0 | 01:00:00
"Otra tarea de ejemplo" | 3 | 2 | 1 | 01:40:00
```

### Cálculo del Tiempo Total

El tiempo total se calcula automáticamente basado en:
- **Pomodoros**: Cada uno cuenta como el tiempo configurado (25 min por defecto)
- **Descansos cortos**: Cada uno cuenta como el tiempo configurado (5 min por defecto)
- **Descansos largos**: Cada uno cuenta como el tiempo configurado (15 min por defecto)

**Ejemplo de cálculo:**
- 3 pomodoros + 2 descansos cortos + 1 descanso largo
- = (3 × 25) + (2 × 5) + (1 × 15)
- = 75 + 10 + 15
- = 100 minutos = 01:40:00

**Nota:** Si modificas los tiempos en `config.yaml`, el cálculo usará tus valores personalizados.

## Estadísticas en Pantalla

En la parte inferior de la ventana verás:
- **Pomodoros: X** - Número de pomodoros completados en la tarea actual
- **Descansos cortos: X** - Número de descansos cortos completados
- **Descansos largos: X** - Número de descansos largos completados
- **Tiempo trabajo: XX:XX** - Tiempo total de trabajo acumulado
- **Tiempo descanso: XX:XX** - Tiempo total de descanso acumulado

**Importante:** Los contadores se incrementan automáticamente cuando el temporizador llega a 00:00. No se cuentan los períodos pausados o reiniciados antes de terminar.

## Ubicación del Archivo

Por defecto, las tareas se guardan en:
```
pomodoro-py/tasks.txt
```

Puedes cambiar la ubicación editando `config.yaml`:

```yaml
tasks:
  file: "mis_tareas.txt"
```

## Flujo de Trabajo Recomendado

### Ejemplo de Sesión Completa

1. **Iniciar sesión**
   - Escribe "Desarrollar feature X"
   - Presiona Enter

2. **Primer pomodoro**
   - Presiona "Iniciar"
   - Trabaja 25 minutos hasta que llegue a 00:00
   - El contador se incrementa automáticamente: Pomodoros: 1

3. **Descanso corto**
   - Cambia a "Descanso Corto"
   - Presiona "Iniciar"
   - Descansa 5 minutos hasta que llegue a 00:00
   - El contador se incrementa automáticamente: Descansos cortos: 1

4. **Continuar trabajando**
   - Repite el ciclo 3 veces más
   - Después del 4º pomodoro, toma un descanso largo

5. **Completar tarea**
   - Presiona "✓ Completar"
   - La tarea se guarda con: nombre, contadores y tiempo total calculado
   - Ejemplo guardado: "Desarrollar feature X" | 4 | 3 | 1 | 02:15:00

## Consejos

### Nombres de Tareas Efectivos

✅ **Buenos ejemplos:**
- "Estudiar capítulo 5 de Python"
- "Escribir informe mensual"
- "Revisar pull request #123"

❌ **Evitar:**
- "Trabajo" (demasiado genérico)
- "Tarea" (no descriptivo)
- Nombres muy largos (más de 50 caracteres)

### Gestión de Interrupciones

Si te interrumpen durante un pomodoro:
1. Pausa el temporizador
2. Atiende la interrupción
3. Reinicia si la interrupción fue larga
4. Continúa si fue breve

### Análisis de Productividad

Revisa periódicamente tu archivo `tasks.txt` para:
- Identificar cuánto tiempo tomas en tareas similares
- Mejorar estimaciones futuras
- Detectar patrones de productividad

## Solución de Problemas

### La tarea no se guarda

**Problema:** Al presionar "✓ Completar" no pasa nada

**Soluciones:**
1. Verifica que estableciste un nombre de tarea (presionaste Enter)
2. Verifica permisos de escritura en el directorio
3. Revisa que el archivo `tasks.txt` no esté abierto en otro programa

### El contador no se incrementa

**Problema:** Los pomodoros no se cuentan

**Soluciones:**
1. Asegúrate de haber establecido una tarea primero
2. Deja que el temporizador llegue a 00:00 (no lo detengas antes)
3. El contador solo se incrementa al finalizar un período completo

### Perdí mis tareas

**Problema:** El archivo `tasks.txt` está vacío o no existe

**Soluciones:**
1. Busca el archivo en el directorio de la aplicación
2. Verifica la configuración en `config.yaml`
3. Las tareas solo se guardan al presionar "✓ Completar"

## Importar/Exportar Tareas

### Hacer Backup

```bash
# Windows
copy tasks.txt tasks_backup.txt

# Linux/macOS
cp tasks.txt tasks_backup.txt
```

### Analizar con Excel/Calc

1. Abre `tasks.txt` con un editor de texto
2. Copia el contenido
3. Pega en Excel/Calc
4. Usa "Datos > Texto en columnas"
5. Selecciona "|" como delimitador

## Próximas Funcionalidades

En futuras versiones:
- [ ] Visualización de tareas completadas en la aplicación
- [ ] Estadísticas gráficas
- [ ] Exportar a CSV/PDF
- [ ] Filtrar tareas por fecha
- [ ] Editar tareas guardadas

## Preguntas Frecuentes

**¿Puedo tener múltiples tareas simultáneas?**
No, solo puedes trabajar en una tarea a la vez. Completa la actual antes de comenzar otra.

**¿Se pierden los datos si cierro la aplicación?**
No, si presionaste "✓ Completar". Las tareas completadas se guardan permanentemente.

**¿Puedo editar el archivo tasks.txt manualmente?**
Sí, pero respeta el formato para que la aplicación pueda leerlo correctamente.

**¿Hay límite de tareas?**
No, puedes guardar tantas tareas como quieras.
