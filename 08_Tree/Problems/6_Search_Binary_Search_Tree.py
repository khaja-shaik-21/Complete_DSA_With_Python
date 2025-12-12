"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.
"""

class Solution:
    def searchBST(self, root, val):
        temp = root

        while temp:
            if temp.val == val:
                return temp
            elif val < temp.val:
                temp = temp.left
            else:
                temp = temp.right
                
        return None
    
# Time complexity : O(log2​n)
# Space Complexity : O(1)