"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, 
as long as the tree remains a BST after insertion. You can return any of them.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val):
        # If tree is empty, create and return new root
        if root is None:
            return TreeNode(val)

        temp = root

        while True:
            if val < temp.val:
                if temp.left is None:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right

        return root
