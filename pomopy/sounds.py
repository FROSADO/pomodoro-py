"""
Module de gestión de sonidos para la aplicación Pomodoro Timer.
"""
import os

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False


class SoundManager:
    """Class que gestiona la reproducción de sonidos."""
    
    def __init__(self, alarm_file='alarm-digital.mp3', ticking_file='ticking-slow.mp3', enabled=True):
        """
        Initializes el gestor de sonidos.
        
        Args:
            alarm_file: Path al archivo de alarma
            ticking_file: Path al archivo de ticking
            enabled: Si está habilitado el sonido
        """
        self.alarm_file = alarm_file
        self.ticking_file = ticking_file
        self.enabled = enabled
        self.alarm_count = 0
        self.callback = None
        self.ticking_playing = False
        
        if PYGAME_AVAILABLE and enabled:
            try:
                pygame.mixer.init()
                self.initialized = True
            except:
                self.initialized = False
        else:
            self.initialized = False
    
    def play_alarm(self, times=5, interval=2000, callback=None):
        """
        Plays la alarma un número específico de veces.
        
        Args:
            times: Número de veces a reproducir
            interval: Intervalo en milisegundos entre reproducciones
            callback: Function a llamar después de cada reproducción
        """
        if not self.enabled:
            return
        
        self.alarm_count = 0
        self.times = times
        self.interval = interval
        self.callback = callback
        self._play_once()
    
    def _play_once(self):
        """Plays la alarma una vez."""
        if self.alarm_count < self.times:
            if self.initialized and os.path.exists(self.alarm_file):
                try:
                    pygame.mixer.music.load(self.alarm_file)
                    pygame.mixer.music.play()
                except:
                    pass
            
            self.alarm_count += 1
            
            if self.callback:
                self.callback(self.alarm_count, self._play_once if self.alarm_count < self.times else None)
        else:
            self.alarm_count = 0
    
    def stop(self):
        """Stops la reproducción de sonido."""
        if self.initialized:
            try:
                pygame.mixer.music.stop()
            except:
                pass
        self.alarm_count = 0
        self.ticking_playing = False
    
    def start_ticking(self):
        """Starts el sonido de ticking en bucle."""
        if not self.enabled or not self.initialized:
            return
        
        if os.path.exists(self.ticking_file) and not self.ticking_playing:
            try:
                pygame.mixer.music.load(self.ticking_file)
                pygame.mixer.music.play(-1)  # -1 = bucle infinito
                self.ticking_playing = True
            except:
                pass
    
    def stop_ticking(self):
        """Stops el sonido de ticking."""
        if self.ticking_playing:
            try:
                pygame.mixer.music.stop()
                self.ticking_playing = False
            except:
                pass
    
    def set_volume(self, volume):
        """
        Sets el volumen de reproducción.
        
        Args:
            volume: Value entre 0.0 y 1.0
        """
        if self.initialized:
            try:
                pygame.mixer.music.set_volume(volume)
            except:
                pass
    
    def get_volume(self):
        """
        Gets el volumen actual.
        
        Returns:
            Value entre 0.0 y 1.0
        """
        if self.initialized:
            try:
                return pygame.mixer.music.get_volume()
            except:
                return 1.0
        return 1.0
    
    def is_available(self):
        """
        Verifies si el sonido está disponible.
        
        Returns:
            True si pygame está disponible y el archivo existe
        """
        return self.initialized and os.path.exists(self.alarm_file)
