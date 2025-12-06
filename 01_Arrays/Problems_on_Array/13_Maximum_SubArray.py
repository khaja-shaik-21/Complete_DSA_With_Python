"""
Find the Maximum SubArray from the given array
"""
######### Method 1: #########
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

n = len(nums)
maxi = float("-inf")
for i in range(n):
    total = 0
    for j in range(n):
        total = nums[i] + nums[j]
        if total > maxi:
            maxi = total
    total = 0

# Time Complexity : O(N^2)
# Space Complexity : O(1)

######### Method 2: Kadane Algorithm #########

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(nums)

maxi = float("-inf")
tot = 0
for i in range(n):
    tot = tot + nums[i]
    maxi = max(maxi, tot)    
    if tot < 0:
        tot = 0
print(maxi)
# Time Complexity : O(N)
# Space Complexity : O(1)