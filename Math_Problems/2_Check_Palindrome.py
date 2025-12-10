"""
Check is an number of string is a palindrome

Palindrome is nothing but a thing that oringal number or a string is same as when we reverse it

integer : 1234 == 4321
string : "MOM" == "MOM"

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
