"""
Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

class Solution:
    def maxPathSum(self, root):
        self.maxi = float("-inf")

        def height(node):
            if not node:
                return 0

            # Get max path from left and right (ignore negatives)
            left = max(0, height(node.left))
            right = max(0, height(node.right))

            # Update global maximum using current node
            self.maxi = max(self.maxi, left + node.val + right)

            # Return path sum including current node to parent
            return node.val + max(left, right)

        height(root)
        return self.maxi
