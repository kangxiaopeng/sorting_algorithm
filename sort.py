# -*- coding=utf-8 -*-

import random


def bubbleSort(arr):
    """
    冒泡
    """
    size = len(arr)
    if size <= 1:
        return
    for i in range(size):
        sorted = True
        for k in range(size - i - 1):
            if arr[k] > arr[k + 1]:
                tmp = arr[k + 1]
                arr[k + 1] = arr[k]
                arr[k] = tmp
                sorted = False
        if sorted:
            break


def insertSort(arr):
    """
    插入
    """
    size = len(arr)
    if size <= 1:
        return
    for i in range(1, size):
        val = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > val:
                arr[j + 1] = arr[j]
                pos = j
            else:
                pos = j + 1
                break
        arr[pos] = val


def selectSort(arr):
    """
    选择
    """
    size = len(arr)
    if size <= 1:
        return
    for i in range(size):
        minIdx = -1
        minVal = 9999
        for j in range(i, size):
            if arr[j] < minVal:
                minVal = arr[j]
                minIdx = j
        tmp = arr[i]
        arr[i] = minVal
        arr[minIdx] = tmp


def portion(arr, start, end):
    """
    分区
    """
    pivot = arr[end]
    k = start
    for i in range(start, end):
        if arr[i] < pivot:
            tmp = arr[k]
            arr[k] = arr[i]
            arr[i] = tmp
            k += 1
    tmp = arr[k]
    arr[k] = pivot
    arr[end] = tmp
    return k


def quickSort(arr, start, end):
    """
    快排
    """
    if start >= end:
        return
    mid = portion(arr, start, end)
    quickSort(arr, start, mid - 1)
    quickSort(arr, mid + 1, end)


def merge(arr, start, mid, end):
    """
    合并
    """
    tmp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    if i < mid:
        tmp.extend(arr[i:mid + 1])
    if j < end:
        tmp.extend(arr[j:end + 1])

    for i in range(len(tmp)):
        arr[start + i] = tmp[i]


def mergeSort(arr, start, end):
    """
    归并
    """
    if start >= end:
        return
    mid = (start + end) / 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid + 1, end)
    merge(arr, start, mid, end)


def findK(arr, start, end, k):
    """
    O(n)找有序后的第k个元素（从1开始）
    """
    idx = portion(arr, start, end)
    if idx + 1 == k:
        return arr[idx]
    elif idx + 1 < k:
        return findK(arr, idx + 1, end, k)
    else:
        return findK(arr, start, idx - 1, k)


if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(random.randint(1, 10))

    print arr
    # bubbleSort(arr)
    # insertSort(arr)
    # selectSort(arr)
    # quickSort(arr, 0, len(arr) - 1)
    # mergeSort(arr, 0, len(arr) - 1)
    print findK(arr, 0, len(arr) - 1, 3)
    print arr



