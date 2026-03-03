"""
Script para construir el ejecutable de Windows usando PyInstaller.
"""
import os
import sys
import shutil
import subprocess

def build_windows():
    """Construye el ejecutable para Windows."""
    print("=== Building Windows executable ===")
    
    # Verificar que PyInstaller está instalado
    try:
        import PyInstaller
        print(f"PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("ERROR: PyInstaller not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], 
                      creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
    
    # Limpiar builds anteriores
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    
    # Comando PyInstaller
    cmd = [
        "pyinstaller",
        "--name=PomodoroTimer",
        "--windowed",
        "--onedir",
        "--add-data=assets;assets",
        "--add-data=config.example.yaml;.",
        "--additional-hooks-dir=.",
        "--icon=assets/icon.ico" if os.path.exists("assets/icon.ico") else "",
        "main.py"
    ]
    
    # Filtrar argumentos vacíos
    cmd = [arg for arg in cmd if arg]
    
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0, check=True)
    
    print("\n=== Build completed ===")
    print(f"Executable directory: dist/PomodoroTimer/")
    
    # Crear ZIP para distribución
    print("\n=== Creating ZIP distribution ===")
    zip_name = "PomodoroTimer-Windows"
    shutil.make_archive(f"dist/{zip_name}", 'zip', 'dist', 'PomodoroTimer')
    print(f"ZIP created: dist/{zip_name}.zip")

if __name__ == "__main__":
    build_windows()
