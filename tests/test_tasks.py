"""
Unit tests for module tasks.
"""
import unittest
import os
import tempfile
import shutil
from pomopy.tasks import TaskManager


class TestTaskManager(unittest.TestCase):
    """Tests for class TaskManager."""
    
    def setUp(self):
        """Sets up the test environment."""
        self.temp_dir = tempfile.mkdtemp()
        self.manager = TaskManager(tasks_folder=self.temp_dir)
    
    def tearDown(self):
        """Cleans up the entorno after each test."""
        try:
            shutil.rmtree(self.temp_dir)
        except:
            pass
    
    def test_initialization(self):
        """Verifies that the gestor inicializa correctly."""
        self.assertEqual(self.manager.tasks_folder, self.temp_dir)
        self.assertEqual(self.manager.current_task, "")
        self.assertEqual(self.manager.work_count, 0)
        self.assertEqual(self.manager.short_break_count, 0)
        self.assertEqual(self.manager.long_break_count, 0)
        self.assertEqual(self.manager.meeting_time, 0)
        self.assertEqual(self.manager.work_time, 1500)
        self.assertEqual(self.manager.short_break_time, 300)
        self.assertEqual(self.manager.long_break_time, 900)
    
    def test_set_task(self):
        """Verifies that puede establecer una tarea."""
        self.manager.set_task("Estudiar Python")
        
        self.assertEqual(self.manager.current_task, "Estudiar Python")
    
    def test_set_task_strips_whitespace(self):
        """Verifies that eliminan espacios en blanco."""
        self.manager.set_task("  Tarea con espacios  ")
        
        self.assertEqual(self.manager.current_task, "Tarea con espacios")
    
    def test_get_task(self):
        """Verifies that puede obtener la tarea actual."""
        self.manager.set_task("Mi tarea")
        
        self.assertEqual(self.manager.get_task(), "Mi tarea")
    
    def test_increment_work(self):
        """Verifies that incrementa el contador de trabajo."""
        self.manager.increment_work()
        self.manager.increment_work()
        
        self.assertEqual(self.manager.work_count, 2)
    
    def test_increment_work_without_task(self):
        """Verifies that incrementa incluso sin tarea activa."""
        self.manager.increment_work()
        
        self.assertEqual(self.manager.work_count, 1)
    
    def test_increment_short_break(self):
        """Verifies that incrementa el contador de descansos cortos."""
        self.manager.increment_short_break()
        
        self.assertEqual(self.manager.short_break_count, 1)
    
    def test_increment_long_break(self):
        """Verifies that incrementa el contador de descansos largos."""
        self.manager.increment_long_break()
        
        self.assertEqual(self.manager.long_break_count, 1)
    
    def test_get_total_time_without_start(self):
        """Verifies el tiempo total sin contadores."""
        time = self.manager.get_total_time()
        
        self.assertEqual(time, "00:00:00")
    
    def test_get_total_time_format(self):
        """Verifies el formato del tiempo total."""
        self.manager.set_task("Tarea")
        time = self.manager.get_total_time()
        
        # Debe tener formato HH:mm:ss
        parts = time.split(':')
        self.assertEqual(len(parts), 3)
        self.assertTrue(all(len(p) == 2 for p in parts))
    
    def test_complete_task_without_task(self):
        """Verifies que no completa sin tarea."""
        result = self.manager.complete_task()
        
        self.assertFalse(result)
    
    def test_complete_task_saves_to_file(self):
        """Verifies que guarda la tarea en el archivo."""
        self.manager.set_task("Tarea de prueba")
        self.manager.increment_work()
        self.manager.increment_work()
        self.manager.increment_short_break()
        
        result = self.manager.complete_task()
        
        self.assertTrue(result)
        daily_file = self.manager._get_daily_file()
        self.assertTrue(os.path.exists(daily_file))
        
        with open(daily_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn("Tarea de prueba", content)
            self.assertIn("| 2 |", content)
            self.assertIn("| 1 |", content)
    
    def test_complete_task_resets_counters(self):
        """Verifies que resetea los contadores al completar."""
        self.manager.set_task("Tarea")
        self.manager.increment_work()
        self.manager.complete_task()
        
        self.assertEqual(self.manager.current_task, "")
        self.assertEqual(self.manager.work_count, 0)
        self.assertEqual(self.manager.short_break_count, 0)
        self.assertEqual(self.manager.long_break_count, 0)
        self.assertEqual(self.manager.meeting_time, 0)
    
    def test_get_session_stats(self):
        """Verifies que obtienen las estadísticas correctly."""
        self.manager.set_task("Mi tarea")
        self.manager.increment_work()
        self.manager.increment_short_break()
        
        stats = self.manager.get_session_stats()
        
        self.assertEqual(stats['task'], "Mi tarea")
        self.assertEqual(stats['work'], 1)
        self.assertEqual(stats['short_break'], 1)
        self.assertEqual(stats['long_break'], 0)
        self.assertIsNotNone(stats['total_time'])
        self.assertIsNotNone(stats['meeting_time'])
    
    def test_load_tasks_empty_file(self):
        """Verifies carga de archivo vacío."""
        tasks = self.manager.load_tasks()
        
        self.assertEqual(tasks, [])
    
    def test_load_tasks_with_data(self):
        """Verifies carga de tareas from file."""
        # Guardar una tarea
        self.manager.set_task("Tarea 1")
        self.manager.increment_work()
        self.manager.complete_task()
        
        # Cargar tareas
        tasks = self.manager.load_tasks()
        
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['name'], "Tarea 1")
        self.assertEqual(tasks[0]['work'], 1)
    
    def test_multiple_tasks(self):
        """Verifies múltiples tareas."""
        # Primera tarea
        self.manager.set_task("Tarea 1")
        self.manager.increment_work()
        self.manager.complete_task()
        
        # Segunda tarea
        self.manager.set_task("Tarea 2")
        self.manager.increment_work()
        self.manager.increment_work()
        self.manager.complete_task()
        
        tasks = self.manager.load_tasks()
        
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['name'], "Tarea 1")
        self.assertEqual(tasks[1]['name'], "Tarea 2")
        self.assertEqual(tasks[1]['work'], 2)
    
    def test_increment_meeting_time(self):
        """Verifies incremento de tiempo de reunión."""
        self.manager.increment_meeting_time(3600)
        self.assertEqual(self.manager.meeting_time, 3600)
        self.assertEqual(self.manager.get_meeting_time(), "01:00:00")
    
    def test_save_meeting(self):
        """Verifies guardado de reunión."""
        self.manager.increment_meeting_time(1800)
        result = self.manager.save_meeting()
        
        self.assertTrue(result)
        self.assertEqual(self.manager.meeting_time, 0)
        
        tasks = self.manager.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['name'], "REUNION")
        self.assertEqual(tasks[0]['meeting_time'], "00:30:00")
    
    def test_save_meeting_without_time(self):
        """Verifies que no guarda reunión sin tiempo."""
        result = self.manager.save_meeting()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
