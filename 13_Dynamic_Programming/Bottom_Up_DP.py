"""
Tabulation Bottom Up Approach for the Fibonacci using the Dynamic Programming

Fibonacci storing the data and using Array
"""
def fib(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp
ans = fib(6)
print(ans)

# Time Complexity : O(N)
# Space Complexity : O(N)