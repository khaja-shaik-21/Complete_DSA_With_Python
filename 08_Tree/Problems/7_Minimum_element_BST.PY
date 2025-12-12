"""
Given the root of a Binary Search Tree. 
Your task is to find the minimum element in this given BST.
"""

class Solution:
    def minValue(self, root):
        # if the tree is empty
        if root is None:
            return -1 

        # go to the leftmost node
        while root.left:
            root = root.left

        return root.data
    
# Time complexity : O(log2​n)
# Space Complexity : O(1)