"""
Print the sum of the numbers of range
"""

def sumFunc(sum, i, n):
    if i > n:
        return 0
    tot = sum + i
    print(f"{sum} + {i} = {tot}")
    sumFunc(sum+i, i+1, n)

sumFunc(0, 1, 10)


def fun(N):
    if N == 0:
        return 0
    return N + fun(N-1)
print(fun(10))