"""
Module de configuración para la aplicación Pomodoro Timer.
Contiene valores por defecto y carga configuración desde config.yaml si existe.
"""
import os
from pathlib import Path
import yaml


class Config:
    """Class de configuración con valores por defecto y carga desde archivo YAML."""
    
    # Times en segundos (valores por defecto)
    WORK_TIME = 25 * 60  # 25 minutos
    SHORT_BREAK = 5 * 60  # 5 minutos
    LONG_BREAK = 15 * 60  # 15 minutos
    
    # Colores de la interfaz
    WORK_COLOR = "#FF6B6B"  # Rojo claro
    SHORT_BREAK_COLOR = "#4ECDC4"  # Verde azulado
    LONG_BREAK_COLOR = "#45B7D1"  # Azul claro
    BG_COLOR = "#2C3E50"  # Fondo oscuro
    TEXT_COLOR = "#FFFFFF"  # Texto blanco
    
    # Configuration de ventana
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 500
    ALWAYS_ON_TOP = True
    
    # Configuration de sonido
    SOUND_ENABLED = True
    ALARM_FILE = "assets/alarm-digital.mp3"
    TICKING_FILE = "assets/ticking-slow.mp3"
    
    # Configuration de tareas
    TASKS_FILE = "tasks.txt"
    
    def __init__(self, config_file="config.yaml", silent=False):
        """
        Initializes la configuración cargando valores desde archivo YAML si existe.
        
        Args:
            config_file: Path al archivo de configuración YAML
            silent: Si es True, no muestra mensajes de error
        """
        self.config_file = config_file
        self.silent = silent
        self._load_config()
    
    def _load_config(self):
        """Loads configuración desde archivo YAML si existe."""
        if not os.path.exists(self.config_file):
            return
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config_data = yaml.safe_load(f)
            
            if not config_data:
                return
            
            # Loadsr tiempos (convertir minutos a segundos)
            if 'times' in config_data:
                times = config_data['times']
                if 'work_time' in times:
                    self.WORK_TIME = times['work_time'] * 60
                if 'short_break' in times:
                    self.SHORT_BREAK = times['short_break'] * 60
                if 'long_break' in times:
                    self.LONG_BREAK = times['long_break'] * 60
            
            # Loadsr colores
            if 'colors' in config_data:
                colors = config_data['colors']
                if 'work_color' in colors:
                    self.WORK_COLOR = colors['work_color']
                if 'short_break_color' in colors:
                    self.SHORT_BREAK_COLOR = colors['short_break_color']
                if 'long_break_color' in colors:
                    self.LONG_BREAK_COLOR = colors['long_break_color']
                if 'bg_color' in colors:
                    self.BG_COLOR = colors['bg_color']
                if 'text_color' in colors:
                    self.TEXT_COLOR = colors['text_color']
            
            # Loadsr configuración de ventana
            if 'window' in config_data:
                window = config_data['window']
                if 'width' in window:
                    self.WINDOW_WIDTH = window['width']
                if 'height' in window:
                    self.WINDOW_HEIGHT = window['height']
                if 'always_on_top' in window:
                    self.ALWAYS_ON_TOP = window['always_on_top']
            
            # Loadsr configuración de sonido
            if 'sound' in config_data:
                sound = config_data['sound']
                if 'enabled' in sound:
                    self.SOUND_ENABLED = sound['enabled']
                if 'alarm_file' in sound:
                    self.ALARM_FILE = sound['alarm_file']
                if 'ticking_file' in sound:
                    self.TICKING_FILE = sound['ticking_file']
            
            # Loadsr configuración de tareas
            if 'tasks' in config_data:
                tasks = config_data['tasks']
                if 'file' in tasks:
                    self.TASKS_FILE = tasks['file']
                    
        except Exception as e:
            if not self.silent:
                print(f"Error al cargar configuración: {e}")
                print("Usando valores por defecto")
    
    def get_time_for_mode(self, mode):
        """
        Gets el tiempo configurado para un modo específico.
        
        Args:
            mode: 'work', 'short_break' o 'long_break'
            
        Returns:
            Time en segundos para el modo especificado
        """
        mode_map = {
            'work': self.WORK_TIME,
            'short_break': self.SHORT_BREAK,
            'long_break': self.LONG_BREAK
        }
        return mode_map.get(mode, self.WORK_TIME)
    
    def get_color_for_mode(self, mode):
        """
        Gets el color configurado para un modo específico.
        
        Args:
            mode: 'work', 'short_break' o 'long_break'
            
        Returns:
            Color hexadecimal para el modo especificado
        """
        color_map = {
            'work': self.WORK_COLOR,
            'short_break': self.SHORT_BREAK_COLOR,
            'long_break': self.LONG_BREAK_COLOR
        }
        return color_map.get(mode, self.WORK_COLOR)
