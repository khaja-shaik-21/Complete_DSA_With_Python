# Merge Sort Algorithm

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Merge the two halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

Data = [3, 2, 8, 1, 5]

print(f"Before Sorting : {Data}")
print(f"After Sorting : {mergeSort(Data)}")



#############   Time & Space Complexity Table: Merge Sort Algorithm  ############

# | Case       | Time Complexity | Space Complexity | Notes                                       |
# | ---------- | --------------- | ---------------- | ------------------------------------------- |
# | Best Case  | O(n log n)      | O(n)             | Always divides input; merge step takes O(n) |
# | Average    | O(n log n)      | O(n)             | Consistent regardless of input distribution |
# | Worst Case | O(n log n)      | O(n)             | Merge always takes linear space and time    |
