"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
"""
# Method 1: Bruite Force
def bruitForce(nums, target):
    n = len(nums)
    left = -1
    right = -1
    for i in range(n):
        if nums[i] == target:
            if left == -1:
                left = i
            right = i
    return [left, right]

# Time Complexity : O(n)
# Space Complexity : O(1)


# Method 2:
class Solution:
    def searchRange(self, nums, target):
        
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]




# Method 3: lower and upper bound
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
    ub = -1
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            ub = mid
            right = mid - 1
        else:
            left = mid + 1
    return ub


def countOccurance(arr, target):
    lb = lower(arr, target)

    # Check if target exists
    if lb == -1 or arr[lb] != target:
        return [-1, -1]

    ub = upper(arr, target)

    return [lb, ub - 1]

nums = [5,7,7,8,8,10]
target = 8
ans = countOccurance(nums, target)
print(ans)


nums = [5,7,7,8,8,10]
target = 6
ans = countOccurance(nums, target)
print(ans)

# Time Complexity : O(logn)+O(logn) = O(logn)
# Space Complexity : O(1)