"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

# Method 1: Bruite Force using Dictionary
nums = [4,1,2,1,2]
my_dict = {}

for i in nums:
    my_dict[i] = my_dict.get(i, 0) + 1

for key in my_dict:
    if my_dict[key] == 1:
        print(key)
        break
# Time Complexity : ~O(N)
# Space Complexity : o(N/2 + 1)

# Method 1: Using XOR Operations
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
"""
nums = [4, 1, 2, 1, 2]

result = 0

result ^= 4
    000 ^ 100 = 100

result ^= 1
    100 ^ 001 = 101

result ^= 2
    101 ^ 010 = 111

result ^= 1
    111 ^ 001 = 110

result ^= 2
    110 ^ 010 = 100

Final result = 4 (single number)

"""