# Heap Sort Algorithm

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr


Data = [3, 2, 8, 1, 5]

print(f"Before Sorting : {Data}")
print(f"After Sorting : {heapSort(Data)}")


#############   Time & Space Complexity Table: Heap Sort Algorithm  ############


# | Case       | Time Complexity | Space Complexity | Notes                                        |
# | ---------- | --------------- | ---------------- | -------------------------------------------- |
# | Best Case  | O(n log n)      | O(1)             | Heap is built and sorted in-place            |
# | Average    | O(n log n)      | O(1)             | Always divides using heapify                 |
# | Worst Case | O(n log n)      | O(1)             | Guaranteed even if already sorted in reverse |
