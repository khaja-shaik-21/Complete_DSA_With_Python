# Linear Search Algorithm

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


Data = [3, 2, 8, 1, 5]

target = int(input("Enter value to search: "))

result = linear_search(Data, target)

if result == -1:
    print("Value not Found")
else:
    print(f"Value at Index : {result}")



#############   Time & Space Complexity Table: Linear Search Algorithm  ############

# | Scenario.       | Time Complexity | Space Complexity | Explanation                                      |
# | --------------- | ----------- --- | ---------------- | ------------------------------------------------ |
# | Best Case       | O(1)            | O(1)             | Target is found at the **first element           |
# | Average Case    | O(n)            | O(1)             | Target is somewhere in the **middle              |
# | Worst Case      | O(n)            | O(1)             | Target is at the **end** or **not present at all |
