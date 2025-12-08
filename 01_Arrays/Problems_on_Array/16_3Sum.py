"""
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k and j != k
and nums[i] + nums[j] + nums[k] == 0.
"""

nums = [-1,0,1,2,-1,-4]

n = len(nums)


######### Method 1: Bruit Force #########
my_set = set()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                temp = [nums[i], nums[j], nums[k]]
                temp.sort()
                my_set.add(tuple(temp))

print([list(ans) for ans in my_set])

# Time Complexity : O(N^3)
# Space Complexity : O(No.of Triplets)


######### Method 2: #########
result = set()

for i in range(n):
    my_set = set()
    for j in range(i+1, n):
        third = -(nums[i] + nums[j])
        if third in my_set:
            temp = [nums[i], nums[j], third]
            temp.sort()
            result.add(tuple(temp))
        my_set.add(nums[j])
print([list(ans) for ans in result])

# Time Complexity : O(N^2)
# Space Complexity : O(N) + O(No.of Triplets)



######### Method 3: #########

ans = []
nums.sort()

for i in range(n):
    if i != 0 and nums[i] == nums[i-1]:
        continue
    
    j = i + 1
    k = n - 1
    
    while j < k:
        tot = nums[i] + nums[j] + nums[k]
        if tot < 0:
            j += 1
        elif tot > 0:
            k -= 1
        else:
            temp = [nums[i], nums[j], nums[k]]
            ans.append(temp)
            j += 1
            k -= 1
            
            while j < k and nums[j] == nums[j+1]:
                j += 1
            while j < k and nums[k] == nums[k-1]:
                 k -= 1
print(ans)

# Time Complexity : O(NlogN) + O(N^2)
# Space Complexity : O(No.of Triplets)