# Configuración de Protección de Ramas en GitHub

Este documento explica cómo configurar GitHub para que requiera que los tests pasen antes de permitir merge de Pull Requests.

## Configuración Automática de Tests

El workflow de GitHub Actions (`.github/workflows/build-release.yml`) está configurado para ejecutarse automáticamente en:

- **Pull Requests** hacia `main` o `develop`
- **Push** a las ramas `main` o `develop`
- **Tags** con formato `v*` (para releases)
- **Manualmente** desde la interfaz de GitHub Actions

## Configurar Protección de Rama en GitHub

Para requerir que los tests pasen antes de hacer merge:

### 1. Acceder a Configuración del Repositorio

1. Ve a tu repositorio en GitHub
2. Click en **Settings** (Configuración)
3. En el menú lateral, click en **Branches** (Ramas)

### 2. Añadir Regla de Protección

1. Click en **Add branch protection rule** (Añadir regla de protección de rama)
2. En **Branch name pattern**, escribe: `main` (o la rama que quieras proteger)

### 3. Configurar Requisitos

Marca las siguientes opciones:

#### Requerir Pull Request antes de merge:
- ☑️ **Require a pull request before merging**
  - ☑️ **Require approvals** (opcional, número de aprobaciones requeridas)

#### Requerir que los checks pasen:
- ☑️ **Require status checks to pass before merging**
  - ☑️ **Require branches to be up to date before merging**
  - En la lista de checks, selecciona: **test** (el job de tests del workflow)

#### Otras opciones recomendadas:
- ☑️ **Require conversation resolution before merging** (resolver comentarios)
- ☑️ **Do not allow bypassing the above settings** (no permitir bypass)

### 4. Guardar Cambios

Click en **Create** o **Save changes** al final de la página.

## Verificación

Una vez configurado:

1. Crea un Pull Request
2. Verás que aparece un check llamado "test" en el PR
3. El botón de merge estará deshabilitado hasta que el check pase
4. Si los tests fallan, no se podrá hacer merge

## Ejemplo de Configuración Mínima

```yaml
# Configuración mínima recomendada:
Branch protection rule for: main

✓ Require a pull request before merging
  - Require approvals: 1

✓ Require status checks to pass before merging
  - Require branches to be up to date before merging
  - Status checks that are required:
    ✓ test

✓ Do not allow bypassing the above settings
```

## Troubleshooting

### El check "test" no aparece en la lista

**Solución**: Primero debes ejecutar el workflow al menos una vez:
1. Crea un PR de prueba
2. El workflow se ejecutará automáticamente
3. Después de la primera ejecución, "test" aparecerá en la lista de checks disponibles
4. Vuelve a la configuración de protección de rama y selecciona "test"

### Los tests fallan en CI pero pasan localmente

**Causas comunes**:
- Diferencias en el entorno (Linux en CI vs Windows/Mac local)
- Falta de dispositivos de audio en CI (para tests de sonido)
- Dependencias no instaladas correctamente

**Solución**: Los tests ya están configurados para manejar la ausencia de audio en CI.

## Documentación Oficial

Para más información, consulta:
- [GitHub Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub Actions Status Checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)
