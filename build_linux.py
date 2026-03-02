#!/usr/bin/env python3
"""
Script para construir el ejecutable de Linux usando PyInstaller.
"""
import os
import sys
import shutil
import subprocess

def build_linux():
    """Construye el ejecutable para Linux."""
    print("=== Building Linux executable ===")
    
    # Verificar que PyInstaller está instalado
    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("ERROR: PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Limpiar builds anteriores
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    
    # Comando PyInstaller
    cmd = [
        "pyinstaller",
        "--name=pomodoro-timer",
        "--windowed",
        "--onefile",
        "--add-data=assets:assets",
        "--add-data=config.example.yaml:.",
        "--collect-all=pygame",
        "--exclude-module=pygame.tests",
        "--exclude-module=pygame.examples",
        "--exclude-module=pygame.camera",
        "--exclude-module=pygame.midi",
        "--exclude-module=pygame.joystick",
        "main.py"
    ]
    
    print(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd)
    
    print("\n=== Build completed ===")
    print(f"Executable: dist/pomodoro-timer")

if __name__ == "__main__":
    build_linux()
