"""
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""
# Method 1: Bruite Force
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

maxi = 0
n = len(nums)
for i in range(n):
    zeros = 0
    for j in range(i, n):
        if nums[j] == 0:
            zeros += 1
        if zeros > k:
            break
        
        maxi = max(maxi, j-i+1)
print(maxi)

# Time Complexity : O(n^2)
# Space Complexity : O(1)



# Method 1: Sliding Window
def max_num(nums, k):
    maxi = 0
    left = 0
    zeros = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        # Shrink window if zeros exceed k
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # Window is valid → update max length
        maxi = max(maxi, right - left + 1)

    return maxi

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
ans = max_num(nums, k)
print(ans)

# Time Complexity : O(2n)
# Space Complexity : O(1)



# Method 3: Sliding Window optimal
def max_num(nums, k):
    maxi = 0
    left = 0
    zeros = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        # Shrink window if zeros exceed k
        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # Window is valid → update max length
        maxi = max(maxi, right - left + 1)

    return maxi

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
ans = max_num(nums, k)
print(ans)