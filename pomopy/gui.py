"""
Module de interfaz gráfica para la aplicación Pomodoro Timer.
"""
import tkinter as tk
from tkinter import font
from pomopy.config import Config
from pomopy.pomodoro_manager import PomodoroManager


class PomodoroApp:
    """Class que gestiona la interfaz gráfica de la aplicación Pomodoro."""
    
    def __init__(self, root, config=None):
        """
        Initializes la aplicación.
        
        Args:
            root: Window raíz de Tkinter
            config: Instancia de Config (opcional)
        """
        self.root = root
        self.config = config or Config()
        self.manager = PomodoroManager(self.config)
        self.manager.set_finish_callback(self._on_timer_finish)
        self.meeting_active = False
        
        self._setup_window()
        self._create_widgets()
        self._update_display()
    
    def _setup_window(self):
        """Configura la ventana principal."""
        self.root.title("Pomodoro Timer")
        self.root.geometry(f"{self.config.WINDOW_WIDTH}x{self.config.WINDOW_HEIGHT + 50}")
        self.root.configure(bg=self.config.BG_COLOR)
        self.root.resizable(False, False)
        
        if self.config.ALWAYS_ON_TOP:
            self.root.attributes('-topmost', True)
    
    def _create_widgets(self):
        """Crea todos los widgets de la interfaz."""
        # Label del modo actual
        self.mode_label = tk.Label(
            self.root,
            text="TRABAJO",
            font=font.Font(size=16, weight='bold'),
            bg=self.config.BG_COLOR,
            fg=self.config.TEXT_COLOR
        )
        self.mode_label.pack(pady=(20, 10))
        
        # Label del tiempo
        self.time_label = tk.Label(
            self.root,
            text="25:00",
            font=font.Font(size=48, weight='bold'),
            bg=self.config.BG_COLOR,
            fg=self.config.get_color_for_mode(self.manager.get_current_mode())
        )
        self.time_label.pack(pady=20)
        
        # Frame de botones de control
        control_frame = tk.Frame(self.root, bg=self.config.BG_COLOR)
        control_frame.pack(pady=10)
        
        self.start_pause_button = tk.Button(
            control_frame,
            text="Start",
            command=self.toggle_timer,
            width=10,
            font=font.Font(size=12)
        )
        self.start_pause_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(
            control_frame,
            text="Reset",
            command=self.reset_timer,
            width=10,
            font=font.Font(size=12)
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # Frame de tarea actual
        task_frame = tk.Frame(self.root, bg=self.config.BG_COLOR)
        task_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(
            task_frame,
            font=font.Font(size=10),
            width=25,
            justify='center'
        )
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.insert(0, "Task name")
        self.task_entry.bind('<FocusIn>', self._on_task_entry_focus)
        self.task_entry.bind('<Return>', self._on_task_entry_submit)
        self.task_entry.bind('<KeyRelease>', self._on_task_entry_change)
        
        self.complete_task_button = tk.Button(
            task_frame,
            text="✓ Complete",
            command=self.complete_task,
            width=10,
            font=font.Font(size=9),
            state=tk.DISABLED
        )
        self.complete_task_button.pack(side=tk.LEFT, padx=5)
        
        # Frame de estadísticas
        stats_frame = tk.Frame(self.root, bg=self.config.BG_COLOR)
        stats_frame.pack(pady=5)
        
        # Labels de estadísticas en dos columnas
        left_stats = tk.Frame(stats_frame, bg=self.config.BG_COLOR)
        left_stats.pack(side=tk.LEFT, padx=10)
        
        right_stats = tk.Frame(stats_frame, bg=self.config.BG_COLOR)
        right_stats.pack(side=tk.LEFT, padx=10)
        
        # Columna izquierda
        self.work_count_label = tk.Label(
            left_stats,
            text="Pomodoros: 0",
            font=font.Font(size=9),
            bg=self.config.BG_COLOR,
            fg=self.config.TEXT_COLOR
        )
        self.work_count_label.pack(anchor='w')
        
        self.short_break_label = tk.Label(
            left_stats,
            text="Short breaks: 0",
            font=font.Font(size=9),
            bg=self.config.BG_COLOR,
            fg=self.config.TEXT_COLOR
        )
        self.short_break_label.pack(anchor='w')
        
        self.long_break_label = tk.Label(
            left_stats,
            text="Long breaks: 0",
            font=font.Font(size=9),
            bg=self.config.BG_COLOR,
            fg=self.config.TEXT_COLOR
        )
        self.long_break_label.pack(anchor='w')
        
        # Columna derecha
        self.work_time_label = tk.Label(
            right_stats,
            text="Work time: 00:00",
            font=font.Font(size=9),
            bg=self.config.BG_COLOR,
            fg=self.config.TEXT_COLOR
        )
        self.work_time_label.pack(anchor='w')
        
        self.break_time_label = tk.Label(
            right_stats,
            text="Break time: 00:00",
            font=font.Font(size=9),
            bg=self.config.BG_COLOR,
            fg=self.config.TEXT_COLOR
        )
        self.break_time_label.pack(anchor='w')
        
        # Frame de botones de modo
        mode_frame = tk.Frame(self.root, bg=self.config.BG_COLOR)
        mode_frame.pack(pady=20)
        
        self.work_button = tk.Button(
            mode_frame,
            text="Work",
            command=lambda: self.change_mode('work'),
            width=12,
            height=2,
            font=font.Font(size=9)
        )
        self.work_button.pack(side=tk.LEFT, padx=5)
        
        self.short_break_button = tk.Button(
            mode_frame,
            text="Short Break",
            command=lambda: self.change_mode('short_break'),
            width=12,
            height=2,
            font=font.Font(size=9)
        )
        self.short_break_button.pack(side=tk.LEFT, padx=5)
        
        self.long_break_button = tk.Button(
            mode_frame,
            text="Long Break",
            command=lambda: self.change_mode('long_break'),
            width=12,
            height=2,
            font=font.Font(size=9)
        )
        self.long_break_button.pack(side=tk.LEFT, padx=5)
        
        # Botón de reunión
        meeting_frame = tk.Frame(self.root, bg=self.config.BG_COLOR)
        meeting_frame.pack(pady=10)
        
        self.meeting_button = tk.Button(
            meeting_frame,
            text="MEETING",
            command=self.toggle_meeting,
            width=38,
            height=2,
            font=font.Font(size=10, weight='bold'),
            bg=self.config.MEETING_COLOR,
            fg="#000000"
        )
        self.meeting_button.pack()
        
        # Label de tiempo de reunión
        self.meeting_time_label = tk.Label(
            self.root,
            text="Meeting time: 00:00:00",
            font=font.Font(size=9),
            bg=self.config.BG_COLOR,
            fg=self.config.TEXT_COLOR
        )
        self.meeting_time_label.pack(pady=5)
        
        # Control de volumen
        volume_frame = tk.Frame(self.root, bg=self.config.BG_COLOR)
        volume_frame.pack(pady=10)
        
        volume_label = tk.Label(
            volume_frame,
            text="Volume:",
            font=font.Font(size=9),
            bg=self.config.BG_COLOR,
            fg=self.config.TEXT_COLOR
        )
        volume_label.pack(side=tk.LEFT, padx=5)
        
        self.volume_scale = tk.Scale(
            volume_frame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            command=self._on_volume_change,
            length=200,
            showvalue=True
        )
        self.volume_scale.set(int(self.manager.get_volume() * 100))
        self.volume_scale.pack(side=tk.LEFT, padx=5)
    
    def toggle_timer(self):
        """Alterna entre iniciar y pausar el temporizador."""
        if self.manager.is_running():
            self.manager.pause_timer()
            self.start_pause_button.config(text="Start")
        else:
            self.manager.start_timer()
            self.start_pause_button.config(text="Pause")
            self._tick()
    
    def reset_timer(self):
        """Resets el temporizador al tiempo inicial del modo actual."""
        self.manager.reset_timer()
        self.start_pause_button.config(text="Start")
        self._update_display()
    
    def change_mode(self, mode):
        """
        Changes el modo del temporizador.
        
        Args:
            mode: 'work', 'short_break' o 'long_break'
        """
        self.manager.change_mode(mode)
        self.start_pause_button.config(text="Start")
        self._update_display()
    
    def _on_timer_finish(self):
        """Callback ejecutado cuando el temporizador termina."""
        self.start_pause_button.config(text="Start")
        self._update_stats()
        
        # Reproducir sonido del sistema como fallback
        if self.config.SOUND_ENABLED:
            self.root.bell()
    
    def _tick(self):
        """Decrements el tiempo y programa el siguiente tick."""
        if self.manager.is_running():
            self.manager.tick()
            self._update_display()
            self.root.after(1000, self._tick)
    
    def _update_display(self):
        """Updates la visualización del tiempo y modo."""
        self.time_label.config(
            text=self.manager.get_time_formatted(),
            fg=self.config.get_color_for_mode(self.manager.get_current_mode())
        )
        
        mode_names = {
            'work': 'WORK',
            'short_break': 'SHORT BREAK',
            'long_break': 'LONG BREAK'
        }
        self.mode_label.config(text=mode_names.get(self.manager.get_current_mode(), 'WORK'))
    
    def _on_task_entry_focus(self, event):
        """Limpia el placeholder al enfocar."""
        if self.task_entry.get() == "Task name":
            self.task_entry.delete(0, tk.END)
    
    def _on_task_entry_change(self, event):
        """Updates el estado del botón al cambiar el texto."""
        task_name = self.task_entry.get().strip()
        if task_name and task_name != "Task name":
            self.complete_task_button.config(state=tk.NORMAL)
        else:
            self.complete_task_button.config(state=tk.DISABLED)
    
    def _on_task_entry_submit(self, event):
        """Sets la tarea al presionar Enter."""
        task_name = self.task_entry.get().strip()
        if task_name and task_name != "Task name":
            self.manager.set_task(task_name)
            self._update_stats()
    
    def complete_task(self):
        """Completes la tarea actual."""
        task_name = self.task_entry.get().strip()
        if task_name and task_name != "Task name":
            # Solo establecer tarea si no hay una ya establecida
            if not self.manager.get_task():
                self.manager.set_task(task_name)
            self.manager.pause_timer()
            self.start_pause_button.config(text="Start")
            self.manager.complete_task()
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, "Task name")
            self.complete_task_button.config(state=tk.DISABLED)
            self._update_stats()
    
    def toggle_meeting(self):
        """Alterna el modo de reunión."""
        if self.meeting_active:
            # Finalizar reunión
            self.meeting_active = False
            self.meeting_button.config(text="MEETING")
            self.manager.save_meeting()
            self._update_stats()
        else:
            # Iniciar reunión
            self.meeting_active = True
            self.meeting_button.config(text="END MEETING")
            self._meeting_tick()
    
    def _meeting_tick(self):
        """Incrementa el tiempo de reunión cada segundo."""
        if self.meeting_active:
            self.manager.increment_meeting_time(1)
            self._update_stats()
            self.root.after(1000, self._meeting_tick)
    
    def _update_stats(self):
        """Updates las estadísticas mostradas."""
        stats = self.manager.get_stats()
        self.work_count_label.config(text=f"Pomodoros: {stats['work']}")
        self.short_break_label.config(text=f"Short breaks: {stats['short_break']}")
        self.long_break_label.config(text=f"Long breaks: {stats['long_break']}")
        self.work_time_label.config(text=f"Work time: {self.manager.get_total_work_time()}")
        self.break_time_label.config(text=f"Break time: {self.manager.get_total_break_time()}")
        self.meeting_time_label.config(text=f"Meeting time: {self.manager.get_meeting_time()}")
    
    def _on_volume_change(self, value):
        """Callback cuando cambia el volumen."""
        self.manager.set_volume(int(value) / 100.0)
    
    def run(self):
        """Starts el loop principal de la aplicación."""
        self.root.mainloop()
