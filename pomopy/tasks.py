"""
Module de gestión de tareas para la aplicación Pomodoro Timer.
"""
import os
from datetime import datetime


class TaskManager:
    """Class que gestiona las tareas y su persistencia."""
    
    def __init__(self, tasks_file='tasks.txt', work_time=1500, short_break_time=300, long_break_time=900):
        """
        Initializes el gestor de tareas.
        
        Args:
            tasks_file: Path al archivo de tareas
            work_time: Time de trabajo en segundos
            short_break_time: Time de descanso corto en segundos
            long_break_time: Time de descanso largo en segundos
        """
        self.tasks_file = tasks_file
        self.current_task = ""
        self.work_count = 0
        self.short_break_count = 0
        self.long_break_count = 0
        self.work_time = work_time
        self.short_break_time = short_break_time
        self.long_break_time = long_break_time
    
    def set_task(self, task_name):
        """
        Sets la tarea actual.
        
        Args:
            task_name: Nombre de la tarea
        """
        self.current_task = task_name.strip()
    
    def get_task(self):
        """
        Gets la tarea actual.
        
        Returns:
            Nombre de la tarea actual
        """
        return self.current_task
    
    def increment_work(self):
        """Increments el contador de pomodoros de trabajo."""
        self.work_count += 1
    
    def increment_short_break(self):
        """Increments el contador de descansos cortos."""
        self.short_break_count += 1
    
    def increment_long_break(self):
        """Increments el contador de descansos largos."""
        self.long_break_count += 1
    
    def get_total_time(self):
        """
        Calculates el tiempo total basado en pomodoros y descansos.
        
        Returns:
            String con formato HH:mm:ss
        """
        total_seconds = (
            self.work_count * self.work_time +
            self.short_break_count * self.short_break_time +
            self.long_break_count * self.long_break_time
        )
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    def complete_task(self):
        """
        Completes la tarea actual y la guarda en el archivo.
        
        Returns:
            True si se guardó correctamente, False si no hay tarea
        """
        if not self.current_task:
            return False
        
        total_time = self.get_total_time()
        
        # Format: "Nombre" | Pomodoros | Descansos cortos | Descansos largos | Time total
        line = f'"{self.current_task}" | {self.work_count} | {self.short_break_count} | {self.long_break_count} | {total_time}\n'
        
        try:
            with open(self.tasks_file, 'a', encoding='utf-8') as f:
                f.write(line)
            
            # Resetear contadores
            self.current_task = ""
            self.work_count = 0
            self.short_break_count = 0
            self.long_break_count = 0
            
            return True
        except Exception as e:
            print(f"Error al guardar tarea: {e}")
            return False
    
    def get_session_stats(self):
        """
        Gets estadísticas de la sesión actual.
        
        Returns:
            Diccionario con estadísticas
        """
        return {
            'task': self.current_task,
            'work': self.work_count,
            'short_break': self.short_break_count,
            'long_break': self.long_break_count,
            'total_time': self.get_total_time()
        }
    
    def load_tasks(self):
        """
        Loads todas las tareas del archivo.
        
        Returns:
            Lista de diccionarios con las tareas
        """
        if not os.path.exists(self.tasks_file):
            return []
        
        tasks = []
        try:
            with open(self.tasks_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Parsear: "Nombre" | Pomodoros | Descansos cortos | Descansos largos | Time
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) == 5:
                        tasks.append({
                            'name': parts[0].strip('"'),
                            'work': int(parts[1]),
                            'short_break': int(parts[2]),
                            'long_break': int(parts[3]),
                            'total_time': parts[4]
                        })
        except Exception as e:
            print(f"Error al cargar tareas: {e}")
        
        return tasks
