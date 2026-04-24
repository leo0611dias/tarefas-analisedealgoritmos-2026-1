import time
import random

"""
Performance benchmark comparing Insertion Sort and Python's native TimSort.
"""

SCALE = [1000, 5000, 10000, 20000, 50000]


def insertion_sort(arr):
    """Sorts a list of integers using insertion sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def run_sorting_benchmark():
    """Runs the performance test for each scale defined."""
    for n in SCALE:
        base_list = [random.randint(0, n * 10) for _ in range(n)]

        # TimSort (n log n)
        tim_list = base_list.copy()
        start = time.time()
        tim_list.sort()
        time_tim_sort = time.time() - start

        # Insertion Sort (O(n²))
        insertion_list = base_list.copy()
        start = time.time()
        insertion_sort(insertion_list)
        time_insertion_sort = time.time() - start

        print(f"n = {n:<5} | TimSort: {time_tim_sort:>10.6f}s | Insertion: {time_insertion_sort:>10.6f}s")
        print("-" * 40)


if __name__ == "__main__":
    run_sorting_benchmark()
