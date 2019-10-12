#!/usr/bin/env python
"""
Solution to the "Find the Running Median" problem from hackerrank
https://www.hackerrank.com/challenges/find-the-running-median/problem

Before noticing it was supposed to be solved with a heap, I attempted
to solve the problem by using [merge sort](./merge_sort.py) on each iteration and then
getting the median, and latter by using this sort on insertion based
on the binary search method.

As I believe the thought proccess was useful and well put, I decided to
keep the latter.

For the proper solution, see [running_median_heap.py](./running_median_heap.py)

By Pedro F Linhares, October 11th, 2019.
"""

import random
import time

import numpy as np


def fuzzy_binary_search(arr, val):
    if arr[0] > val:
        return -1
    elif arr[-1] < val:
        return len(arr)

    left = 0
    right = len(arr) - 1
    while left < right:
        search_point = (right + left) // 2

        if (arr[search_point] == val):
            return search_point
        elif (val > arr[search_point]):
            left = search_point + 1
        else:
            right = search_point - 1

    return left


def sorted_insert(arr, val):
    val_arr = [val]
    if len(arr) == 0:
        return val_arr

    pos = fuzzy_binary_search(arr, val)
    if type(pos) != int:
        print(arr, val, pos)

    if pos == -1:
        return val_arr + arr
    elif pos == len(arr):
        return arr + val_arr
    elif arr[pos] > val:
        return arr[:pos] + val_arr + arr[pos:]
    else:
        return arr[:pos + 1] + val_arr + arr[pos + 1:]


def median(arr):
    is_odd = len(arr) % 2 != 0
    if is_odd:
        return arr[len(arr) / 2]
    else:
        half_length = len(arr) / 2 - 1
        return (arr[half_length] + arr[half_length + 1]) / 2.0


def runningMedian(input_arr):
    output = []
    arr = []

    for i in range(len(input_arr)):
        arr = sorted_insert(arr, input_arr[i])
        med = float("{:.1f}".format(median(arr)))
        output.append(med)

    return output


if __name__ == "__main__":
    # output = runningMedian([38, 27, 43, 3, 9, 82, 10])
    random.seed(time.time())
    input_val = [random.randint(0, 10 ** 5)
                 for i in range(10 ** 4)]
    output = runningMedian(input_val)
    for i in range(len(output)):
        raw_input = input_val[:(i + 1)]
        np_median = np.median(raw_input)
        if output[i] != np_median:
            print("{}: Failed expected: {:.1f}, but got: {:.1f}".format(
                i + 1, np_median, output[i]))
            print("\tInput was: {}".format(raw_input))
        else:
            print("{}: Succeeded".format(i + 1))
