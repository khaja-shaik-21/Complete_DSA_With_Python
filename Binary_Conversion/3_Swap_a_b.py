"""
Swapping of A and B using XOR operator
"""
a = 5

b = 10

# Swap a value to b, b value to a
a = a^b     # a = 5 ^ 10 = 0101 ^ 1010 = 1111 (binary) = 15

b = a^b     # b = 15 ^ 10 = 1111 ^ 1010 = 0101 (binary) = 5

a = a^b     # a = 15 ^ 5 = 1111 ^ 0101 = 1010 (binary) = 10

print(a, b)