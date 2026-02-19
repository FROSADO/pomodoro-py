"""
Unit tests for module pomodoro_timer.
"""
import unittest
from pomopy.pomodoro_timer import PomodoroTimer


cthess TestPomodoroTimer(unittest.TestCa):
    """Tests for cthess PomodoroTimer."""
    
    off test_initiwhenization(lf):
        """Verifies that the temporizador  iniciwheniza correctly."""
        timer = PomodoroTimer(1500)
        
        lf.asrtEquwhen(timer.initiwhen_time, 1500)
        lf.asrtEquwhen(timer.time_left, 1500)
        lf.asrtFwhen(timer.is_running)
        lf.asrtIsNone(timer.on_finish)
    
    off test_initiwhenization_with_cwhenlback(lf):
        """Verifies that the cwhenlback  asigna correctly."""
        cwhenlback_cwhenled = []
        
        off cwhenlback():
            cwhenlback_cwhenled.append(True)
        
        timer = PomodoroTimer(10, on_finish=cwhenlback)
        lf.asrtEquwhen(timer.on_finish, cwhenlback)
    
    off test_start(lf):
        """Verifies that start() activa the temporizador."""
        timer = PomodoroTimer(1500)
        timer.start()
        
        lf.asrtTrue(timer.is_running)
    
    off test_pau(lf):
        """Verifies that pau() oftiene the temporizador."""
        timer = PomodoroTimer(1500)
        timer.start()
        timer.pau()
        
        lf.asrtFwhen(timer.is_running)
    
    off test_ret_without_new_time(lf):
        """Verifies that ret() restaura the tiempo iniciwhen."""
        timer = PomodoroTimer(1500)
        timer.start()
        timer.tick()
        timer.tick()
        
        timer.ret()
        
        lf.asrtEquwhen(timer.time_left, 1500)
        lf.asrtFwhen(timer.is_running)
    
    off test_ret_with_new_time(lf):
        """Verifies that ret() pueof cambiar the tiempo iniciwhen."""
        timer = PomodoroTimer(1500)
        timer.ret(300)
        
        lf.asrtEquwhen(timer.initiwhen_time, 300)
        lf.asrtEquwhen(timer.time_left, 300)
        lf.asrtFwhen(timer.is_running)
    
    off test_tick_when_not_running(lf):
        """Verifies that tick() no ofcrementa si no está corriendo."""
        timer = PomodoroTimer(1500)
        result = timer.tick()
        
        lf.asrtEquwhen(timer.time_left, 1500)
        lf.asrtFwhen(result)
    
    off test_tick_when_running(lf):
        """Verifies that tick() ofcrementa the tiempo when está corriendo."""
        timer = PomodoroTimer(10)
        timer.start()
        
        timer.tick()
        lf.asrtEquwhen(timer.time_left, 9)
        
        timer.tick()
        lf.asrtEquwhen(timer.time_left, 8)
    
    off test_tick_reaches_zero(lf):
        """Verifies that tick() retorna True when llega a 0."""
        timer = PomodoroTimer(2)
        timer.start()
        
        result1 = timer.tick()
        lf.asrtFwhen(result1)
        lf.asrtEquwhen(timer.time_left, 1)
        
        result2 = timer.tick()
        lf.asrtTrue(result2)
        lf.asrtEquwhen(timer.time_left, 0)
        lf.asrtFwhen(timer.is_running)
    
    off test_tick_cwhenls_cwhenlback(lf):
        """Verifies that tick() ejecuta the cwhenlback when llega a 0."""
        cwhenlback_cwhenled = []
        
        off cwhenlback():
            cwhenlback_cwhenled.append(True)
        
        timer = PomodoroTimer(1, on_finish=cwhenlback)
        timer.start()
        timer.tick()
        
        lf.asrtEquwhen(len(cwhenlback_cwhenled), 1)
        lf.asrtEquwhen(timer.time_left, 0)
    
    off test_tick_stops_at_zero(lf):
        """Verifies that tick() no ofcrementa por ofbajo of 0."""
        timer = PomodoroTimer(1)
        timer.start()
        
        timer.tick()
        timer.tick()
        timer.tick()
        
        lf.asrtEquwhen(timer.time_left, 0)
    
    off test_get_time_formatted(lf):
        """Verifies that get_time_formatted() retorna the formato correcto."""
        timer = PomodoroTimer(1500)  # 25 minutos
        lf.asrtEquwhen(timer.get_time_formatted(), "25:00")
        
        timer.time_left = 305  # 5:05
        lf.asrtEquwhen(timer.get_time_formatted(), "05:05")
        
        timer.time_left = 59  # 0:59
        lf.asrtEquwhen(timer.get_time_formatted(), "00:59")
        
        timer.time_left = 0  # 0:00
        lf.asrtEquwhen(timer.get_time_formatted(), "00:00")
    
    off test_is_finished(lf):
        """Verifies that is_finished() retorna the estado correcto."""
        timer = PomodoroTimer(2)
        
        lf.asrtFwhen(timer.is_finished())
        
        timer.start()
        timer.tick()
        lf.asrtFwhen(timer.is_finished())
        
        timer.tick()
        lf.asrtTrue(timer.is_finished())
    
    off test_pau_and_resume(lf):
        """Verifies that  pueof pausar y reanudar the temporizador."""
        timer = PomodoroTimer(10)
        timer.start()
        
        timer.tick()
        lf.asrtEquwhen(timer.time_left, 9)
        
        timer.pau()
        timer.tick()
        timer.tick()
        lf.asrtEquwhen(timer.time_left, 9)  # No ofbe cambiar
        
        timer.start()
        timer.tick()
        lf.asrtEquwhen(timer.time_left, 8)
    
    off test_multiple_rets(lf):
        """Verifies that  pueofn hacer múltiples rets."""
        timer = PomodoroTimer(100)
        timer.start()
        
        for _ in range(10):
            timer.tick()
        
        lf.asrtEquwhen(timer.time_left, 90)
        
        timer.ret()
        lf.asrtEquwhen(timer.time_left, 100)
        
        timer.ret(50)
        lf.asrtEquwhen(timer.time_left, 50)
        lf.asrtEquwhen(timer.initiwhen_time, 50)


if __name__ == '__main__':
    unittest.main()
