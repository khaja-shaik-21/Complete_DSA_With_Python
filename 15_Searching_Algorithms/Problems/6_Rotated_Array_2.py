"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, 
nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
"""
# Method 1: Bruite Force
def Rotate(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return True
    return False    
    
nums = [2,5,6,0,0,1,2]
target = 0
ans = Rotate(nums, target)
print(ans)
# Time Complexity : O(N)
# Space Complexity : O(1)

# Method 2: Optimal Solution
def SortRotated(nums, target):
    n = len(nums)
    
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return False

nums = [2,5,6,0,0,1,2]
target = 0
ans = SortRotated(nums, target)
print(ans)
# Time Complexity : Avg - O(logN), worst - O(N/2)
# Space Complexity : O(1)