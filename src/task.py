from .schedulable import Schedulable

class Task(Schedulable):
    def __init__(self, name: str, deadline: int, execution_time: float):
        self.name = name
        self.deadline = deadline
        self.execution_time = execution_time  # in Sekunden

    def get_deadline(self) -> int:
        return self.deadline

    def get_execution_time(self) -> float:
        return self.execution_time

    def __repr__(self):
        return f"Task(name={self.name}, deadline={self.deadline}, exec={self.execution_time}s)"
