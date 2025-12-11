# Using Recursion....
def fibonacci(n):
    if n <= 0 or n == 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(15))

for i in range(15+1):
    print(fibonacci(i), end=' ')
print()

# Time Complexity : O(2^n)
# Space Complexity : o(n)



# Uisng Iteration.....
def fibonacci_iterative(n):
    if n < 2:
        return n
    
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci_iterative(10)

# Time Complexity : O(n)
# Space Complexity : o(1)