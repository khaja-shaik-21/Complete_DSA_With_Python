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


######## Right View of Binary Tree ########

# Method 1: Bruite Force
from collections import deque
class Solution:
    def rightSideView(self, root):
        
        result = []
        queue = deque([])
        queue.append(root)
        
        while queue:
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.popleft()
                
                if i == len_queue - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
# Method 2: DFS - Reverse postOrder(root-right-left)
class Solution:
    def rightSideView(self, root):
        
        def reverse(node, level, ans):
            if not node:
                return
            
            # If this is the first node we are visiting at this level, add it
            if level == len(ans):
                ans.append(node.val)
            
            # Visit the right subtree first
            reverse(node.right, level + 1, ans)
            # Then visit the left subtree
            reverse(node.left, level + 1, ans)
        
        ans = []
        reverse(root, 0, ans)
        return ans