"""
Rotate the array to the right by 1
"""

######### Method 1: Slicing #########

nums = [1, 2, 3, 4, 5, 6, 7]

nums[:] = [nums[len(nums)-1]] + nums[:len(nums)-1]  

print(nums)  # Output: [7, 1, 2, 3, 4, 5, 6]

# Time Complexity : O(N)
# Space Complexity : O(1)



######### Method 2: #########

nums = [1, 2, 3, 4, 5, 6, 7]
temp = nums[-1]

for i in range(len(nums) - 2, -1, -1):
    nums[i+1] = nums[i]
print(nums)

# Time Complexity : O(N)
# Space Complexity : O(1)



"""
Rotate the array to the right by k
"""

######### Method 1: #########
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
for _ in range(k):
    nums[:] = [nums[-1]] + nums[:len(nums) - 1]
print(nums)



######### Method 2: Reduce Rotations #########
nums = [1, 2, 3, 4, 5, 6, 7]
k = 9

rotations = k % len(nums)

for _ in range(rotations):
    e = nums.pop()
    nums.insert(0, e)

print(nums)

######### Method 3: Slicing #########
nums = [1, 2, 3, 4, 5, 6, 7]
k = 5

nums[:] = nums[len(nums) - k: ] + nums[:len(nums) - k]
print(nums)


######### Method 1: #########
nums = [1, 2, 3, 4, 5, 6, 7]
k = 5
n = len(nums)

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # Handle k > n
    
    # All three reversals in one function
    reverse(nums, n-k, n-1)      # Reverse last k elements
    reverse(nums, 0, n-k-1)      # Reverse first n-k elements
    reverse(nums, 0, n-1)        # Reverse entire array

rotate_array(nums, k)  # ✓ Single function call

print(nums)  # [3, 4, 5, 6, 7, 1, 2]

# Time Complexity : O(K)+O(N-K)+O(N) = O(K+N-K+N) = O(2N) ~ O(N)
# Space Complexity : O(1)