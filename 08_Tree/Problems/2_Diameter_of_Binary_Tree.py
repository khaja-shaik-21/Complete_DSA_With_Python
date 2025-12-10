"""
Given the root of a binary tree, return the length of the diameter of the tree.
"""

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter = 0
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        height(root)
        return self.diameter