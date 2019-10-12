#!/usr/bin/env python3
'''
Solution to the "Find the Running Median" problem from hackerrank
https://www.hackerrank.com/challenges/find-the-running-median/problem

By Pedro F Linhares, October 12th, 2019.
'''

import random
import time
import numpy as np


class MinMaxHeap:
    def __init__(self, is_max=True):
        self._items = []
        self._is_max = is_max

    def __len__(self):
        return len(self._items)

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

    def __heapify_up(self, compare_method):
        idx = len(self._items) - 1
        parent_idx = self._get_parent_index(idx)

        while parent_idx is not None and compare_method(self._items[idx], self._items[parent_idx]):
            self._swap(idx, parent_idx)
            idx = parent_idx
            parent_idx = self._get_parent_index(idx)

    def _heapify_up(self):
        if self._is_max:
            self.__heapify_up(lambda a, b: a > b)
        else:
            self.__heapify_up(lambda a, b: a < b)

    def peek(self):
        return self._items[0]

    def enqueue(self, item):
        self._items.append(item)
        self._heapify_up()

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

    def _heapify_down(self):
        if self._is_max:
            self.__heapify_down(lambda a, b: a < b)
        else:
            self.__heapify_down(lambda a, b: a > b)

    def dequeue(self):
        head = self._items[0]
        self._items[0] = self._items[-1]
        self._items = self._items[:-1]
        self._heapify_down()
        return head


def median(min_heap, max_heap):
    if len(min_heap) == len(max_heap):
        return (min_heap.peek() + max_heap.peek()) / 2
    elif len(min_heap) > len(max_heap):
        return min_heap.peek()
    else:
        return max_heap.peek()


def runningMedian(input_arr):
    output = []
    last_median = None
    max_heap = MinMaxHeap()
    min_heap = MinMaxHeap(False)

    for i in range(len(input_arr)):
        if last_median is None or input_arr[i] > last_median:
            min_heap.enqueue(input_arr[i])
        else:
            max_heap.enqueue(input_arr[i])

        if len(min_heap) - len(max_heap) > 1:
            max_heap.enqueue(min_heap.dequeue())
        elif len(max_heap) - len(min_heap) > 1:
            min_heap.enqueue(max_heap.dequeue())

        med = float("{0:.1f}".format(median(min_heap, max_heap)))
        last_median = med
        output.append(med)

    return output


if __name__ == '__main__':
    random.seed(time.time())
    input_val = [random.randint(0, 10 ** 5)
                 for i in range(10 ** 5)]
    output = runningMedian(input_val)
    for i in range(len(output)):
        raw_input = input_val[:(i + 1)]
        np_median = np.median(raw_input)
        if output[i] != np_median:
            print(
                f"{i}: Failed expected: {np_median}, but got: {output[i]}")
            print(f"\tInput was: {raw_input}")
        else:
            print(f"{i}: Succeeded")
