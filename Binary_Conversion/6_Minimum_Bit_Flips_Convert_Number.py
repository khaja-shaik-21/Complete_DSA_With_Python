"""
A bit flip of a number x is choosing a bit in the binary representation of x 
and flipping it from either 0 to 1 or 1 to 0.

Ex: 10 - 1011 -> 0111 - 7
 
"""

# Method 1
start = 10
end = 7

ans = start ^ end

print(bin(ans).count('1'))

# Time Complexity: O(k) ~ O(1)  k is the number of bits of the number
# Space Complexity: O(1)



# Method 2
start = 10
end = 7

ans = start ^ end
count = 0
for i in range(32):
    if ans & (1 << i) != 0:
        count += 1
print(count)


""" Code workflow
start = 10 (1010)
end   = 7  (0111)

XOR:
    1010
  ^ 0111
  -------
    1101  → ans = 13

Check bits 0-31:

i = 0
    mask = 0001
    1101 & 0001 = 0001 → count = 1

i = 1
    mask = 0010
    1101 & 0010 = 0000 → count = 1

i = 2
    mask = 0100
    1101 & 0100 = 0100 → count = 2

i = 3
    mask = 1000
    1101 & 1000 = 1000 → count = 3

i = 4..31
    all AND = 0 → count stays 3

Final output = 3

"""
# Time Complexity: O(32) ~ O(1)  32 is the number of bits of the number
# Space Complexity: O(1)

