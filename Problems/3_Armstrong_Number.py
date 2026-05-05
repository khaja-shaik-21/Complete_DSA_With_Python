"""
An Armstrong number (also called a Narcissistic number) is a number that is equal to the sum of its own digits, where each digit is raised to the power of the total number of digits in the number.

153 = 1³ + 5³ + 3³
    = 1 + 125 + 27
    = 153

1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
     = 1 + 1296 + 81 + 256
     = 1634

"""
n = 152

nod = len(str(n))
result = 0
num = n

while num > 0:
    val = num % 10
    result += val ** nod
    num //= 10
print(result)
print('Armstrong Number' if result == n else "Not Armstrong Number")

# Time complexity: O(log n) where n is the input number
# Space complexity: O(1)