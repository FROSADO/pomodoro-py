# Distribution Guide - Pomodoro Timer

This guide explains how to build and distribute the Pomodoro Timer application for different platforms.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Building Locally](#building-locally)
3. [CI/CD with GitHub Actions](#cicd-with-github-actions)
4. [Version Management](#version-management)
5. [Monitoring and Troubleshooting](#monitoring-and-troubleshooting)

## Prerequisites

### All Platforms
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Windows
- PyInstaller: `pip install pyinstaller`

### Linux (Debian/Ubuntu)
- PyInstaller: `pip install pyinstaller`
- dpkg-dev: `sudo apt-get install dpkg-dev`

### Linux (RedHat/Fedora/CentOS)
- PyInstaller: `pip install pyinstaller`
- rpm-build: `sudo yum install rpm-build`

## Building Locally

### Windows Executable

```bash
# Install dependencies
pip install -r requirements.txt
pip install pyinstaller

# Build executable
python build_windows.py

# Output: dist/PomodoroTimer.exe
```

**Configuration:**
- Edit `build_windows.py` to customize:
  - Application name
  - Icon file (place in `assets/icon.ico`)
  - Additional data files

### Linux Executable

```bash
# Install dependencies
pip install -r requirements.txt
pip install pyinstaller

# Build executable
python build_linux.py

# Output: dist/pomodoro-timer
```

### Debian Package (.deb)

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install dpkg-dev

# Build package
python build_deb.py

# Output: pomodoro-timer_0.1.0.deb
```

**Installation:**
```bash
sudo dpkg -i pomodoro-timer_0.1.0.deb
sudo apt-get install -f  # Fix dependencies if needed
```

**Uninstallation:**
```bash
sudo apt-get remove pomodoro-timer
```

### RPM Package (.rpm)

```bash
# Install dependencies
sudo yum install rpm-build

# Build package
python build_rpm.py

# Output: RPMS/noarch/pomodoro-timer-0.1.0-1.noarch.rpm
```

**Installation:**
```bash
sudo rpm -i RPMS/noarch/pomodoro-timer-0.1.0-1.noarch.rpm
```

**Uninstallation:**
```bash
sudo rpm -e pomodoro-timer
```

## CI/CD with GitHub Actions

### Workflow Overview

The project uses GitHub Actions for automated building and releasing. The workflow is defined in `.github/workflows/build-release.yml`.

### GITHUB_TOKEN Configuration

#### What is GITHUB_TOKEN?

`GITHUB_TOKEN` is an **automatic** authentication token that GitHub provides to each GitHub Actions workflow. **You don't need to create or configure it manually**.

**Features**:
- ✅ **Automatic**: GitHub creates it automatically for each workflow run
- ✅ **Secure**: Expires when the workflow finishes
- ✅ **No configuration needed**: You don't need to add it in Settings > Secrets
- ✅ **Permissions**: Has permissions to create releases, upload files, etc.

#### How it's used in the workflow

In the `.github/workflows/build-release.yml` file:

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
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # ← Automatic, no configuration needed
```

#### Configuring permissions (if needed)

By default, `GITHUB_TOKEN` has read and write permissions. If you encounter permission errors:

**Option 1: In the workflow (Recommended)**

Add at the beginning of `.github/workflows/build-release.yml`:

```yaml
name: Build and Release

permissions:
  contents: write  # Required to create releases
  packages: write  # Optional, for publishing packages

on:
  push:
    tags:
      - 'v*'
```

**Option 2: At repository level**

1. Go to **Settings** > **Actions** > **General**
2. Under "Workflow permissions", select:
   - ☑️ **Read and write permissions**
3. Click **Save**

#### GITHUB_TOKEN Troubleshooting

**Error: "Resource not accessible by integration"**
- **Cause**: GITHUB_TOKEN doesn't have sufficient permissions
- **Solution**: Add `permissions: contents: write` to the workflow (see Option 1 above)

**Error: "Bad credentials"**
- **Cause**: Rare, may occur with special repository configurations
- **Solution**: Verify the workflow is on the correct branch

**Do you need a Personal Access Token (PAT)?**

**NO** for this project. You would only need a PAT if:
- You want to push to another repository
- You need to access GitHub APIs outside the current repository
- You want to trigger workflows in other repositories

### Workflow Stages

1. **Test** - Runs all unit tests
2. **Build Windows** - Creates Windows executable
3. **Build Linux** - Creates Linux executable
4. **Build Debian** - Creates .deb package
5. **Build RPM** - Creates .rpm package
6. **Release** - Publishes artifacts to GitHub Releases (only on tags)

### Triggering Builds

#### Manual Trigger
1. Go to GitHub repository
2. Click "Actions" tab
3. Select "Build and Release" workflow
4. Click "Run workflow"

#### Automatic Trigger (Release)
```bash
# Create and push a version tag
git tag v0.1.0
git push origin v0.1.0
```

This will:
- Run all tests
- Build all platform packages
- Create a GitHub Release with all artifacts

### Monitoring Builds

#### GitHub Actions Dashboard
1. Navigate to repository on GitHub
2. Click "Actions" tab
3. View running/completed workflows
4. Click on specific workflow run for details

#### Build Status
- ✅ Green checkmark: Success
- ❌ Red X: Failed
- 🟡 Yellow circle: In progress

#### Viewing Logs
1. Click on workflow run
2. Click on specific job (e.g., "build-windows")
3. Expand steps to view detailed logs

#### Downloading Artifacts
1. Go to completed workflow run
2. Scroll to "Artifacts" section
3. Download desired artifact

### Configuration

#### Updating Python Version
Edit `.github/workflows/build-release.yml`:
```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.11'  # Change version here
```

#### Adding Build Steps
Add new steps in the workflow file:
```yaml
- name: Custom Step
  run: |
    echo "Running custom command"
    python custom_script.py
```

#### Modifying Release Files
Edit the `release` job in workflow:
```yaml
- name: Create Release
  uses: softprops/action-gh-release@v1
  with:
    files: |
      pomodoro-timer-windows/PomodoroTimer.exe
      pomodoro-timer-linux/pomodoro-timer
      # Add more files here
```

## Version Management

### Version Format
Follow Semantic Versioning (SemVer): `MAJOR.MINOR.PATCH`
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

### Updating Version

1. **Update version in build scripts:**
   - `build_deb.py`: `VERSION = "0.2.0"`
   - `build_rpm.py`: `VERSION = "0.2.0"`

2. **Create git tag:**
   ```bash
   git tag v0.2.0
   git push origin v0.2.0
   ```

3. **GitHub Actions will automatically:**
   - Build all packages with new version
   - Create GitHub Release
   - Upload all artifacts

### Release Notes

Create release notes in GitHub:
1. Go to "Releases" tab
2. Click on the release
3. Click "Edit release"
4. Add description and changelog

## Monitoring and Troubleshooting

### Common Issues

#### PyInstaller Fails
**Symptom:** Build fails with PyInstaller errors

**Solution:**
```bash
# Clear cache
pyinstaller --clean main.py

# Update PyInstaller
pip install --upgrade pyinstaller
```

#### Missing Dependencies
**Symptom:** "ModuleNotFoundError" in built executable

**Solution:** Add to build script:
```python
"--hidden-import=module_name"
```

#### Audio Files Not Found
**Symptom:** No sound in executable

**Solution:** Verify `--add-data` in build scripts:
```python
"--add-data=assets;assets"  # Windows
"--add-data=assets:assets"  # Linux
```

#### GitHub Actions Timeout
**Symptom:** Workflow exceeds time limit

**Solution:** Optimize build or increase timeout:
```yaml
jobs:
  build-windows:
    timeout-minutes: 30  # Default is 360
```

### Testing Builds Locally

Before pushing to GitHub, test builds locally:

```bash
# Test all builds
python build_windows.py
python build_linux.py
python build_deb.py
python build_rpm.py

# Run tests
python -m unittest discover -s tests -p "test_*.py"
```

### Logs and Debugging

#### Enable Verbose Logging
Add to build scripts:
```python
subprocess.check_call(cmd, env={**os.environ, "PYTHONVERBOSE": "1"})
```

#### GitHub Actions Debug Logging
Enable in workflow:
```yaml
env:
  ACTIONS_STEP_DEBUG: true
```

### Performance Monitoring

#### Build Times
Monitor in GitHub Actions:
- Typical Windows build: 5-10 minutes
- Typical Linux build: 3-5 minutes
- Typical package builds: 2-3 minutes

#### Artifact Sizes
Expected sizes:
- Windows .exe: 30-50 MB
- Linux binary: 30-50 MB
- .deb package: 5-10 MB
- .rpm package: 5-10 MB

## Best Practices

1. **Test locally before pushing tags**
2. **Use semantic versioning consistently**
3. **Document changes in release notes**
4. **Keep build scripts simple and maintainable**
5. **Monitor GitHub Actions usage (free tier limits)**
6. **Cache dependencies when possible**
7. **Use specific action versions (not @latest)**

## Support

For issues with:
- **Build scripts:** Check script logs and error messages
- **GitHub Actions:** Review workflow logs in Actions tab
- **Packages:** Test installation on clean system
- **Application:** Run unit tests and check application logs

## References

- [PyInstaller Documentation](https://pyinstaller.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Debian Packaging Guide](https://www.debian.org/doc/manuals/maint-guide/)
- [RPM Packaging Guide](https://rpm-packaging-guide.github.io/)
