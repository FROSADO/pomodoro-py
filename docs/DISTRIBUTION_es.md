# Guía de Distribución - Pomodoro Timer

Esta guía explica cómo construir y distribuir la aplicación Pomodoro Timer para diferentes plataformas.

## Tabla de Contenidos

1. [Prerequisitos](#prerequisitos)
2. [Construcción Local](#construcción-local)
3. [CI/CD con GitHub Actions](#cicd-con-github-actions)
4. [Gestión de Versiones](#gestión-de-versiones)
5. [Monitorización y Resolución de Problemas](#monitorización-y-resolución-de-problemas)

## Prerequisitos

### Todas las Plataformas
- Python 3.8 o superior
- pip (gestor de paquetes Python)
- Git

### Windows
- PyInstaller: `pip install pyinstaller`

### Linux (Debian/Ubuntu)
- PyInstaller: `pip install pyinstaller`
- dpkg-dev: `sudo apt-get install dpkg-dev`

### Linux (RedHat/Fedora/CentOS)
- PyInstaller: `pip install pyinstaller`
- rpm-build: `sudo yum install rpm-build`

## Construcción Local

### Ejecutable Windows

```bash
# Instalar dependencias
pip install -r requirements.txt
pip install pyinstaller

# Construir ejecutable
python build_windows.py

# Salida: dist/PomodoroTimer.exe
```

**Configuración:**
- Edita `build_windows.py` para personalizar:
  - Nombre de la aplicación
  - Archivo de icono (colocar en `assets/icon.ico`)
  - Archivos de datos adicionales

### Ejecutable Linux

```bash
# Instalar dependencias
pip install -r requirements.txt
pip install pyinstaller

# Construir ejecutable
python build_linux.py

# Salida: dist/pomodoro-timer
```

### Paquete Debian (.deb)

```bash
# Instalar dependencias
sudo apt-get update
sudo apt-get install dpkg-dev

# Construir paquete
python build_deb.py

# Salida: pomodoro-timer_0.1.0.deb
```

**Instalación:**
```bash
sudo dpkg -i pomodoro-timer_0.1.0.deb
sudo apt-get install -f  # Arreglar dependencias si es necesario
```

**Desinstalación:**
```bash
sudo apt-get remove pomodoro-timer
```

### Paquete RPM (.rpm)

```bash
# Instalar dependencias
sudo yum install rpm-build

# Construir paquete
python build_rpm.py

# Salida: RPMS/noarch/pomodoro-timer-0.1.0-1.noarch.rpm
```

**Instalación:**
```bash
sudo rpm -i RPMS/noarch/pomodoro-timer-0.1.0-1.noarch.rpm
```

**Desinstalación:**
```bash
sudo rpm -e pomodoro-timer
```

## CI/CD con GitHub Actions

### Resumen del Workflow

El proyecto usa GitHub Actions para construcción y publicación automatizada. El workflow está definido en `.github/workflows/build-release.yml`.

### Configuración de GITHUB_TOKEN

#### ¿Qué es GITHUB_TOKEN?

`GITHUB_TOKEN` es un token de autenticación **automático** que GitHub proporciona a cada workflow de GitHub Actions. **No necesitas crearlo ni configurarlo manualmente**.

**Características**:
- ✅ **Automático**: GitHub lo crea automáticamente para cada ejecución del workflow
- ✅ **Seguro**: Expira al finalizar el workflow
- ✅ **Sin configuración**: No necesitas añadirlo en Settings > Secrets
- ✅ **Permisos**: Tiene permisos para crear releases, subir archivos, etc.

#### Cómo se usa en el workflow

En el archivo `.github/workflows/build-release.yml`:

```yaml
- name: Create Release
  uses: softprops/action-gh-release@v1
  with:
    files: |
      pomodoro-timer-windows/PomodoroTimer.exe
      pomodoro-timer-linux/pomodoro-timer
      pomodoro-timer-deb/*.deb
      pomodoro-timer-rpm/**/*.rpm
    draft: false
    prerelease: false
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # ← Automático, no requiere configuración
```

#### Configurar permisos (si es necesario)

Por defecto, `GITHUB_TOKEN` tiene permisos de lectura y escritura. Si encuentras errores de permisos:

**Opción 1: En el workflow (Recomendado)**

Añade al inicio de `.github/workflows/build-release.yml`:

```yaml
name: Build and Release

permissions:
  contents: write  # Necesario para crear releases
  packages: write  # Opcional, para publicar paquetes

on:
  push:
    tags:
      - 'v*'
```

**Opción 2: A nivel de repositorio**

1. Ve a **Settings** > **Actions** > **General**
2. En "Workflow permissions", selecciona:
   - ☑️ **Read and write permissions**
3. Click en **Save**

#### Troubleshooting GITHUB_TOKEN

**Error: "Resource not accessible by integration"**
- **Causa**: El GITHUB_TOKEN no tiene permisos suficientes
- **Solución**: Añade `permissions: contents: write` al workflow (ver Opción 1 arriba)

**Error: "Bad credentials"**
- **Causa**: Raro, puede ocurrir con configuraciones especiales del repositorio
- **Solución**: Verifica que el workflow está en la rama correcta

**¿Necesitas un Personal Access Token (PAT)?**

**NO** para este proyecto. Solo necesitarías un PAT si:
- Quieres hacer push a otro repositorio
- Necesitas acceder a APIs de GitHub fuera del repositorio actual
- Quieres ejecutar workflows en otros repositorios

### Etapas del Workflow

1. **Test** - Ejecuta todos los tests unitarios
2. **Build Windows** - Crea ejecutable Windows
3. **Build Linux** - Crea ejecutable Linux
4. **Build Debian** - Crea paquete .deb
5. **Build RPM** - Crea paquete .rpm
6. **Release** - Publica artefactos en GitHub Releases (solo con tags)

### Disparar Construcciones

#### Disparo Manual
1. Ir al repositorio en GitHub
2. Click en pestaña "Actions"
3. Seleccionar workflow "Build and Release"
4. Click en "Run workflow"

#### Disparo Automático (Release)
```bash
# Crear y publicar un tag de versión
git tag v0.1.0
git push origin v0.1.0
```

Esto:
- Ejecutará todos los tests
- Construirá todos los paquetes
- Creará un GitHub Release con todos los artefactos

### Monitorizar Construcciones

#### Panel de GitHub Actions
1. Navegar al repositorio en GitHub
2. Click en pestaña "Actions"
3. Ver workflows en ejecución/completados
4. Click en ejecución específica para detalles

#### Estado de Construcción
- ✅ Marca verde: Éxito
- ❌ X roja: Fallo
- 🟡 Círculo amarillo: En progreso

#### Ver Logs
1. Click en ejecución del workflow
2. Click en trabajo específico (ej: "build-windows")
3. Expandir pasos para ver logs detallados

#### Descargar Artefactos
1. Ir a ejecución completada del workflow
2. Scroll a sección "Artifacts"
3. Descargar artefacto deseado

### Configuración

#### Actualizar Versión de Python
Editar `.github/workflows/build-release.yml`:
```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.11'  # Cambiar versión aquí
```

#### Añadir Pasos de Construcción
Añadir nuevos pasos en el archivo workflow:
```yaml
- name: Paso Personalizado
  run: |
    echo "Ejecutando comando personalizado"
    python custom_script.py
```

## Gestión de Versiones

### Formato de Versión
Seguir Versionado Semántico (SemVer): `MAJOR.MINOR.PATCH`
- MAJOR: Cambios incompatibles
- MINOR: Nuevas funcionalidades (compatible)
- PATCH: Corrección de errores

### Actualizar Versión

1. **Actualizar versión en scripts de construcción:**
   - `build_deb.py`: `VERSION = "0.2.0"`
   - `build_rpm.py`: `VERSION = "0.2.0"`

2. **Crear tag de git:**
   ```bash
   git tag v0.2.0
   git push origin v0.2.0
   ```

3. **GitHub Actions automáticamente:**
   - Construirá todos los paquetes con nueva versión
   - Creará GitHub Release
   - Subirá todos los artefactos

## Monitorización y Resolución de Problemas

### Problemas Comunes

#### PyInstaller Falla
**Síntoma:** Construcción falla con errores de PyInstaller

**Solución:**
```bash
# Limpiar caché
pyinstaller --clean main.py

# Actualizar PyInstaller
pip install --upgrade pyinstaller
```

#### Dependencias Faltantes
**Síntoma:** "ModuleNotFoundError" en ejecutable construido

**Solución:** Añadir al script de construcción:
```python
"--hidden-import=nombre_modulo"
```

#### Archivos de Audio No Encontrados
**Síntoma:** Sin sonido en ejecutable

**Solución:** Verificar `--add-data` en scripts de construcción:
```python
"--add-data=assets;assets"  # Windows
"--add-data=assets:assets"  # Linux
```

### Probar Construcciones Localmente

Antes de publicar en GitHub, probar construcciones localmente:

```bash
# Probar todas las construcciones
python build_windows.py
python build_linux.py
python build_deb.py
python build_rpm.py

# Ejecutar tests
python -m unittest discover -s tests -p "test_*.py"
```

## Mejores Prácticas

1. **Probar localmente antes de publicar tags**
2. **Usar versionado semántico consistentemente**
3. **Documentar cambios en notas de release**
4. **Mantener scripts de construcción simples y mantenibles**
5. **Monitorizar uso de GitHub Actions (límites de tier gratuito)**
6. **Cachear dependencias cuando sea posible**
7. **Usar versiones específicas de actions (no @latest)**

## Soporte

Para problemas con:
- **Scripts de construcción:** Revisar logs y mensajes de error
- **GitHub Actions:** Revisar logs de workflow en pestaña Actions
- **Paquetes:** Probar instalación en sistema limpio
- **Aplicación:** Ejecutar tests unitarios y revisar logs de aplicación

## Referencias

- [Documentación PyInstaller](https://pyinstaller.org/)
- [Documentación GitHub Actions](https://docs.github.com/en/actions)
- [Guía de Empaquetado Debian](https://www.debian.org/doc/manuals/maint-guide/)
- [Guía de Empaquetado RPM](https://rpm-packaging-guide.github.io/)
