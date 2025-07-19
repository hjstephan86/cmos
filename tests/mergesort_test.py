import unittest

from src.task import Task
from src.mergesort import MergeSort

class TestMergeSort(unittest.TestCase):
    def test_sorting_by_deadline(self):
        tasks = [
            Task("A", 7, 1),
            Task("B", 2, 1),
            Task("C", 5, 1)
        ]
        sorted_tasks = MergeSort.sort(tasks)
        deadlines = [t.get_deadline() for t in sorted_tasks]
        self.assertEqual(deadlines, [2, 5, 7])

    def test_empty_list(self):
        sorted_tasks = MergeSort.sort([])
        self.assertEqual(sorted_tasks, [])

    def test_single_element(self):
        task = Task("Single", 1, 1)
        sorted_tasks = MergeSort.sort([task])
        self.assertEqual(sorted_tasks, [task])

if __name__ == "__main__":
    unittest.main()
