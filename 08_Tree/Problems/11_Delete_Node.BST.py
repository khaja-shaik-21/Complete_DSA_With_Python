"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None
        
        # search for the key
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # node to delete found
            
            # case 1: no left child
            if root.left is None:
                return root.right
            
            # case 2: no right child
            if root.right is None:
                return root.left
            
            # case 3: two children
            # find inorder successor (min value in right subtree)
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        
        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
