"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, 
nums is possibly left rotated at an unknown index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.
"""
# Method 1: Bruite Force
def bruite(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [4,5,6,7,0,1,2]
target = -1
ans = bruite(nums, target)
print(ans)


# Method 2: Binary Search
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


nums = [4,5,6,7,0,1,2]
target = 0

ans = search(nums, target)
print(ans)