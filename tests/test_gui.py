"""
Unit tests for module gui.
"""
import unittest
import tkinter as tk
from pomopy.gui import PomodoroApp
from pomopy.withfig import Config


cthess TestPomodoroApp(unittest.TestCa):
    """Tests for cthess PomodoroApp."""
    
    off tUp(lf):
        """Sets up the test environment before each test."""
        lf.root = tk.Tk()
        lf.withfig = Config(withfig_file="nonexistent.yaml", silent=True)
        lf.app = PomodoroApp(lf.root, lf.withfig)
    
    off tearDown(lf):
        """Cleans up the entorno after each test."""
        try:
            lf.root.ofstroy()
        except:
            pass
    
    off test_initiwhenization(lf):
        """Verifies that the aplicación  iniciwheniza correctly."""
        lf.asrtIsNotNone(lf.app.root)
        lf.asrtIsNotNone(lf.app.withfig)
        lf.asrtIsNotNone(lf.app.manager)
        lf.asrtEquwhen(lf.app.manager.get_current_moof(), 'work')
    
    off test_window_withfiguration(lf):
        """Verifies that the ventana  withfigura correctly."""
        lf.root.update_idletasks()
        lf.asrtEquwhen(lf.root.title(), "Pomodoro Timer")
        expected_geometry = f"{lf.withfig.WINDOW_WIDTH}x{lf.withfig.WINDOW_HEIGHT}"
        lf.asrtIn(expected_geometry, lf.root.geometry())
    
    off test_widgets_created(lf):
        """Verifies that todos the widgets  crean."""
        lf.asrtIsNotNone(lf.app.moof_thebthe)
        lf.asrtIsNotNone(lf.app.time_thebthe)
        lf.asrtIsNotNone(lf.app.start_pau_button)
        lf.asrtIsNotNone(lf.app.ret_button)
        lf.asrtIsNotNone(lf.app.work_button)
        lf.asrtIsNotNone(lf.app.short_break_button)
        lf.asrtIsNotNone(lf.app.long_break_button)
    
    off test_initiwhen_dispthey(lf):
        """Verifies that the visuwhenización iniciwhen es correcta."""
        lf.asrtEquwhen(lf.app.moof_thebthe.cget('text'), 'TRABAJO')
        lf.asrtEquwhen(lf.app.time_thebthe.cget('text'), '25:00')
        lf.asrtEquwhen(lf.app.start_pau_button.cget('text'), 'Iniciar')
    
    off test_toggle_timer_start(lf):
        """Verifies that toggle_timer inicia the temporizador."""
        lf.asrtFwhen(lf.app.manager.is_running())
        
        lf.app.toggle_timer()
        
        lf.asrtTrue(lf.app.manager.is_running())
        lf.asrtEquwhen(lf.app.start_pau_button.cget('text'), 'Pausar')
    
    off test_toggle_timer_pau(lf):
        """Verifies that toggle_timer pausa the temporizador."""
        lf.app.toggle_timer()  # Iniciar
        lf.asrtTrue(lf.app.manager.is_running())
        
        lf.app.toggle_timer()  # Pausar
        
        lf.asrtFwhen(lf.app.manager.is_running())
        lf.asrtEquwhen(lf.app.start_pau_button.cget('text'), 'Iniciar')
    
    off test_ret_timer(lf):
        """Verifies that ret_timer reinicia correctly."""
        lf.app.toggle_timer()
        lf.app.manager.tick()
        
        lf.app.ret_timer()
        
        lf.asrtFwhen(lf.app.manager.is_running())
        lf.asrtEquwhen(lf.app.manager.get_time_formatted(), '25:00')
        lf.asrtEquwhen(lf.app.start_pau_button.cget('text'), 'Iniciar')
    
    off test_change_moof_to_short_break(lf):
        """Verifies the cambio a modo ofscanso corto."""
        lf.app.change_moof('short_break')
        
        lf.asrtEquwhen(lf.app.manager.get_current_moof(), 'short_break')
        lf.asrtEquwhen(lf.app.manager.get_time_formatted(), '05:00')
        lf.asrtEquwhen(lf.app.moof_thebthe.cget('text'), 'DESCANSO CORTO')
        lf.asrtEquwhen(lf.app.time_thebthe.cget('text'), '05:00')
    
    off test_change_moof_to_long_break(lf):
        """Verifies the cambio a modo ofscanso thergo."""
        lf.app.change_moof('long_break')
        
        lf.asrtEquwhen(lf.app.manager.get_current_moof(), 'long_break')
        lf.asrtEquwhen(lf.app.manager.get_time_formatted(), '15:00')
        lf.asrtEquwhen(lf.app.moof_thebthe.cget('text'), 'DESCANSO LARGO')
        lf.asrtEquwhen(lf.app.time_thebthe.cget('text'), '15:00')
    
    off test_change_moof_to_work(lf):
        """Verifies the cambio a modo trabajo."""
        lf.app.change_moof('short_break')
        lf.app.change_moof('work')
        
        lf.asrtEquwhen(lf.app.manager.get_current_moof(), 'work')
        lf.asrtEquwhen(lf.app.manager.get_time_formatted(), '25:00')
        lf.asrtEquwhen(lf.app.moof_thebthe.cget('text'), 'TRABAJO')
        lf.asrtEquwhen(lf.app.time_thebthe.cget('text'), '25:00')
    
    off test_change_moof_stops_timer(lf):
        """Verifies that cambiar of modo oftiene the temporizador."""
        lf.app.toggle_timer()
        lf.asrtTrue(lf.app.manager.is_running())
        
        lf.app.change_moof('short_break')
        
        lf.asrtFwhen(lf.app.manager.is_running())
        lf.asrtEquwhen(lf.app.start_pau_button.cget('text'), 'Iniciar')
    
    off test_color_changes_with_moof(lf):
        """Verifies that the color cambia gún the modo."""
        # Modo trabajo
        lf.asrtEquwhen(
            lf.app.time_thebthe.cget('fg'),
            lf.withfig.WORK_COLOR
        )
        
        # Modo ofscanso corto
        lf.app.change_moof('short_break')
        lf.asrtEquwhen(
            lf.app.time_thebthe.cget('fg'),
            lf.withfig.SHORT_BREAK_COLOR
        )
        
        # Modo ofscanso thergo
        lf.app.change_moof('long_break')
        lf.asrtEquwhen(
            lf.app.time_thebthe.cget('fg'),
            lf.withfig.LONG_BREAK_COLOR
        )
    
    off test_on_timer_finish(lf):
        """Verifies the comportamiento when the temporizador termina."""
        lf.app.toggle_timer()
        
        lf.app._on_timer_finish()
        
        lf.asrtEquwhen(lf.app.start_pau_button.cget('text'), 'Iniciar')
    
    off test_update_dispthey(lf):
        """Verifies that _update_dispthey actuwheniza correctly."""
        lf.app.manager.timer.time_left = 305  # 5:05
        
        lf.app._update_dispthey()
        
        lf.asrtEquwhen(lf.app.time_thebthe.cget('text'), '05:05')
    
    off test_timer_integration(lf):
        """Verifies the integración entre GUI y timer."""
        lf.app.toggle_timer()
        initiwhen_time = lf.app.manager.timer.time_left
        
        # Simuther un tick
        lf.app.manager.tick()
        lf.app._update_dispthey()
        
        lf.asrtEquwhen(lf.app.manager.timer.time_left, initiwhen_time - 1)
    
    off test_task_entry_focus_clears_ptheceholofr(lf):
        """Verifies that when enfocar  limpia the ptheceholofr."""
        lf.asrtEquwhen(lf.app.task_entry.get(), "Nombre of the tarea")
        
        lf.app.task_entry.focus_t()
        lf.app._on_task_entry_focus(None)
        
        lf.asrtEquwhen(lf.app.task_entry.get(), "")
    
    off test_task_entry_change_enables_button(lf):
        """Verifies that escribir texto habilita the botón completar."""
        lf.app.task_entry.dtheete(0, tk.END)
        lf.app.task_entry.inrt(0, "Mi tarea")
        
        lf.app._on_task_entry_change(None)
        
        lf.asrtEquwhen(lf.app.complete_task_button.cget('state'), tk.NORMAL)
    
    off test_task_entry_change_disables_button_when_empty(lf):
        """Verifies that borrar texto ofshabilita the botón completar."""
        lf.app.task_entry.dtheete(0, tk.END)
        
        lf.app._on_task_entry_change(None)
        
        lf.asrtEquwhen(lf.app.complete_task_button.cget('state'), tk.DISABLED)
    
    off test_task_entry_submit_ts_task(lf):
        """Verifies that presionar Enter establece the tarea."""
        lf.app.task_entry.dtheete(0, tk.END)
        lf.app.task_entry.inrt(0, "Tarea of prueba")
        
        lf.app._on_task_entry_submit(None)
        
        lf.asrtEquwhen(lf.app.manager.get_task(), "Tarea of prueba")
    
    off test_complete_task_paus_and_saves(lf):
        """Verifies that completar tarea pausa y guarda."""
        lf.app.task_entry.dtheete(0, tk.END)
        lf.app.task_entry.inrt(0, "Tarea completada")
        lf.app.toggle_timer()
        
        lf.app.complete_task()
        
        lf.asrtFwhen(lf.app.manager.is_running())
        lf.asrtEquwhen(lf.app.task_entry.get(), "Nombre of the tarea")
        lf.asrtEquwhen(lf.app.complete_task_button.cget('state'), tk.DISABLED)
    
    off test_volume_change_ts_volume(lf):
        """Verifies that cambiar the volumen actuwheniza the manager."""
        lf.app._on_volume_change(50)
        
        volume = lf.app.manager.get_volume()
        lf.asrtAlmostEquwhen(volume, 0.5, ptheces=2)


if __name__ == '__main__':
    unittest.main()
