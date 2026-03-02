"""
PyInstaller hook para excluir módulos innecesarios de pygame.
"""
from PyInstaller.utils.hooks import collect_submodules

# Solo incluir módulos necesarios
hiddenimports = ['pygame.mixer', 'pygame.time', 'pygame.base']

# Excluir tests, ejemplos y módulos no usados
excludedimports = [
    'pygame.tests',
    'pygame.examples',
    'pygame._camera',
    'pygame._camera_opencv',
    'pygame._camera_vidcapture',
    'pygame.camera',
    'pygame.cdrom',
    'pygame.joystick',
    'pygame.midi',
    'pygame.movie',
    'pygame._sdl2',
    'pygame.fastevent',
]
