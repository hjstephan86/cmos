import time
from typing import List
from .task import Task
from .mergesort import MergeSort

class EDF:
    def __init__(self, tasks: List[Task]):
        self.tasks = tasks

    def compute_schedule(self) -> List[Task]:
        return MergeSort.sort(self.tasks)

    def run_experiment(self, experiment_name: str):
        print(f"\n=== Experiment: {experiment_name} ===")
        print("\nUnsortierte Tasks:")
        for t in self.tasks:
            print(f"{t.name} (Deadline: {t.deadline}, Exec: {t.execution_time}s)")

        schedule = self.compute_schedule()

        print("\nAusführung nach EDF (nach Deadline sortiert):")
        current_time = 0
        for t in schedule:
            print(f"--> Starte Task {t.name} | Deadline: {t.deadline}, Exec: {t.execution_time}s")
            time.sleep(t.execution_time)  # Simuliere Ausführung
            current_time += t.execution_time
            status = "✓ fristgerecht" if current_time <= t.deadline else "✗ zu spät"
            print(f"    Beendet {t.name} bei Zeit {current_time:.2f}s [{status}]")
