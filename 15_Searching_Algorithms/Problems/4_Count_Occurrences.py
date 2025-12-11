"""
Given a sorted array, arr[] and a number target, 
you need to find the number of occurrences of target in arr[]. 
"""
# Method 1: Bruite Force
def count(nums, target):
    n = len(nums)
    first = -1
    last = -1
    for i in range(n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    if first == -1: return 0
    return last - first + 1 

arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
ans = count(arr, target)
print(ans)


# Method 2: Lower and Upper bound
def lower(nums, target):
    n = len(nums)
    lb = -1
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            lb = mid
            right = mid - 1
        else:
            left = mid + 1
    return lb


def upper(nums, target):
    n = len(nums)
    ub = n
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            ub = mid
            right = mid - 1
        else:
            left = mid + 1
    return ub


def countFreq(arr, target):
    lb = lower(arr, target)

    # Check if target exists
    if lb == -1 or arr[lb] != target:
        return 0

    ub = upper(arr, target)

    return ub - lb

nums = [1, 1, 2, 2, 2, 2, 3]
target = 2
ans = countFreq(nums, target)
print(ans)