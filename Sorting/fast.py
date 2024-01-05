def quick_sort(arr):
    """
    Best: NlogN
    Median: NlogN
    Worst: N^2
    """
    if len(arr) < 2:
        return arr
    center = len(arr) // 2
    pivot = arr[center]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def merge_sort(arr):
    pass
