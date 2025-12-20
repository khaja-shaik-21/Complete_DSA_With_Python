"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
# Method 1: Reccursion 
def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    return climbStairs(n - 1) + climbStairs(n -2)
n = 2
ans = climbStairs(n)
print(ans)
# Time Complexity : O(N)
# Space Comlexity : O(N)

# Method 1: Space Optimisation
n = 2
prev = 1
next = 1

for i in range(2, n+1):
    curr = prev + next
    prev = next
    next = curr
print(next)
# Time Complexity : O(N)
# Space Comlexity : O(1)