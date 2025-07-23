# Bubble Sort Algorithm

def bubbleSort(CustomList):
    for i in range(len(CustomList) - 1):
        for j in range(len(CustomList)-i-1):
            if CustomList[j] > CustomList[j+1]:
                CustomList[j], CustomList[j+1] = CustomList[j+1], CustomList[j]
    return CustomList
    
    
Data = [3, 2, 8, 1, 5]

print(f"Before Sorting : {Data}")
print(f"After Sorting : {bubbleSort(Data)}")


#############   Time & Space Complexity Table: Bubble Sort Algorithm  ############

# | Case         | Time Complexity | Space Complexity | Notes                                                           |
# | ------------ | --------------- | ---------------- | --------------------------------------------------------------- |
# | Best Case    | O(n)            | O(1)             | When the list is already sorted (if optimized with a swap flag) |
# | Average Case | O(n²)           | O(1)             | Two nested loops, n iterations each (ignoring optimization)     |
# | Worst Case   | O(n²)           | O(1)             | When the list is in reverse order (maximum swaps required)      |
