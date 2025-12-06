"""
Find the Missing Number in an Array
"""
######### Method 1: #########
nums = [9,6,4,2,3,5,7,0,1]

n = len(nums)

for i in range(n):          # O(N)
    if i not in nums:       # O(N)
        print(i)
        break

# Time Complexity : O(N^2)
# Space Complexity : O(1)



######### Method 2: #########
nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)

freq = {}
for i in range(n):
    freq[i] = 0

for i in nums:
    freq[i] = 1

for k, v in freq.items():
    if v == 0:
        print(k)
        break
    
# Time Complexity : O(N) + O(N) + O(N) = O(3N) ~ O(N)
# Space Complexity : O(N)


######### Method 3: #########
nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)

Total_Sum = sum(range(n+1))     # O(N)

#   OR

# Total_Sum = 0                 O(N)
# for i in range(1, n+1):
#     Total_Sum += i

nums_sum = 0                    # O(N)
for i in nums:
    nums_sum += i

print(Total_Sum - nums_sum)

# Time Complexity : O(N) + O(N) = O(2N) ~ O(N)
# Space Complexity : O(1)



######### Method 4: #########
nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)


print((n*(n+1))//2 - sum(nums))

# Time Complexity : O(N)
# Space Complexity : O(1)