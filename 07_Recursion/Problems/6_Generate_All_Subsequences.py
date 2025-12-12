"""
Generate All Subsequences of a array elements
"""
def solve(idx, subset, ):
    if idx >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[idx])
    solve(idx + 1, subset)
    subset.pop()
    solve(idx + 1, subset)
  

nums = [5, 7, 9]
idx = 0
result = []
subset = []
ans = solve(idx, subset, )
print(result)


# Time Complexity : O(2^N)
# Space Complexity : o(N)