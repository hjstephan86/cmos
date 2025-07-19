import unittest

from src.task import Task
from src.edf import EDF

class TestEDF(unittest.TestCase):
    def test_schedule_order(self):
        tasks = [
            Task("T1", 8, 1),
            Task("T2", 3, 1),
            Task("T3", 6, 1)
        ]
        scheduler = EDF(tasks)
        schedule = scheduler.compute_schedule()
        ordered_names = [t.name for t in schedule]
        self.assertEqual(ordered_names, ["T2", "T3", "T1"])

    def test_empty_schedule(self):
        scheduler = EDF([])
        schedule = scheduler.compute_schedule()
        self.assertEqual(schedule, [])

    def test_same_deadline(self):
        tasks = [
            Task("A", 4, 1),
            Task("B", 4, 1),
            Task("C", 4, 1)
        ]
        scheduler = EDF(tasks)
        schedule = scheduler.compute_schedule()
        deadlines = [t.get_deadline() for t in schedule]
        self.assertEqual(deadlines, [4, 4, 4])
        self.assertEqual(len(schedule), 3)

if __name__ == "__main__":
    unittest.main()
