"""
Find the factors that will divide the number and make it into list
"""

num = 10

###### Method 1: Bruite Force #######

result = []
for i in range(1, num):         # O(N)
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)

# Time Complexity = O(N)
# Space Complexity = O(K) K = no.of factors



###### Method 2: #######
result = []
for i in range(1, num//2 + 1):      # O(N/2) ~ O(N)
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)

# Time Complexity = O(N/2) ~ O(N)
# Space Complexity = O(K) K = no.of factors



###### Method 3: #######
import math
result = []
for i in range(1, int(math.sqrt(num) + 1)):     # O(√N)
    if num % i == 0:
        result.append(i)
    if num // i != i:
        result.append(num//i)
print(result)

result.sort()       # O(NlogN)

print(result)

# Time Complexity = O(√N) + O(NlogN)
# Space Complexity = O(K) K = no.of factors