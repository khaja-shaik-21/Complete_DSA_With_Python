"""
Given an array arr and target sum k, 
check whether there exists a subsequence such that the sum of all elements in the subsequence 
equals the given target sum(k).

"""
def solve(idx, subset, tot):
    if tot == target:
        result.append(subset.copy())
        return
    elif tot > target:
        return

    if idx >= len(nums):
        return
     
    subset.append(nums[idx])
    tot = tot + nums[idx]
    solve(idx + 1, subset, tot)
    e = subset.pop()
    tot -= e
    solve(idx + 1, subset, tot)
  

nums = [5, 7, 9, 3, 6, 7, 2, 1]
target = 10
idx = 0
result = []
subset = []
sum = 0
ans = solve(idx, subset, sum)
print(result)

# Time Complexity : O(2^N)
# Space Complexity : o(N)