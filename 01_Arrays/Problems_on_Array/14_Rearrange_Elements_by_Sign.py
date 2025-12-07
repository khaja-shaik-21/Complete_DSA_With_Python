"""
Rearrange Array Elements by Sign 
1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present in nums is preserved.
3. The rearranged array begins with a positive integer.
"""

######### Method 1: #########
nums = [3,1,-2,-5,2,-4]


pos = []
neg = []
for i in nums:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)

for i in range(len(pos)):
    nums[2*i] = pos[i]
    nums[(2*i) + 1] = neg[i]
print(nums)

# Time Complexity : ~O(N)
# Space Complexity : O(N)



######### Method 2: #########
nums = [3,1,-2,-5,2,-4]

LEN = len(nums)

p = 0
n = 1
result = [0] * LEN

for i in range(LEN):
    if nums[i] >= 0:
        result[p] = nums[i]
        p += 2
    else:
        result[n] = nums[i]
        n += 2
print(result)

# Time Complexity : O(N)
# Space Complexity : O(N)