import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task("TestTask", 5, 3)
        self.assertEqual(task.name, "TestTask")
        self.assertEqual(task.get_deadline(), 5)
        self.assertEqual(task.execution_time, 3)

def test_repr(self):
    task = Task("Sample", 10, 2)
    self.assertEqual(repr(task), "Task(name=Sample, deadline=10, exec=2s)")

if __name__ == "__main__":
    unittest.main()
