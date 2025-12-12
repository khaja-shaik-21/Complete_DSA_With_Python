"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
"""
# Method 1: Bruite Force
def Min(nums):
    Min = float("inf")
    for i in range(len(nums)):
        if nums[i] < Min:
            Min = nums[i]
    return Min

nums = [3,4,5,1,2]
ans = Min(nums)
print(ans)

# Time Complexity : O(N)
# Space Complexity : O(1)



# Method 2: Binary Search
def minSorted(nums):
    n = len(nums)
    low = 0
    high = n - 1
    Min = float("inf")
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] <= nums[high]:
            Min = min(nums[mid], Min)
            high = mid - 1
        else:
            Min = min(nums[low], Min)
            low = mid + 1
    return Min


nums = [3,4,5,1,2]
ans = minSorted(nums)
print(ans)

# Time Complexity : O(logN)
# Space Complexity : O(1)