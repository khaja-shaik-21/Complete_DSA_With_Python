"""
Given a sorted doubly linked list of positive distinct elements, 
the task is to find pairs in a doubly-linked list whose sum is equal to given value target.
"""
####### Method 1: ####### 
class Solution:
    def findPairsWithGivenSum(self, target, head):
        
        curr = head
        
        result = []
        my_set = set()
        
        while curr:
            rem = target - curr.data
            if rem in my_set:
                result.append([rem, curr.data])
            my_set.add(rem)
            curr = curr.next
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)




####### Method 2: #######
class Solution:
    def findPairsWithGivenSum(self, target, head):
        left = head
        right = head
        while right.next:
            right = right.next
        
        result = []

        while left and right and left.data < right.data:
            tot = left.data + right.data
            if tot == target:
                result.append([left.data, right.data])
                left = left.next
                right = right.prev
            elif tot > target:
                right = right.prev
            else:
                left = left.next
        return result

# Time Complexity : O(N)
# Space Complexity : O(1)