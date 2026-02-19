"""
Module de lógica del temporizador Pomodoro.
Gestiona el tiempo, estados y callbacks.
"""


class PomodoroTimer:
    """Class que gestiona la lógica del temporizador Pomodoro."""
    
    def __init__(self, initial_time, on_finish=None):
        """
        Initializes el temporizador.
        
        Args:
            initial_time: Time inicial en segundos
            on_finish: Callback opcional que se ejecuta cuando el tiempo llega a 0
        """
        self.initial_time = initial_time
        self.time_left = initial_time
        self.is_running = False
        self.on_finish = on_finish
    
    def start(self):
        """Starts el temporizador."""
        self.is_running = True
    
    def pause(self):
        """Pauses el temporizador."""
        self.is_running = False
    
    def reset(self, new_time=None):
        """
        Resets el temporizador.
        
        Args:
            new_time: Nuevo tiempo inicial en segundos. Si es None, usa initial_time
        """
        if new_time is not None:
            self.initial_time = new_time
        self.time_left = self.initial_time
        self.is_running = False
    
    def tick(self):
        """
        Decrements el tiempo en 1 segundo si está corriendo.
        Ejecuta callback si el tiempo llega a 0.
        
        Returns:
            True si el tiempo llegó a 0, False en caso contrario
        """
        if not self.is_running:
            return False
        
        if self.time_left > 0:
            self.time_left -= 1
        
        if self.time_left == 0:
            self.is_running = False
            if self.on_finish:
                self.on_finish()
            return True
        
        return False
    
    def get_time_formatted(self):
        """
        Gets el tiempo restante en formato MM:SS.
        
        Returns:
            String con formato MM:SS
        """
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def is_finished(self):
        """
        Verifies si el temporizador ha terminado.
        
        Returns:
            True si el tiempo es 0, False en caso contrario
        """
        return self.time_left == 0
