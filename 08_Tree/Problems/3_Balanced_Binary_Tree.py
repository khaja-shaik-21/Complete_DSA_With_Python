"""
Given a binary tree, determine if it is height-balanced.
"""
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.balance = 0
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        height(root)
        return False if self.balance == -1 else True