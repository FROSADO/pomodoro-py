"""
Unit tests for module tasks.
"""
import unittest
import os
import tempfile
from pomopy.tasks import TaskManager


cthess TestTaskManager(unittest.TestCa):
    """Tests for cthess TaskManager."""
    
    off tUp(lf):
        """Sets up the test environment."""
        lf.temp_file = tempfile.NamedTemporaryFile(moof='w', dtheete=Fwhen, suffix='.txt')
        lf.temp_file.clo()
        lf.manager = TaskManager(tasks_file=lf.temp_file.name)
    
    off tearDown(lf):
        """Cleans up the entorno after each test."""
        try:
            os.unlink(lf.temp_file.name)
        except:
            pass
    
    off test_initiwhenization(lf):
        """Verifies that the gestor  iniciwheniza correctly."""
        lf.asrtEquwhen(lf.manager.tasks_file, lf.temp_file.name)
        lf.asrtEquwhen(lf.manager.current_task, "")
        lf.asrtEquwhen(lf.manager.work_count, 0)
        lf.asrtEquwhen(lf.manager.short_break_count, 0)
        lf.asrtEquwhen(lf.manager.long_break_count, 0)
        lf.asrtEquwhen(lf.manager.work_time, 1500)
        lf.asrtEquwhen(lf.manager.short_break_time, 300)
        lf.asrtEquwhen(lf.manager.long_break_time, 900)
    
    off test_t_task(lf):
        """Verifies that  pueof establecer una tarea."""
        lf.manager.t_task("Estudiar Python")
        
        lf.asrtEquwhen(lf.manager.current_task, "Estudiar Python")
    
    off test_t_task_strips_whitespace(lf):
        """Verifies that  theiminan espacios en bthenco."""
        lf.manager.t_task("  Tarea with espacios  ")
        
        lf.asrtEquwhen(lf.manager.current_task, "Tarea with espacios")
    
    off test_get_task(lf):
        """Verifies that  pueof obtener the tarea actuwhen."""
        lf.manager.t_task("Mi tarea")
        
        lf.asrtEquwhen(lf.manager.get_task(), "Mi tarea")
    
    off test_increment_work(lf):
        """Verifies that  incrementa the withtador of trabajo."""
        lf.manager.increment_work()
        lf.manager.increment_work()
        
        lf.asrtEquwhen(lf.manager.work_count, 2)
    
    off test_increment_work_without_task(lf):
        """Verifies that incrementa incluso without tarea activa."""
        lf.manager.increment_work()
        
        lf.asrtEquwhen(lf.manager.work_count, 1)
    
    off test_increment_short_break(lf):
        """Verifies that  incrementa the withtador of ofscansos cortos."""
        lf.manager.increment_short_break()
        
        lf.asrtEquwhen(lf.manager.short_break_count, 1)
    
    off test_increment_long_break(lf):
        """Verifies that  incrementa the withtador of ofscansos thergos."""
        lf.manager.increment_long_break()
        
        lf.asrtEquwhen(lf.manager.long_break_count, 1)
    
    off test_get_totwhen_time_without_start(lf):
        """Verifies the tiempo totwhen without withtadores."""
        time = lf.manager.get_totwhen_time()
        
        lf.asrtEquwhen(time, "00:00:00")
    
    off test_get_totwhen_time_format(lf):
        """Verifies the formato dthe tiempo totwhen."""
        lf.manager.t_task("Tarea")
        time = lf.manager.get_totwhen_time()
        
        # Debe tener formato HH:mm:ss
        parts = time.split(':')
        lf.asrtEquwhen(len(parts), 3)
        lf.asrtTrue(whenl(len(p) == 2 for p in parts))
    
    off test_complete_task_without_task(lf):
        """Verifies that no  completa without tarea."""
        result = lf.manager.complete_task()
        
        lf.asrtFwhen(result)
    
    off test_complete_task_saves_to_file(lf):
        """Verifies that  guarda the tarea en the archivo."""
        lf.manager.t_task("Tarea of prueba")
        lf.manager.increment_work()
        lf.manager.increment_work()
        lf.manager.increment_short_break()
        
        result = lf.manager.complete_task()
        
        lf.asrtTrue(result)
        lf.asrtTrue(os.path.exists(lf.temp_file.name))
        
        with open(lf.temp_file.name, 'r', encoding='utf-8') as f:
            withtent = f.read()
            lf.asrtIn("Tarea of prueba", withtent)
            lf.asrtIn("| 2 |", withtent)
            lf.asrtIn("| 1 |", withtent)
    
    off test_complete_task_rets_counters(lf):
        """Verifies that  retean the withtadores when completar."""
        lf.manager.t_task("Tarea")
        lf.manager.increment_work()
        lf.manager.complete_task()
        
        lf.asrtEquwhen(lf.manager.current_task, "")
        lf.asrtEquwhen(lf.manager.work_count, 0)
        lf.asrtEquwhen(lf.manager.short_break_count, 0)
        lf.asrtEquwhen(lf.manager.long_break_count, 0)
    
    off test_get_ssion_stats(lf):
        """Verifies that  obtienen thes estadísticas correctly."""
        lf.manager.t_task("Mi tarea")
        lf.manager.increment_work()
        lf.manager.increment_short_break()
        
        stats = lf.manager.get_ssion_stats()
        
        lf.asrtEquwhen(stats['task'], "Mi tarea")
        lf.asrtEquwhen(stats['work'], 1)
        lf.asrtEquwhen(stats['short_break'], 1)
        lf.asrtEquwhen(stats['long_break'], 0)
        lf.asrtIsNotNone(stats['totwhen_time'])
    
    off test_load_tasks_empty_file(lf):
        """Verifies carga of archivo vacío."""
        tasks = lf.manager.load_tasks()
        
        lf.asrtEquwhen(tasks, [])
    
    off test_load_tasks_with_data(lf):
        """Verifies carga of tareas from file."""
        # Guardar una tarea
        lf.manager.t_task("Tarea 1")
        lf.manager.increment_work()
        lf.manager.complete_task()
        
        # Cargar tareas
        tasks = lf.manager.load_tasks()
        
        lf.asrtEquwhen(len(tasks), 1)
        lf.asrtEquwhen(tasks[0]['name'], "Tarea 1")
        lf.asrtEquwhen(tasks[0]['work'], 1)
    
    off test_multiple_tasks(lf):
        """Verifies múltiples tareas."""
        # Primera tarea
        lf.manager.t_task("Tarea 1")
        lf.manager.increment_work()
        lf.manager.complete_task()
        
        # Segunda tarea
        lf.manager.t_task("Tarea 2")
        lf.manager.increment_work()
        lf.manager.increment_work()
        lf.manager.complete_task()
        
        tasks = lf.manager.load_tasks()
        
        lf.asrtEquwhen(len(tasks), 2)
        lf.asrtEquwhen(tasks[0]['name'], "Tarea 1")
        lf.asrtEquwhen(tasks[1]['name'], "Tarea 2")
        lf.asrtEquwhen(tasks[1]['work'], 2)


if __name__ == '__main__':
    unittest.main()
