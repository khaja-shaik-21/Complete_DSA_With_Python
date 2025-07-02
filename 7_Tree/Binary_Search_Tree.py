# Binary Search Tree

from collections import deque

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(rootNode, nodevalue):
    if rootNode is None:
        return BSTNode(nodevalue)
    elif nodevalue < rootNode.data:
        rootNode.left = insert(rootNode.left, nodevalue)
    else:
        rootNode.right = insert(rootNode.right, nodevalue)
    return rootNode

def preOrder(rootNode):
    if rootNode:
        print(rootNode.data, end=" ")
        preOrder(rootNode.left)
        preOrder(rootNode.right)

def inOrder(rootNode):
    if rootNode:
        inOrder(rootNode.left)
        print(rootNode.data, end=" ")
        inOrder(rootNode.right)

def postOrder(rootNode):
    if rootNode:
        postOrder(rootNode.left)
        postOrder(rootNode.right)
        print(rootNode.data, end=" ")

def levelOrder(rootNode):
    if not rootNode:
        return
    queue = deque([rootNode])
    while queue:
        current = queue.popleft()
        print(current.data, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def searchNode(rootNode, nodevalue):
    if rootNode is None:
        return 'Not Found'
    if rootNode.data == nodevalue:
        return 'The value is Found'
    elif nodevalue < rootNode.data:
        return searchNode(rootNode.left, nodevalue)
    else:
        return searchNode(rootNode.right, nodevalue)

def minValueNode(rootNode):
    current = rootNode
    while current.left:
        current = current.left
    return current

def deleteNode(rootNode, nodevalue):
    if rootNode is None:
        return None
    if nodevalue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodevalue)
    elif nodevalue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodevalue)
    else:
        if rootNode.left is None:
            return rootNode.right
        elif rootNode.right is None:
            return rootNode.left
        temp = minValueNode(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)
    return rootNode

def deleteTree(rootNode):
    rootNode = None
    rootNode.left = None
    rootNode.right = None
    return "The BST has successfully deleted."

def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print('    ' * level + str(node.data))
        printTree(node.left, level + 1)


# -------- Menu-Driven Program --------
def menu():
    root = None
    while True:
        print("\n====== Binary Search Tree Menu ======")
        print("1. Insert Node")
        print("2. PreOrder Traversal")
        print("3. InOrder Traversal")
        print("4. PostOrder Traversal")
        print("5. Level Order Traversal")
        print("6. Search Node")
        print("7. Delete Node")
        print("8. Delete Entire Tree")
        print("9. Display Tree Structure")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            root = insert(root, val)
        elif choice == '2':
            print("PreOrder Traversal:")
            preOrder(root)
            print()
        elif choice == '3':
            print("InOrder Traversal:")
            inOrder(root)
            print()
        elif choice == '4':
            print("PostOrder Traversal:")
            postOrder(root)
            print()
        elif choice == '5':
            print("Level Order Traversal:")
            levelOrder(root)
            print()
        elif choice == '6':
            val = int(input("Enter value to search: "))
            print(searchNode(root, val))
        elif choice == '7':
            val = int(input("Enter value to delete: "))
            root = deleteNode(root, val)
        elif choice == '8':
            root = deleteTree()
            print("BST has been deleted.")
        elif choice == '9':
            print("\nTree Structure:")
            printTree(root)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    menu()


#############   Time & Space Complexity Table: Binary Search Tree using LinkedList Nodes  ############

# | Operation              | Time Complexity            | Space Complexity          | Notes                                                   |
# | ---------------------- | ---------------------------| -----------------         | ------------------------------------------------------- |
# |  insert_node()         | O(log n) avg / O(n) worst  | O(log n) avg / O(n) worst | Goes down one path from root to leaf (height of tree)   |
# |  search_node()         | O(log n) avg / O(n) worst  | O(log n) avg / O(n) worst | Same as insert — path from root to node                 |
# |  pre_order()           | O(n)                       | O(n) worst                | Recursive; space used by call stack                     |
# |  in_order()            | O(n)                       | O(n) worst                | Same as above                                           |
# |  post_order()          | O(n)                       | O(n) worst                | Same as above                                           |
# |  level_order()         | O(n)                       | O(n)                      | Uses a queue storing up to all nodes at one level       |
# |  min_value_node()      | O(log n) avg / O(n) worst  | O(1)                      | Follows left children only                              |
# |  delete_node()         | O(log n) avg / O(n) worst  | O(log n) avg / O(n) worst | One recursive pass to locate and fix tree               |
# |  print_tree()          | O(n)                       | O(log n) avg / O(n) worst | Recursive sideways printing, depth controls indentation |
# |  delete_entire_tree()  | O(1)                       | O(1)                      | Just sets root to `None`                                |
