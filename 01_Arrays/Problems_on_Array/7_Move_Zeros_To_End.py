"""
move all 0's to the end of Array
"""

######### Method 1: Bruite Force #########
nums = [0,1,0,3,12]

n = len(nums)
temp = []
for i in range(n):              # O(N)
    if nums[i] != 0:
        temp.append(nums[i])


nz = len(temp)
for i in range(nz):             # O(N/2)
    nums[i] = temp[i]
    
for i in range(nz, n):          # O(N/2)
    nums[i] = 0

print(nums)

# Time Complexity : O(N) + (O(N/2) + O(N/2)) = O(N) + O(2N/2) = ON(N) + O(N) = O(2N) ~ O(N)
# Space Complexity : O(N)



######### Method 2: #########
nums = [0,1,0,3,12]

n = len(nums)

i = 0
while i < n:
    if nums[i] == 0:
        break

j = i+1
while j< n:
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    j += 1
print(nums) 

# Time Complexity : O(N)
# Space Complexity : O(1)



######### Method 2: ######### 

nums = [0,1,0,3,12]
nzero=0
m= len(nums)
        
arr= [0]*m
idx=0
for i in range(m):
    if nums[i]!=0:
        arr[idx]= nums[i]
        idx+=1
    
for i in range(m):
    nums[i] = arr[i]
print(nums)
# Time Complexity : O(N) + O(N) = O(2N) ~ O(N)
# Space Complexity : O(N)