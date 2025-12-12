"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

nums = [1,2,3]

n = len(nums)

tot_subsets = 1 << n
result = []

for num in range(tot_subsets):
    lst = []
    for i in range(n):
        if num & (1 << i) != 0:
            lst.append(nums[i])
    result.append(lst)
print(result)

# Time Complexity : O(N * 2^N)
# Space Complexity : O(N * 2^N)