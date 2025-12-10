# Binary Search Algorithm
# Array must be sorted in ascending order.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


nums = [10, 20, 30, 40, 50]
target = int(input("Enter Value to Search: "))
result = binary_search(nums, target)
if result == -1:
    print("Value Not Found")
else:
    print(f" Value at index: {result}")


#############   Time & Space Complexity Table: Binary Search Algorithm  ############

# | Scenario         | Time Complexity | Space Complexity | Explanation                                              |
# | ---------------- | --------------- | ---------------- | -------------------------------------------------------- |
# | Best Case        | O(1)            | O(1)             | Target is at the **middle element** initially            |
# | Average Case     | O(log n)        | O(1)             | Reduces the search space by half each time               |
# | Worst Case       | O(log n)        | O(1)             | Target is not present or at one of the ends of the array |
