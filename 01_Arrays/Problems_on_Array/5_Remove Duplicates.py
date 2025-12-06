"""
Remove Duplicates from Sorted Array
"""

######### Method 1: #########

nums = [0,0,1,1,2,3,4,4,5,6,6]

Len = len(nums)
freq_map = {}
for i in range(Len):          # O(N)
    freq_map[nums[i]] = 0

j = 0
for k in freq_map:          # O(N)
    nums[j] = k
    j += 1
print(nums[:j])

# Time Complexity : O(N)+O(N) = O(2N) ~O(N)
# Space Complexity : O(N)



######### Method 2: #########

nums = [0,0,1,1,2,3,4,4,5,6,6]

Len = len(nums)

i = 0
j = i+1
while j < Len:
    if nums[j] != nums[i]:
        i +=1
        nums[i], nums[j] = nums[j], nums[i]
    j += 1
print(i+1)

# Time Complexity : O(N)
# Space Complexity : O(1)