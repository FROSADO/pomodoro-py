"""
Module de gestión de la lógica de negocio del Pomodoro Timer.
Coordina el temporizador, tareas y sonidos.
"""
from pomopy.pomodoro_timer import PomodoroTimer
from pomopy.tasks import TaskManager
from pomopy.sounds import SoundManager


class PomodoroManager:
    """Class que gestiona la lógica de negocio de la aplicación Pomodoro."""
    
    def __init__(self, config):
        """
        Initializes el gestor de Pomodoro.
        
        Args:
            config: Instancia de Config
        """
        self.config = config
        self.current_mode = 'work'
        
        # Initializesr componentes
        self.task_manager = TaskManager(
            tasks_file=config.TASKS_FILE,
            work_time=config.WORK_TIME,
            short_break_time=config.SHORT_BREAK,
            long_break_time=config.LONG_BREAK,
            tasks_folder=config.TASKS_FOLDER
        )
        self.sound_manager = SoundManager(
            alarm_file=config.ALARM_FILE,
            ticking_file=config.TICKING_FILE,
            enabled=config.SOUND_ENABLED
        )
        self.timer = PomodoroTimer(
            config.get_time_for_mode(self.current_mode),
            on_finish=self._on_timer_finish
        )
        
        # Callback para notificar a la GUI
        self.on_finish_callback = None
    
    def set_finish_callback(self, callback):
        """
        Sets el callback para notificar cuando termina un período.
        
        Args:
            callback: Function a llamar cuando termina
        """
        self.on_finish_callback = callback
    
    def start_timer(self):
        """Starts el temporizador."""
        self.timer.start()
        if self.current_mode == 'work':
            self.sound_manager.start_ticking()
    
    def pause_timer(self):
        """Pauses el temporizador."""
        self.timer.pause()
        self.sound_manager.stop_ticking()
    
    def reset_timer(self):
        """Resets el temporizador al tiempo inicial del modo actual."""
        self.timer.reset()
        self.sound_manager.stop_ticking()
    
    def change_mode(self, mode):
        """
        Changes el modo del temporizador.
        
        Args:
            mode: 'work', 'short_break' o 'long_break'
        """
        self.current_mode = mode
        new_time = self.config.get_time_for_mode(mode)
        self.timer.reset(new_time)
        self.sound_manager.stop_ticking()
    
    def tick(self):
        """Decrements el tiempo en 1 segundo."""
        self.timer.tick()
    
    def is_running(self):
        """Verifies si el temporizador está corriendo."""
        return self.timer.is_running
    
    def get_time_formatted(self):
        """Gets el tiempo formateado MM:SS."""
        return self.timer.get_time_formatted()
    
    def get_current_mode(self):
        """Gets el modo actual."""
        return self.current_mode
    
    def set_task(self, task_name):
        """
        Sets la tarea actual.
        
        Args:
            task_name: Nombre de la tarea
        """
        self.task_manager.set_task(task_name)
    
    def get_task(self):
        """Gets el nombre de la tarea actual."""
        return self.task_manager.get_task()
    
    def complete_task(self):
        """
        Completes la tarea actual.
        
        Returns:
            True si se completó correctamente
        """
        return self.task_manager.complete_task()
    
    def get_stats(self):
        """
        Gets las estadísticas actuales.
        
        Returns:
            Diccionario con estadísticas
        """
        return self.task_manager.get_session_stats()
    
    def get_total_work_time(self):
        """
        Calculates el tiempo total de trabajo en formato MM:SS.
        
        Returns:
            String con formato MM:SS
        """
        total_seconds = self.task_manager.work_count * (self.config.WORK_TIME)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def get_total_break_time(self):
        """
        Calculates el tiempo total de descanso en formato MM:SS.
        
        Returns:
            String con formato MM:SS
        """
        short_seconds = self.task_manager.short_break_count * self.config.SHORT_BREAK
        long_seconds = self.task_manager.long_break_count * self.config.LONG_BREAK
        total_seconds = short_seconds + long_seconds
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def _on_timer_finish(self):
        """Callback interno cuando el temporizador termina."""
        # Detener ticking
        self.sound_manager.stop_ticking()
        
        # Incrementsr contadores según el modo
        if self.current_mode == 'work':
            self.task_manager.increment_work()
        elif self.current_mode == 'short_break':
            self.task_manager.increment_short_break()
        elif self.current_mode == 'long_break':
            self.task_manager.increment_long_break()
        
        # Reproducir alarma
        if self.config.SOUND_ENABLED and self.sound_manager.is_available():
            self.sound_manager.play_alarm(times=5, interval=2000)
        
        # Notificar a la GUI
        if self.on_finish_callback:
            self.on_finish_callback()
    
    def set_volume(self, volume):
        """
        Sets el volumen.
        
        Args:
            volume: Value entre 0.0 y 1.0
        """
        self.sound_manager.set_volume(volume)
    
    def get_volume(self):
        """
        Gets el volumen actual.
        
        Returns:
            Value entre 0.0 y 1.0
        """
        return self.sound_manager.get_volume()
    
    def increment_meeting_time(self, seconds):
        """Increments el tiempo de reunión."""
        self.task_manager.increment_meeting_time(seconds)
    
    def get_meeting_time(self):
        """Gets el tiempo de reunión formateado."""
        return self.task_manager.get_meeting_time()
    
    def save_meeting(self):
        """Guarda el tiempo de reunión como tarea."""
        return self.task_manager.save_meeting()
