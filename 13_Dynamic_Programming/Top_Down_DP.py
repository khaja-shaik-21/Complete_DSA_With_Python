"""
Recursion Top down Approach for the Fibonacci using the Dynamic Programming

Fibonacci Memorization storing the data and using it without doing it again
"""
def fibonacci(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

memo = {}
ans = fibonacci(6, memo)
print(ans)


# Time Complexity : O(n)
# Space Complexity : O(n)