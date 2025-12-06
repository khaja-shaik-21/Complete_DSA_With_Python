"""
Find the Maximum profit to get while buying and sell the stock.
"""

######### Method 1: #########
nums = [7,1,5,3,6,4]

n = len(nums)
maxi = float("-inf")
for i in range(n):
    for j in range(i+1, n):
        if nums[j] > nums[i]:
            p = nums[j] - nums[i]
            maxi = max(maxi, p)
print(maxi)

# Time Complexity : O(N^2)
# Space Complexity : O(1)

######### Method 2: #########
nums = [7,1,5,3,6,4]
n = len(nums)

maxi = 0
mini = nums[0]
for i in  range(n):
    mini = min(mini, nums[i])
    maxi = max(maxi, nums[i] - mini)
print(maxi)

# Time Complexity : O(N)
# Space Complexity : O(1)


######### Method 2: #########

prices = [7,1,5,3,6,4]

min_price = prices[0]
max_profit = 0
        
for price in prices:
    if price < min_price:
        min_price = price
    elif price - min_price > max_profit:
        max_profit = price - min_price
        
print(max_profit)

# Time Complexity : O(N)
# Space Complexity : O(1)