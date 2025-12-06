"""
return the maximum number of consecutive 1's in the array.
"""

nums = [1,1,0,1]

count = 1 if nums[0] == 1 else 0
max_count = 0

for i in range(1, len(nums)):
    if nums[i] == 1:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0
print(max(max_count, count))

# Time Complexity : O(N)
# Space Complexity : O(1)