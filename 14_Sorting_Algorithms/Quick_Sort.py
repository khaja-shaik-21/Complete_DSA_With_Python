# Quick Sort Algorithm
# Type 1:
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        return quickSort(left) + [pivot] + quickSort(right)


Data = [3, 2, 8, 1, 5]

print(f"Before Sorting : {Data}")
print(f"After Sorting : {quickSort(Data)}")


# Type 2:
def partition(nums, low, high):
    pivot = nums[low]
    i = low + 1
    j = high

    while True:
        # Move i right
        while i <= high and nums[i] <= pivot:
            i += 1

        # Move j left
        while j >= low and nums[j] > pivot:
            j -= 1

        # If pointers cross, break
        if i >= j:
            break

        # Swap
        nums[i], nums[j] = nums[j], nums[i]

    # Place pivot in correct position
    nums[low], nums[j] = nums[j], nums[low]
    return j


def quickSort(nums, low, high):
    if low < high:
        p_idx = partition(nums, low, high)
        quickSort(nums, low, p_idx - 1)
        quickSort(nums, p_idx + 1, high)

        
Data = [3, 2, 8, 1, 5]
n = len(Data)
print(f"Before Sorting : {Data}")
quickSort(Data, 0, n - 1)
print(f"After Sorting : {Data}")

    

#############   Time & Space Complexity Table: QuickSort Algorithm  ############

# | Case       | Time Complexity | Space Complexity | Notes                                                         |
# | ---------- | --------------- | ---------------- | ------------------------------------------------------------- |
# | Best Case  | O(n log n)      | O(log n)         | Balanced partition; divide evenly                             |
# | Average    | O(n log n)      | O(log n)         | Good pivot selection maintains balance                        |
# | Worst Case | O(n²)           | O(n)             | Happens when pivot is smallest/largest; unbalanced partitions |
