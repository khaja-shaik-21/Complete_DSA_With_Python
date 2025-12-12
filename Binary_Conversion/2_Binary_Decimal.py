def binaryTodecimal(bin_num):
    dec_num = 0
    n = len(bin_num)
    power = 0
    index = n - 1
    
    while index >= 0:
        num = int(bin_num[index]) * (2**power)
        dec_num += num
        index -= 1
        power += 1
    return dec_num

bin_num = "1011"
ans = binaryTodecimal(bin_num)
print(ans)

# Time Complexity : O(len)
# Space Complexity : O(1)