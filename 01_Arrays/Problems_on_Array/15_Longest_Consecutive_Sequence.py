"""
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.
"""

######### Method 1: #########
nums = [1, 99, 101, 98, 2, 3, 5, 100, 1, 1]

n = len(nums)
max_count = 0

for i in range(n):
    num = nums[i]
    count = 1
    while num + 1 in nums:
        count += 1
        num += 1
    max_count = max(max_count, count)
print(max_count)

# Time Complexity : O(N^2)
# Space Complexity : O(1)




######### Method 2: #########

nums = [1, 99, 101, 98, 2, 3, 5, 100, 1, 1]

nums.sort()         # TC : Best Case O(n), Worst Case O(n log n)

n = len(nums)
last_smaller = float('-inf')
count = 1

longest = 0

for i in range(n):
    if nums[i] - 1 != last_smaller:
        last_smaller = nums[i]
        count = 1
    else:
        count += 1
        last_smaller = nums[i]
    longest = max(longest, count)

print(longest)

# Time Complexity : O(NlogN)
# Space Complexity : O(1)



######### Method 3: #########

nums = [1, 99, 101, 98, 2, 3, 5, 100, 1, 1]


new_nums = set(nums)
n = len(nums)

longest = 0

for num in new_nums:
    if num -1 not in new_nums:      # Hash set lookup → O(1)
        n = num
        count = 1
        while n+1 in new_nums:      # Even though it looks nested, it does not recheck the same numbers repeatedly.
            count += 1
            n += 1
        longest = max(longest, count)
print(longest)

# Time Complexity : O(N)
# Space Complexity : O(N)