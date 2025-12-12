"""
Given the integer array fruits, return the maximum number of fruits you can pick.
"""
##### Method 1: Bruite Force #####
fruits = [1,2,3,2,2]

n = len(fruits)

maxi = 0

for i in range(n):
    my_set = set()
    for j in range(i, n):
        my_set.add(fruits[j])
        if len(my_set) > 2:
            break
        
        maxi = max(maxi, j - i + 1)
print(maxi)

# Time Complexity : O(N^2)
# Space Complexity : O(1)


##### Method 2: Better #####

fruits = [1,2,3,2,2]
maxi = 0
n = len(fruits)
my_dict = dict()
l = 0
r = 0

while r < n:
    my_dict[fruits[r]] = my_dict.get(fruits[r], 0) + 1
    
    while len(my_dict) > 2:
        my_dict[fruits[l]] -= 1
        
        if my_dict[fruits[l]] == 0:
            del my_dict[fruits[l]]
        l += 1
    
    if len(my_dict) <= 2:
        maxi = max(maxi, r - l + 1)
    r += 1
print(maxi)

# Time Complexity : O(2N)
# Space Complexity : O(1)



##### Method 2: Optimal #####

fruits = [1,2,3,2,2]
maxi = 0
n = len(fruits)
my_dict = dict()
l = 0
r = 0

while r < n:
    my_dict[fruits[r]] = my_dict.get(fruits[r], 0) + 1
    
    if len(my_dict) > 2:
        my_dict[fruits[l]] -= 1
        
        if my_dict[fruits[l]] == 0:
            del my_dict[fruits[l]]
        l += 1
    
    if len(my_dict) <= 2:
        maxi = max(maxi, r - l + 1)
    r += 1
print(maxi)

