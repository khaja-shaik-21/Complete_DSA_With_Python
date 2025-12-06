"""
Finding the Second Largest value in the List / Array
"""

######### Method 1: #########

nums = [55, 32, 97, -55, 45, 32, 88, 21]

nums.sort()

print(nums) # [-55, 21, 32, 32, 45, 55, 88, 97]

print(nums[-2]) # 88

# Time Complexity : O(NlogN), because of sorting()
# Space Complexity : O(1)




######### Method 2: #########

nums = [55, 32, 97, -55, 45, 32, 88, 21]

largest = float("-inf")
second_largest = float("-inf")

Len = len(nums)

for i in range(Len):                  # O(N)
    largest = max(nums[i], largest)

for i in range(Len):                  # O(N)
    if nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]
        
print(second_largest) # 88

# Time Complexity : O(N) + O(N) = O(2N) ~ O(N)
# Space Complexity : O(1)




######### Method 3: #########

nums = [55, 32, 97, -55, 45, 32, 88, 21]

largest = float("-inf")
second_largest = float("-inf")

Len = len(nums)

for i in range(Len):                  # O(N)
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]
print(second_largest)

# Time Complexity : O(N)
# Space Complexity : O(1)