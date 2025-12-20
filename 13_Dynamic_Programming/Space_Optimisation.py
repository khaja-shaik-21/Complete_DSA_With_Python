"""
Tabulation Space Optimisation

"""

n = 3
prev = 0
next = 1

for i in range(2, n+1):
    curr = prev + next
    prev = next
    next = curr
print(next)

# Time Complexity : O(N)
# Space Comlexity : O(1)