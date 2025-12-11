# Insertion Sort Algorithm

def insertionSort(CustomList):
    for i in range(1, len(CustomList)):
        key = CustomList[i]
        j = i - 1
        while j >= 0 and key < CustomList[j]:   # key > CustomList[j] for Descending Order
            CustomList[j+1] = CustomList[j]
            j -= 1
        CustomList[j+1] = key
    return CustomList

Data = [3, 2, 8, 1, 5]

print(f"Before Sorting : {Data}")
print(f"After Sorting : {insertionSort(Data)}")


#############   Time & Space Complexity Table: Insertion Sort Algorithm  ############

# | Case       | Time Complexity | Space Complexity | Notes                                            |
# | ---------- | --------------- | ---------------- | ------------------------------------------------ |
# | Best Case  | O(n)            | O(1)             | Already sorted; only comparisons, no shifting    |
# | Average    | O(n²)           | O(1)             | Each element compared with all previous ones     |
# | Worst Case | O(n²)           | O(1)             | Reverse sorted; max shifts and comparisons occur |
