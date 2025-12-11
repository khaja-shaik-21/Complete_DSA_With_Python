"""
Print N - 1 numbers using Recursion
"""
def num(n):     # Head Recursion
    if n == 0:
        return 0
    print(n)
    num(n-1)
num(5)

def num(x, n):      # Tail Recursion
    if x > n:
        return 0
    num(x+1, n)
    print(x)
    
num(x=1, n=5)


"""
Print 1 - N numbers using Recursion
"""
def num(n):     # Head Recursion
    if n == 0:
        return 0
    num(n-1)
    print(n)
num(5)

def num(x, n):      # Tail Recursion
    if x > n:
        return 0
    print(x)
    num(x+1, n)
    
num(x=1, n=5)