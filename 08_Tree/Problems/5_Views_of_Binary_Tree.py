"""
                1
              /   \
             2     3
            / \   / \
           4   5 6   7
          /
         8

Vertical Lines (Top View Perspective):

   |      |      |      |      |      |
   |      |      |      |      |      |
   8      4      2      1      3      7

Top View Output:
[8, 4, 2, 1, 3, 7]

"""

from collections import deque

######## Top View of Binary Tree ########

class Solution:
    def topView(self, root):
        if not root:
            return None
        ans = []
        queue = deque()
        result = {}
        queue.append((root, 0))
        while queue:
            e, line = queue.popleft()
            if line not in result:          # Remove This line to get Bottom View of Binary Tree
                result[line] = e.data
            if e.left:
                queue.append((e.left, line -1))
            if e.right:
                queue.append((e.right, line + 1))
        for value in sorted(result.items()):
            ans.append(value[1])
        return ans
    
    

######## Bottom View of Binary Tree ########
class Solution:
    def topView(self, root):
        if not root:
            return None
        ans = []
        queue = deque()
        result = {}
        queue.append((root, 0))
        while queue:
            e, line = queue.popleft()
            result[line] = e.data
            if e.left:
                queue.append((e.left, line -1))
            if e.right:
                queue.append((e.right, line + 1))
        for value in sorted(result.items()):
            ans.append(value[1])
        return ans