"""
Finding the Largets value in List / Array
"""

######### Method 1: #########

nums = [2, 10, 5, 11]
    
largest = 0
    
for i in nums:
    if i> largest:
        largest = i
print(largest)
    
# Output: 11

nums = [-2, 10, 55, -90]
    
largest = 0
    
for i in nums:
    if i> largest:
        largest = i
print(largest)
    
# Output: 55

# Time Complexity : O(N)
# Space Complexity : O(1)


######### Method 2: #########

nums = [-2, 10, 55, -90]
    
lrgst = nums[0]
    
for i in range(1, len(nums)):
    if nums[i] > lrgst:
        lrgst = nums[i]
print(lrgst)
    
# Output: 55



nums = [-2, 10, 55, -90]
    
lrgst = nums[0]
    
for i in range(1, len(nums)):
    lrgst = max(nums[i], lrgst)  # TC : O(1), taking two values only not the whole list
    
print(lrgst)
    
# Output: 55

# Time Complexity : O(N)
# Space Complexity : O(1)





######## Method 3: #########

nums = [-2, 10, 55, -90]
    
lrgst = float("-inf")
    
for i in range(1, len(nums)):
    if nums[i] > lrgst:
        lrgst = nums[i]
print(lrgst)
    
# Output: 55

# Time Complexity : O(N)
# Space Complexity : O(1)