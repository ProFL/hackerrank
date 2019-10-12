#!/usr/bin/env python3
import random


class MinMaxHeap:
    def __init__(self, is_max=True):
        self._items = []
        self._is_max = is_max

    def __len__(self):
        return len(self._items)

    def __heapify_up(self, compare_method):
        idx = len(self._items) - 1
        parent_idx = self._get_parent_index(idx)

        while parent_idx is not None and compare_method(self._items[idx], self._items[parent_idx]):
            self._swap(idx, parent_idx)
            idx = parent_idx
            parent_idx = self._get_parent_index(idx)

    def __heapify_down(self, compare_method):
        idx = 0
        left = self._get_left_child_index(idx)
        right = self._get_right_child_index(idx)

        while left is not None:
            child_to_use_idx = left
            if right is not None and compare_method(self._items[child_to_use_idx], self._items[right]):
                child_to_use_idx = right
            self._swap(idx, child_to_use_idx)
            idx = child_to_use_idx

            left = self._get_left_child_index(idx)
            right = self._get_right_child_index(idx)

    def _swap(self, idxA, idxB):
        aux = self._items[idxA]
        self._items[idxA] = self._items[idxB]
        self._items[idxB] = aux

    def _get_parent_index(self, idx):
        parent_idx = (idx - 1) // 2
        if parent_idx < 0:
            return None
        return parent_idx

    def _get_left_child_index(self, idx):
        left_idx = idx * 2 + 1
        if left_idx >= len(self._items):
            return None
        return left_idx

    def _get_right_child_index(self, idx):
        right_idx = idx * 2 + 2
        if right_idx >= len(self._items):
            return None
        return right_idx

    def _heapify_up(self):
        if self._is_max:
            self.__heapify_up(lambda a, b: a > b)
        else:
            self.__heapify_up(lambda a, b: a < b)

    def _heapify_down(self):
        if self._is_max:
            self.__heapify_down(lambda a, b: a < b)
        else:
            self.__heapify_down(lambda a, b: a > b)

    def peek(self):
        return self._items[0]

    def enqueue(self, item):
        self._items.append(item)
        self._heapify_up()

    def dequeue(self):
        head = self._items[0]
        self._items[0] = self._items[-1]
        self._items = self._items[:-1]
        self._heapify_down()
        return head

    def show(self):
        print(self._items)

        print(self._items[0])
        total_print_count = 1
        cur_line_count = 2

        while total_print_count < len(self._items):
            to_print = []
            while len(to_print) < cur_line_count and total_print_count < len(self._items):
                to_print.append(self._items[total_print_count])
                total_print_count += 1
            print(' '.join(map(str, to_print)))
            cur_line_count *= 2
        print()


if __name__ == "__main__":
    print('MinHeap tests')
    min_heap = MinMaxHeap()
    for i in range(7):
        min_heap.enqueue(random.randint(0, 100))
    min_heap.show()
    removed = min_heap.dequeue()
    print(f"Removed: {removed}, now queue is:")
    min_heap.show()
    removed = min_heap.dequeue()
    print(f"Removed: {removed}, now queue is:")
    min_heap.show()

    print()
    print()

    print('MaxHeap tests')
    min_heap = MinMaxHeap(False)
    for i in range(7):
        min_heap.enqueue(random.randint(0, 100))
    min_heap.show()
    removed = min_heap.dequeue()
    print(f"Removed: {removed}, now queue is:")
    min_heap.show()
    removed = min_heap.dequeue()
    print(f"Removed: {removed}, now queue is:")
    min_heap.show()
