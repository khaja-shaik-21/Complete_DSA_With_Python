"""
Check is an number of string is a palindrome

Palindrome is nothing but a thing that oringal number or a string is same as when we reverse it

integer : 1234 == 4321
string : "MOM" == "MOM"
"""

""" 
Number Palindrome
"""
n = 121
print("Number:", n)

num = n
result = 0

while num > 0:
    result = result * 10 + (num % 10)
    num = num // 10

print("Reversed:", result)

if n == result:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Time complexity: O(log n) where n is the input number
# Space complexity: O(1)


"""
String Palindrome
"""
def reverse(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return f'{s} is Not Palindrome'
        left += 1
        right -= 1
    return f"{s} is Palindrome"
s = "mome"
n = len(s)
left = 0
right = n - 1
print("String:",s)
print(reverse(s, left, right))    

# Time complexity: O(n) where n is the length of the input string
# Space complexity: O(1)