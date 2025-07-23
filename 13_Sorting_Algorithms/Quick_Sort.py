# Quick Sort Algorithm

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


#############   Time & Space Complexity Table: QuickSort Algorithm  ############

# | Case       | Time Complexity | Space Complexity | Notes                                                         |
# | ---------- | --------------- | ---------------- | ------------------------------------------------------------- |
# | Best Case  | O(n log n)      | O(log n)         | Balanced partition; divide evenly                             |
# | Average    | O(n log n)      | O(log n)         | Good pivot selection maintains balance                        |
# | Worst Case | O(n²)           | O(n)             | Happens when pivot is smallest/largest; unbalanced partitions |
