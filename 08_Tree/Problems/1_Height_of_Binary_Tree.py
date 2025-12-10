"""
Given the root of a binary tree, return its maximum depth.
"""
####### Method 1: #######
class Solution:
    def maxDepth(self, root):
        def height(node):
            if node is None:
                return 0

            left_h = height(node.left)
            right_h = height(node.right)

            return 1 + max(left_h, right_h)

        return height(root)
    
####### Method 2: Using Iteration #######
from collections import deque

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        queue = deque([root])
        h = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            h += 1

        return h
