"""
You're given a sorted array 'a' of 'n' integers and an integer 'x'.

Find the floor and ceiling of 'x' in 'a[0..n-1]'.

Note:
Floor of 'x' is the largest element in the array which is smaller than or equal to 'x'.
Ceiling of 'x' is the smallest element in the array greater than or equal to 'x'.
"""

def floorCeil(nums, target):
    n = len(nums)
    
    floor = -1
    ceil = -1
    
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        elif nums[mid] < target:
            floor = nums[mid]
            low = mid + 1
        else:
            ceil = nums[mid]
            high = mid - 1
    return[floor, ceil]



nums = [1, 3, 5, 6]
target = 5


ans = floorCeil(nums, target)
print(ans)


# Time Complexity : O(logN)
# Space Complexity : O(1)