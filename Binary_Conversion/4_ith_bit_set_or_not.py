"""
Given two positive integer n and  k, check if the kth index bit of n is set or not.
 Note: A bit is called set if it is 1. 
"""

# Method 1: Letf Shift Operator
n = 13
i = 1

if (n & (1 << i)) != 0:
    print(True)
else:
    print(False)


# Method 2: Right Shift Operator
n = 13
i = 1

if ((n >> i) & 1) == 1:
    print(True)
else:
    print(False)
