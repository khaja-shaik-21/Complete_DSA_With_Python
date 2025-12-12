"""
You are given a root binary search tree and an integer x . Your task is to find the Ceil of x in the tree.

Note: Ceil(x) is a number that is either equal to x or is immediately greater than x.
        If Ceil could not be found, return -1.
"""


class Solution:
    def findCeil(self,root, x):
        # code here
        mini = -1
        
        while root:
            if root.data == x:
                return root.data
            elif root.data < x:
                root = root.right
            else:
                mini = root.data
                root = root.left
        return mini
    
# Time complexity : O(log2​n)
# Space Complexity : O(1)