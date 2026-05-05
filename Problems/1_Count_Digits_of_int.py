"""
Count the no of digits of an integer
"""

###### Method 1: ######
n = 5678
num = n
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)

# Time complexity: O(log n) where n is the input number
# Space complexity: O(1)

###### Method 2: Pythanic way ######
import math

print(int(math.log10(abs(n)) + 1))


###### Method 2: Pythanic way convert to str ######
num = 12345
print(len(str(abs(num))))
