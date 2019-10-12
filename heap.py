#!/usr/bin/env python
import math
import random
import time


class MinMaxHeap:
    @staticmethod
    def get_max_nodes_for_height(height):
        return 2 ** (height + 1) - 1

    def __init__(self, is_max=True):
        self._items = []
        self._is_max = is_max

    def __len__(self):
        return len(self._items)

    # FIXME: Not pretty pretting a non-complete tree
    def __str__(self):
        output = []
        output.append("Heap: {}".format(self._items))
        height = self.get_height()
        output.append("Height: {}".format(height))
        max_nodes_for_height = MinMaxHeap.get_max_nodes_for_height(height)
        # output.append("Max nodes for given height: {}\n".format(
        #     max_nodes_for_height))

        total_print_count = 1
        cur_line_count = 2
        lines = [[self._items[0]]]
        while total_print_count < len(self._items):
            to_print = []
            while len(to_print) < cur_line_count and total_print_count < len(self._items):
                to_print.append(self._items[total_print_count])
                total_print_count += 1
            lines.append(to_print)
            cur_line_count *= 2
        # output.append("{}".format(lines))
        output.append('')

        # + 1 space + 2 brackets
        base_line_length = max_nodes_for_height * (1 + 2) - 1
        base_line = ''.join([' ' for i in range(base_line_length)])
        for i in range(len(lines)):
            str_to_print = list(base_line)

            # if i == len(lines) - 1:
            #     elem_spacing = base_line_length / max_nodes_for_height
            # else:
            elem_spacing = base_line_length / len(lines[i])

            idx = 0
            pos = 0
            while idx < len(lines[i]):
                str_to_print[pos] = '{'
                str_to_print[pos + 1] = '}'
                idx += 1
                pos += elem_spacing + 1

            last_pos = pos + 1 - elem_spacing
            post_space_count = len(str_to_print) - last_pos - 1
            if post_space_count > 0:
                str_to_print = [' ' for j in range(
                    post_space_count / 2)] + str_to_print[:-(post_space_count / 2)]
            joint = "".join(str_to_print)
            # output.append(i, lines[i], elem_spacing, post_space_count, joint)
            output.append(joint.format(*lines[i]))
        return "\n".join(output)

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

    def get_height(self):
        return int(math.ceil(math.log(len(self._items) + 1, 2) - 1))

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


if __name__ == "__main__":
    random.seed(time.time())
    max_gen_height = 4

    print("MaxHeap tests")
    max_heap = MinMaxHeap()
    for i in range(random.randint(1, 2 * (2 ** max_gen_height) - 1)):
        max_heap.enqueue(random.randint(0, 100))
    print(max_heap)
    print('\n')
    removed = max_heap.dequeue()
    print("Removed: {}, now queue is:".format(removed))
    print(max_heap)
    print('\n')
    removed = max_heap.dequeue()
    print("Removed: {}, now queue is:".format(removed))
    print(max_heap)
    print('\n')

    print("\n")
    print("\n")

    print("MinHeap tests")
    min_heap = MinMaxHeap(False)
    for i in range(random.randint(1, 2 * (2 ** max_gen_height) - 1)):
        min_heap.enqueue(random.randint(0, 100))
    print(min_heap)
    print('\n')
    removed = min_heap.dequeue()
    print("Removed: {}, now queue is:".format(removed))
    print(min_heap)
    print('\n')
    removed = min_heap.dequeue()
    print("Removed: {}, now queue is:".format(removed))
    print(min_heap)
    print('\n')
