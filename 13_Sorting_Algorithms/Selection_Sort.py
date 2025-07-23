# Selection Sort Algorithm

def selectionSort(CustomList):
    for i in range(len(CustomList)):
        min_index = i
        for j in range(i+1, len(CustomList)):
            if CustomList[min_index] > CustomList[j]:
                min_index = j
        CustomList[i], CustomList[min_index] = CustomList[min_index], CustomList[i]
    return CustomList

Data = [3, 2, 8, 1, 5]

print(f"Before Sorting : {Data}")
print(f"After Sorting : {selectionSort(Data)}")

#############   Time & Space Complexity Table: Selection Sort Algorithm  ############

# | Case       | Time Complexity | Space Complexity | Notes                                  |
# | ---------- | --------------- | ---------------- | -------------------------------------- |
# | Best Case  | O(n²)           | O(1)             | Even if sorted, comparisons happen     |
# | Average    | O(n²)           | O(1)             | In-place, stable only with extra steps |
# | Worst Case | O(n²)           | O(1)             | Worst when reverse sorted              |
