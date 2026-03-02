#!/usr/bin/env python3
"""
Script para crear paquete .rpm para RedHat/Fedora/CentOS.
"""
import os
import sys
import shutil
import subprocess

VERSION = "0.1.0"
PACKAGE_NAME = "pomodoro-timer"

def create_rpm_package():
    """Crea el paquete .rpm."""
    print("=== Creating RPM package ===")
    
    # Crear estructura de directorios
    rpm_dirs = ["BUILD", "RPMS", "SOURCES", "SPECS", "SRPMS"]
    for d in rpm_dirs:
        os.makedirs(d, exist_ok=True)
    
    # Crear tarball de fuentes
    source_dir = f"{PACKAGE_NAME}-{VERSION}"
    if os.path.exists(source_dir):
        shutil.rmtree(source_dir)
    
    os.makedirs(source_dir)
    shutil.copy("main.py", source_dir)
    shutil.copytree("pomopy", f"{source_dir}/pomopy")
    shutil.copytree("assets", f"{source_dir}/assets")
    shutil.copy("config.example.yaml", source_dir)
    
    subprocess.check_call(["tar", "czf", f"SOURCES/{source_dir}.tar.gz", source_dir])
    shutil.rmtree(source_dir)
    
    # Crear archivo .spec
    spec = f"""Name:           {PACKAGE_NAME}
Version:        {VERSION}
Release:        1%{{?dist}}
Summary:        Pomodoro Timer Desktop Application

License:        MIT
URL:            https://github.com/yourusername/{PACKAGE_NAME}
Source0:        %{{name}}-%{{version}}.tar.gz

Requires:       python3 >= 3.8
Requires:       python3-pyyaml
Requires:       python3-pygame

%description
Desktop application implementing the Pomodoro time management technique.
Features timer with visual countdown, sound alarms, and task management.

%prep
%setup -q

%install
mkdir -p %{{buildroot}}/usr/share/%{{name}}
mkdir -p %{{buildroot}}/usr/local/bin
cp -r * %{{buildroot}}/usr/share/%{{name}}/

cat > %{{buildroot}}/usr/local/bin/%{{name}} << EOF
#!/bin/bash
cd /usr/share/%{{name}}
python3 main.py
EOF
chmod +x %{{buildroot}}/usr/local/bin/%{{name}}

%files
/usr/share/%{{name}}
/usr/local/bin/%{{name}}

%changelog
* {subprocess.check_output(['date', '+%a %b %d %Y']).decode().strip()} Builder <builder@example.com> - {VERSION}-1
- Initial package
"""
    
    with open(f"SPECS/{PACKAGE_NAME}.spec", "w") as f:
        f.write(spec)
    
    # Construir paquete
    subprocess.check_call(["rpmbuild", "-ba", f"SPECS/{PACKAGE_NAME}.spec", 
                          "--define", f"_topdir {os.getcwd()}"])
    
    print(f"\n=== Package created in RPMS/ ===")

if __name__ == "__main__":
    create_rpm_package()
