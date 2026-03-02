#!/usr/bin/env python3
"""
Script para crear paquete .deb para Debian/Ubuntu.
"""
import os
import sys
import shutil
import subprocess

VERSION = "0.1.0"
PACKAGE_NAME = "pomodoro-timer"

def create_deb_package():
    """Crea el paquete .deb."""
    print("=== Creating Debian package ===")
    
    # Crear estructura de directorios
    deb_dir = f"{PACKAGE_NAME}_{VERSION}"
    if os.path.exists(deb_dir):
        shutil.rmtree(deb_dir)
    
    os.makedirs(f"{deb_dir}/DEBIAN")
    os.makedirs(f"{deb_dir}/usr/local/bin")
    os.makedirs(f"{deb_dir}/usr/share/{PACKAGE_NAME}")
    os.makedirs(f"{deb_dir}/usr/share/applications")
    
    # Copiar archivos
    shutil.copy("main.py", f"{deb_dir}/usr/share/{PACKAGE_NAME}/")
    shutil.copytree("pomopy", f"{deb_dir}/usr/share/{PACKAGE_NAME}/pomopy")
    shutil.copytree("assets", f"{deb_dir}/usr/share/{PACKAGE_NAME}/assets")
    shutil.copy("config.example.yaml", f"{deb_dir}/usr/share/{PACKAGE_NAME}/")
    
    # Crear script de lanzamiento
    launcher = f"""#!/bin/bash
cd /usr/share/{PACKAGE_NAME}
python3 main.py
"""
    with open(f"{deb_dir}/usr/local/bin/{PACKAGE_NAME}", "w") as f:
        f.write(launcher)
    os.chmod(f"{deb_dir}/usr/local/bin/{PACKAGE_NAME}", 0o755)
    
    # Crear archivo control
    control = f"""Package: {PACKAGE_NAME}
Version: {VERSION}
Section: utils
Priority: optional
Architecture: all
Depends: python3 (>= 3.8), python3-yaml, python3-pygame
Maintainer: Pomodoro Timer Team <team@example.com>
Description: Pomodoro Timer Desktop Application
 Desktop application implementing the Pomodoro time management technique.
 Features timer with visual countdown, sound alarms, and task management.
"""
    with open(f"{deb_dir}/DEBIAN/control", "w") as f:
        f.write(control)
    
    # Crear archivo .desktop
    desktop = f"""[Desktop Entry]
Name=Pomodoro Timer
Comment=Time management using Pomodoro technique
Exec={PACKAGE_NAME}
Terminal=false
Type=Application
Categories=Utility;Office;
"""
    with open(f"{deb_dir}/usr/share/applications/{PACKAGE_NAME}.desktop", "w") as f:
        f.write(desktop)
    
    # Construir paquete
    subprocess.check_call(["dpkg-deb", "--build", deb_dir])
    
    print(f"\n=== Package created: {deb_dir}.deb ===")

if __name__ == "__main__":
    create_deb_package()
