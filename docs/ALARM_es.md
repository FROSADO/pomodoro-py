# Nota sobre el archivo de alarma

La aplicación requiere un archivo de audio llamado `alarm-digital.mp3` en el directorio raíz del proyecto.

## Ubicación del archivo

El archivo debe estar en:
```
pomodoro-py/alarm-digital.mp3
```

## Comportamiento

- Cuando un pomodoro o descanso termina, la alarma se reproduce **5 veces** consecutivas
- Cada reproducción tiene un intervalo de 2 segundos
- Si el archivo no existe o pygame no está instalado, se usa el sonido del sistema (bell)
- La alarma solo suena si `sound.enabled` está en `true` en la configuración

## Requisitos

- pygame debe estar instalado: `pip install pygame`
- El archivo debe ser formato MP3
- El archivo debe tener permisos de lectura

## Desactivar la alarma

Para desactivar la alarma, edita `config.yaml`:

```yaml
sound:
  enabled: false
```

## Usar un archivo de alarma personalizado

Puedes usar tu propio archivo de alarma:

```yaml
sound:
  enabled: true
  alarm_file: "mi-alarma.mp3"
```

## Solución de problemas

Si la alarma no suena:
1. Verifica que el archivo `alarm-digital.mp3` existe
2. Verifica que pygame está instalado: `pip list | grep pygame`
3. Verifica que `sound.enabled` está en `true` en `config.yaml`
4. Verifica los permisos del archivo de audio
