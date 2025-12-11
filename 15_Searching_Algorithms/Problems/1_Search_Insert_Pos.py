"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 

If not, return the index where it would be if it were inserted in order.
"""

class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        lb = n
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return lb


nums = [1, 3, 5, 6]
target = 5

obj = Solution()
ans = obj.searchInsert(nums, target)
print(ans)
