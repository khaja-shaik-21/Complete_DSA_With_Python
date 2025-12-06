"""
return indices of the two numbers such that they add up to target.
"""
######### Method 1: #########
def Sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
nums = [2,7,11,15]
target = 9

print(Sum(nums, target))
# Time Complexity : O(N^2)
# Space Complexity : O(1)



######### Method 2: #########
def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        rem = target - num
        if rem in hash_map:
            return [hash_map[rem], i]                                                
        hash_map[num] = i
        
nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))

# Time Complexity : O(N)
# Space Complexity : O(N)