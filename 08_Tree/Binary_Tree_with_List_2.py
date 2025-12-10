# Binary Tree Creation using Python List
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# DFS in Binary Trees :
def preOrder(node):              # Root - Left - Right
    if node == None:
        return 
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.Right)

def inOrder(node):              # Left - Root - Right
    if node == None:
        return 
    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.Right)

def postOrder(node):              # Left - Right - Root
    if node == None:
        return 
    postOrder(node.left)
    postOrder(node.Right)
    print(node.data, end=" ")

from collections import deque
# BFS in Binary Trees
def levelOrder(node):
    result = []
    queue = deque([])
    queue.append(node)
    
    while len(queue) != 0:
        e = queue.pop()
        result.append(e.data)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return result

