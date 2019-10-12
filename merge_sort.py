#!/usr/bin/env python

import os
import sys


def merge(arr1, arr2):
    merged = []
    arr1_idx = 0
    arr2_idx = 0
    smaller_len = len(arr1) if len(arr1) < len(arr2) else len(arr2)

    while arr1_idx < smaller_len and arr2_idx < smaller_len:
        if arr1[arr1_idx] < arr2[arr2_idx]:
            merged.append(arr1[arr1_idx])
            arr1_idx += 1
        elif arr2[arr2_idx] < arr1[arr1_idx]:
            merged.append(arr2[arr2_idx])
            arr2_idx += 1

    if arr1_idx < len(arr1):
        merged += arr1[arr1_idx:]
    if arr2_idx < len(arr2):
        merged += arr2[arr2_idx:]

    return merged


def sort(arr):
    if len(arr) == 1:
        return arr

    half_length = len(arr) // 2
    left = sort(arr[:half_length])
    right = sort(arr[half_length:])

    return merge(left, right)


if __name__ == "__main__":
    print(sort([38, 27, 43, 3, 9, 82, 10]))
    print(sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
