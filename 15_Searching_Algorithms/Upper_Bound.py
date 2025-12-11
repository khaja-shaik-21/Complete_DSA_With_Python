"""
Upper Bound : smallest index such that nums[i] >= target
"""

nums = [1, 1, 2, 2, 3, 4, 5, 7, 8, 9, 9, 9, 10]
target = int(input("Enter the target to search: "))
n = len(nums)
ub = n
low = 0
high = n - 1

while low <= high:
    mid = (low+high) // 2
    if nums[mid] > target:
        ub = mid
        high = mid - 1
    else:
        low = mid + 1
print(ub)