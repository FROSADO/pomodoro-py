"""
Module de interfaz gráfica Flet para la aplicación Pomodoro Timer.
Reemplaza la GUI Tkinter con componentes Material Design 3.
"""
import asyncio
import flet as ft
from pomopy.config import Config
from pomopy.pomodoro_manager import PomodoroManager
from pomopy.components.timer_display import TimerDisplay
from pomopy.components.control_buttons import ControlButtons
from pomopy.components.mode_selector import ModeSelector
from pomopy.components.task_input import TaskInput
from pomopy.components.stats_panel import StatsPanel


class PomodoroApp:
    """Class que gestiona la interfaz gráfica Flet de la aplicación Pomodoro."""

    def __init__(self, page, config=None):
        """
        Initializes la aplicación Flet.

        Args:
            page: Instancia de ft.Page proporcionada por Flet.
            config: Instancia de Config (opcional).
        """
        self.page = page
        self.config = config or Config()
        self.manager = PomodoroManager(self.config)
        self.manager.set_finish_callback(self._on_timer_finish)
        self.meeting_active = False
        self._tick_running = False

        self._setup_page()
        self._create_components()
        self._build_layout()

    def _setup_page(self):
        """Configura la página Flet: título, dimensiones y tema."""
        self.page.title = "Pomodoro Timer"
        self.page.window.width = self.config.WINDOW_WIDTH
        self.page.window.height = self.config.WINDOW_HEIGHT
        self.page.window.resizable = self.config.WINDOW_RESIZABLE
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.config.THEME_MODE == "dark"
            else ft.ThemeMode.LIGHT
        )
        self.page.theme = ft.Theme(color_scheme_seed=self.config.COLOR_SEED)

    def _create_components(self):
        """Crea los 5 componentes Flet, switch de tema y slider de volumen."""
        self.timer_display = TimerDisplay()
        self.control_buttons = ControlButtons(
            on_start_pause=self.toggle_timer,
            on_reset=self.reset_timer,
        )
        self.mode_selector = ModeSelector(on_mode_change=self.change_mode)
        self.task_input = TaskInput(on_complete=self.complete_task)
        self.stats_panel = StatsPanel()

        self.theme_switch = ft.Switch(
            label="Dark mode",
            value=self.config.THEME_MODE == "dark",
            on_change=self._toggle_theme,
        )
        self.volume_slider = ft.Slider(
            min=0,
            max=100,
            value=self.manager.get_volume() * 100,
            label="Volume: {value}%",
            on_change=self._on_volume_change,
            width=250,
        )
        self.meeting_button = ft.Button(
            content=ft.Text("MEETING"),
            icon=ft.Icons.GROUPS,
            on_click=self.toggle_meeting,
            style=ft.ButtonStyle(
                bgcolor=self.config.MEETING_COLOR,
                color="#000000",
            ),
            width=300,
        )
        self.meeting_time_text = ft.Text(
            value=f"Meeting time: {self.manager.get_meeting_time()}",
            size=12,
        )
        self.snack_bar = ft.SnackBar(content=ft.Text(""))
        self.page.overlay.append(self.snack_bar)

    def _build_layout(self):
        """Construye el layout vertical con todos los componentes."""
        self.page.add(
            ft.Column(
                controls=[
                    ft.Container(
                        content=self.timer_display.build(),
                        alignment=ft.Alignment(0, 0),
                        padding=20,
                    ),
                    ft.Container(
                        content=self.control_buttons.build(),
                        alignment=ft.Alignment(0, 0),
                    ),
                    ft.Container(
                        content=self.mode_selector.build(),
                        alignment=ft.Alignment(0, 0),
                        padding=ft.Padding(top=10, bottom=0, left=0, right=0),
                    ),
                    ft.Divider(),
                    ft.Container(
                        content=self.task_input.build(),
                        alignment=ft.Alignment(0, 0),
                        padding=ft.Padding(top=5, bottom=5, left=0, right=0),
                    ),
                    ft.Divider(),
                    ft.Container(
                        content=self.stats_panel.build(),
                        alignment=ft.Alignment(0, 0),
                        padding=ft.Padding(top=5, bottom=5, left=0, right=0),
                    ),
                    ft.Divider(),
                    ft.Container(
                        content=self.meeting_button,
                        alignment=ft.Alignment(0, 0),
                    ),
                    self.meeting_time_text,
                    ft.Divider(),
                    ft.Row(
                        controls=[self.theme_switch],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls=[ft.Text("Volume:"), self.volume_slider],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            )
        )
        # Inicializar display con tiempo actual
        self.timer_display.update_time(self.manager.get_time_formatted())
        self.timer_display.set_color(
            self.config.get_color_for_mode(self.manager.get_current_mode())
        )
        self.page.update()

    # --- Handlers (3.2) ---

    def toggle_timer(self, e):
        """Alterna entre iniciar y pausar el temporizador.

        Args:
            e: Evento de click de Flet.
        """
        if self.manager.is_running():
            self.manager.pause_timer()
            self._reset_start_button()
        else:
            self.manager.start_timer()
            self.control_buttons.is_running = True
            self.control_buttons._start_pause_button.content = ft.Text("Pause")
            self.control_buttons._start_pause_button.icon = ft.Icons.PAUSE
            if not self._tick_running:
                self._tick_running = True
                self.page.run_task(self._tick_loop)
        self.page.update()

    def reset_timer(self, e):
        """Resets el temporizador al tiempo inicial del modo actual.

        Args:
            e: Evento de click de Flet.
        """
        self.manager.reset_timer()
        self._tick_running = False
        self._reset_start_button()
        self._update_display()
        self.page.update()

    # --- Handler (3.3) ---

    def change_mode(self, mode):
        """Changes el modo del temporizador.

        Args:
            mode: 'work', 'short_break' o 'long_break'.
        """
        self.manager.change_mode(mode)
        self._tick_running = False
        self._reset_start_button()
        self._update_display()
        self.page.update()

    # --- Handler (3.4) ---

    def complete_task(self, task_name):
        """Completes la tarea actual y muestra confirmación.

        Args:
            task_name: Nombre de la tarea completada.
        """
        if not self.manager.get_task():
            self.manager.set_task(task_name)
        self.manager.pause_timer()
        self._tick_running = False
        self._reset_start_button()
        self.manager.complete_task()
        self._update_stats()
        self.snack_bar.content = ft.Text(f"Task completed: {task_name}")
        self.snack_bar.open = True
        self.page.update()

    # --- Handler (3.5) ---

    def toggle_meeting(self, e):
        """Alterna entre modo reunión y modo normal.

        Args:
            e: Evento de click de Flet.
        """
        if self.meeting_active:
            self.meeting_active = False
            self.meeting_button.content = ft.Text("MEETING")
            self.meeting_button.icon = ft.Icons.GROUPS
            self.meeting_button.style = ft.ButtonStyle(
                bgcolor=self.config.MEETING_COLOR, color="#000000"
            )
            self.manager.save_meeting()
            self._update_stats()
        else:
            self.meeting_active = True
            self.meeting_button.content = ft.Text("END MEETING")
            self.meeting_button.icon = ft.Icons.STOP
            self.meeting_button.style = ft.ButtonStyle(
                bgcolor=ft.Colors.RED, color="#FFFFFF"
            )
            self.page.run_task(self._meeting_tick_loop)
        self.page.update()

    # --- Tick loop (3.6) ---

    async def _tick_loop(self):
        """Loop asíncrono que decrementa el timer cada segundo."""
        while self._tick_running and self.manager.is_running():
            self.manager.tick()
            self._update_display()
            self.page.update()
            await asyncio.sleep(1)
        self._tick_running = False

    async def _meeting_tick_loop(self):
        """Loop asíncrono que incrementa el tiempo de reunión cada segundo."""
        while self.meeting_active:
            self.manager.increment_meeting_time(1)
            self.meeting_time_text.value = (
                f"Meeting time: {self.manager.get_meeting_time()}"
            )
            self.page.update()
            await asyncio.sleep(1)

    # --- Theme / Volume (3.7) ---

    def _toggle_theme(self, e):
        """Cambia el tema entre oscuro y claro.

        Args:
            e: Evento de cambio del Switch.
        """
        if self.theme_switch.value:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()

    def _on_volume_change(self, e):
        """Callback cuando cambia el slider de volumen.

        Args:
            e: Evento de cambio del Slider.
        """
        self.manager.set_volume(e.control.value / 100.0)

    # --- Helpers internos ---

    def _reset_start_button(self):
        """Resetea el botón Start/Pause al estado Start."""
        self.control_buttons.is_running = False
        self.control_buttons._start_pause_button.content = ft.Text("Start")
        self.control_buttons._start_pause_button.icon = ft.Icons.PLAY_ARROW

    def _update_display(self):
        """Updates el timer display con tiempo y progreso actuales."""
        self.timer_display.update_time(self.manager.get_time_formatted())
        mode = self.manager.get_current_mode()
        total = self.config.get_time_for_mode(mode)
        elapsed = total - self.manager.timer.time_left
        percentage = (elapsed / total * 100) if total > 0 else 0
        self.timer_display.update_progress(percentage)
        self.timer_display.set_color(self.config.get_color_for_mode(mode))

    def _update_stats(self):
        """Updates el panel de estadísticas."""
        stats = self.manager.get_stats()
        self.stats_panel.update_stats({
            'work': stats['work'],
            'short_break': stats['short_break'],
            'long_break': stats['long_break'],
            'work_time': self.manager.get_total_work_time(),
            'break_time': self.manager.get_total_break_time(),
            'meeting_time': self.manager.get_meeting_time(),
        })

    def _on_timer_finish(self):
        """Callback ejecutado cuando el temporizador termina."""
        self._tick_running = False
        self._reset_start_button()
        self._update_stats()
        self._update_display()
        self.page.update()


def main(page: ft.Page):
    """Punto de entrada Flet para la aplicación.

    Args:
        page: Instancia de ft.Page proporcionada por Flet.
    """
    config = Config()
    PomodoroApp(page, config)
