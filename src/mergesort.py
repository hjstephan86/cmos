from typing import List
from .schedulable import Schedulable

class MergeSort:
    @staticmethod
    def sort(tasks: List[Schedulable]) -> List[Schedulable]:
        if len(tasks) <= 1:
            return tasks

        mid = len(tasks) // 2
        left = MergeSort.sort(tasks[:mid])
        right = MergeSort.sort(tasks[mid:])

        return MergeSort.merge(left, right)

    @staticmethod
    def merge(left: List[Schedulable], right: List[Schedulable]) -> List[Schedulable]:
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].get_deadline() <= right[j].get_deadline():
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list
