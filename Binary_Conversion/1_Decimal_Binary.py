def decimalTobinary(num):
    result = ''
    n = num
    while n > 0:
        if n % 2 == 1:
            result += '1'
        else:
            result += '0'
        n //= 2
    return result[::-1]

num = 25
ans = decimalTobinary(num)
print(ans)

# Time Complexity : O(len)
# Space Complexity : O(1)