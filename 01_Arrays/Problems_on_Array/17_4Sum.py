"""
Given an array nums of n integers, 
return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.

"""
nums = [1,0,-1,0,-2,2]
target = 0

n = len(nums)

######### Method 1: Bruit Force #########
result = set()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if nums[i] + nums[j] + nums[k] + nums[l] == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    temp.sort()
                    result.add(tuple(temp))
print([list(ans) for ans in result])

# Time Complexity : O(N^4)
# Space Complexity : O(N)



######### Method 2: #########
result = set()
for i in range(n):
    for j in range(i+1, n):
        my_set = set()
        for k in range(j+1, n):
            fourth = target - (nums[i] + nums[j] + nums[k])
            if fourth in my_set:
                temp = [nums[i], nums[j], nums[k], fourth]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(nums[k])
print([list(ans) for ans in result])

# Time Complexity : O(N^3)
# Space Complexity : O(N)




######### Method 2: #########
nums.sort()
result = []

for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    
    for j in range(i+1, n):
        if j > i + 1 and nums[j] == nums[j-1]:
            continue
        
        k = j + 1
        l = n - 1
        
        while k < l:
            tot = nums[i] + nums[j] + nums[k] + nums[l]
            
            if tot == target:
                result.append([nums[i], nums[j], nums[k], nums[l]])
                k += 1
                l -= 1
                
                while k < l and nums[k] == nums[k-1]:
                    k+= 1
                while l > k and nums[l] == nums[l+1]:
                    l -= 1
            elif tot < target:
                k += 1
            
            else:
                l -= 1
print([ans for ans in result])

# Time Complexity : O(N^3)
# Space Complexity : O(No.of answers)