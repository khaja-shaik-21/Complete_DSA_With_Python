# Bucket Sort Algorithm using Insertion Sort Algorithm

import math

def insertionSort(CustomList):
    for i in range(1, len(CustomList)):
        key = CustomList[i]
        j = i - 1
        while j >= 0 and key < CustomList[j]:
            CustomList[j+1] = CustomList[j]
            j -= 1
        CustomList[j+1] = key
    return CustomList


def bucketSort(CustomList):
    numberOfBuckets = round(math.sqrt(len(CustomList)))
    maxValue = max(CustomList)
    arr = []
    
    for i in range(numberOfBuckets):
        arr.append([])
    
    for j in CustomList:
        index_b = math.ceil(j * numberOfBuckets / maxValue)
        arr[index_b - 1].append(j)
    
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            CustomList[k] = arr[i][j]
            k += 1
    return CustomList

# Bucket Sort with Negative Numbers
def bucketSortNegative(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    rangeVal = (maxValue - minValue) / numberofBuckets
 
    buckets = [[] for _ in range(numberofBuckets)]
 
    for j in customList:
        if j == maxValue:
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - minValue) / rangeVal)
            buckets[index_b].append(j)
    
    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i] = insertionSort(buckets[i])
        sorted_array.extend(buckets[i])
    
    return sorted_array

Data = [3, 2, 8, 1, 5]

print(f"Before Sorting : {Data}")
print(f"After Sorting : {bucketSort(Data)}")


Data = [-3, -2, 8, -1, 5]

print(f"Before Sorting : {Data}")
print(f"After Sorting : {bucketSortNegative(Data)}")


#############   Time & Space Complexity Table: Bucket Sort Algorithm using Insertion Sort Algorithm  ############

# | Case       | Time Complexity | Space Complexity | Notes                                                                 |
# | ---------- | --------------- | ---------------- | --------------------------------------------------------------------- |
# | Best Case  | O(n + k)        | O(n + k)         | Uniform distribution; few elements per bucket; insertion sort is O(n) |
# | Average    | O(n + n²/k + k) | O(n + k)         | k = number of buckets (≈ √n); depends on distribution inside buckets  |
# | Worst Case | O(n²)           | O(n + k)         | All elements go into one bucket → insertion sort becomes O(n²)        |
