# Merge Sort Algorithm
# Type 1
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


# Merge Sort Algorithm
# Type 2
def merge_arr(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)
    
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i >= n:
        while j<m:
            result.append(right[j])
            j += 1
    if j >= m:
        while i<n:
            result.append(left[i])
            i += 1
    return result

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = arr // 2
    L = arr[:mid]
    R = arr[mid:]   

    left = merge_sort(L, R)
    right = merge_sort(L, R)
    return merge_arr(left, right)
    
Data = [3, 2, 8, 1, 5]

print(f"Before Sorting : {Data}")
print(f"After Sorting : {mergeSort(Data)}")



#############   Time & Space Complexity Table: Merge Sort Algorithm  ############

# | Case       | Time Complexity | Space Complexity | Notes                                       |
# | ---------- | --------------- | ---------------- | ------------------------------------------- |
# | Best Case  | O(n log n)      | O(n)             | Always divides input; merge step takes O(n) |
# | Average    | O(n log n)      | O(n)             | Consistent regardless of input distribution |
# | Worst Case | O(n log n)      | O(n)             | Merge always takes linear space and time    |
