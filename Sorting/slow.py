def buble_sort(arr):
    """
    Best: N
    Median: N^2
    Worst: N^2
    """
    size = len(arr) - 1
    for i in range(size):
        for j in range(size):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    """
    Best: N
    Median: N^2
    Worst: N^2
    """
    size = len(arr)
    for i in range(1, size):
        j = i - 1
        while arr[j] > arr[j+1] and j >= 0:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr


def selection_sort(arr):
    """
    Best: N^2
    Median: N^2
    Worst: N^2
    """
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
