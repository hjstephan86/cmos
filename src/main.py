from .task import Task
from .edf import EDF

def main():
    # Experiment 1: Unterschiedliche Deadlines & Zeiten
    tasks1 = [
        Task("A", 10, 1.5),
        Task("B", 5, 2.0),
        Task("C", 7, 0.5),
        Task("D", 2, 1.0)
    ]
    edf1 = EDF(tasks1)
    edf1.run_experiment("Standard-Scheduling mit Execution Time")

    # Experiment 2: Gleiche Deadlines, unterschiedliche Laufzeiten
    tasks2 = [
        Task("T1", 4, 1.0),
        Task("T2", 4, 0.5),
        Task("T3", 4, 1.2)
    ]
    edf2 = EDF(tasks2)
    edf2.run_experiment("Gleiche Deadlines, verschiedene Ausführungszeiten")

    # Experiment 3: Enge Deadlines (Deadline-Miss möglich)
    tasks3 = [
        Task("X", 1, 1.0),
        Task("Y", 2, 1.5),
        Task("Z", 3, 1.0)
    ]
    edf3 = EDF(tasks3)
    edf3.run_experiment("Deadline-Miss Simulation")

if __name__ == "__main__":
    main()
