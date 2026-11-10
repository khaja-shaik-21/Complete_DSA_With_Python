"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

"""
# Method 1: Brute Force
nums = [2,2,1,1,1,2,2]

for x in set(nums):
    if nums.count(x) > len(nums) // 2:
        print(x)
        
# Time Complexity : O(N^2)
# Space Complexity : O(1)



# Method 2: Boyer-Moore Voting Algorithm
candidate, count = None, 0
for num in nums:
    if count == 0:
        candidate = num
    count += 1 if candidate == num else -1

print(candidate)
# Time Complexity : O(N)
# Space Complexity : O(1)



# Method 3: Hash Map
from collections import Counter

counter = Counter(nums)
print(counter.most_common(1)[0][0])

# Time Complexity : O(N)
# Space Complexity : O(N)