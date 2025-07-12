from queue import Queue  

# Node class for AVL Tree
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1  


# Preorder Traversal (Root -> Left -> Right)
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=' ')
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# Inorder Traversal (Left -> Root -> Right)
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=' ')
    inOrderTraversal(rootNode.rightChild)

# Postorder Traversal (Left -> Right -> Root)
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=' ')

# Level Order Traversal using Queue
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    q = Queue()
    q.put(rootNode)
    while not q.empty():
        node = q.get()
        print(node.data, end=' ')
        if node.leftChild:
            q.put(node.leftChild)
        if node.rightChild:
            q.put(node.rightChild)
            

# Return height of the node (0 if None)
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

# Return balance factor of node
def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

# Perform right rotation (used in LL and LR imbalance)
def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = newRoot.rightChild
    newRoot.rightChild = disbalanceNode

    # Update heights
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# Perform left rotation (used in RR and RL imbalance)
def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = newRoot.leftChild
    newRoot.leftChild = disbalanceNode

    # Update heights
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


# Insert a node and rebalance if necessary
def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)

    if nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    # Update height
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))

    # Check balance and perform rotations
    balance = getBalance(rootNode)

    # Case LL
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    # Case LR
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    # Case RR
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    # Case RL
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode

# Get node with minimum value (used during deletion)
def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

# Delete a node and rebalance tree
def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode

    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        # Node with one or no child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        # Node with two children
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    if not rootNode:
        return rootNode

    # Update height
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))

    # Rebalance
    balance = getBalance(rootNode)

    # Rotations based on balance
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode


# Recursive search for a value
def searchNode(rootNode, nodeValue):
    if not rootNode:
        print("The value is not found")
        return
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        searchNode(rootNode.leftChild, nodeValue)
    else:
        searchNode(rootNode.rightChild, nodeValue)

# Clear the entire tree
def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL has been successfully deleted"


# Print AVL Tree using InOrder & LevelOrder
def printTree(root, level=0, prefix="Root: "):
    if root is not None:
        printTree(root.rightChild, level + 1, "-- ")
        print("     " * level + prefix + str(root.data))
        printTree(root.leftChild, level + 1, "-- ")


# Function to check if AVL Tree is balanced and rebalance if needed
def checkAndRebalanceAVL(root):
    if root is None:
        print("The AVL tree is empty. Nothing to rebalance.")
        return root
    
    # 🔍 Check if tree is balanced
    def isBalanced(node):
        if node is None:
            return True
        left_height = getHeight(node.leftChild)
        right_height = getHeight(node.rightChild)
        if abs(left_height - right_height) > 1:
            return False
        return isBalanced(node.leftChild) and isBalanced(node.rightChild)

    if isBalanced(root):
        print("AVL Tree is already balanced.")
        return root

    print("⚠️ AVL Tree is not balanced. Rebalancing now...")

    # Collect all values using in-order traversal
    values = []
    def collectInOrder(node):
        if node:
            collectInOrder(node.leftChild)
            values.append(node.data)
            collectInOrder(node.rightChild)
    collectInOrder(root)

    # Build balanced AVL from sorted array
    def buildBalancedAVL(arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        newRoot = AVLNode(arr[mid])
        newRoot.leftChild = buildBalancedAVL(arr, start, mid - 1)
        newRoot.rightChild = buildBalancedAVL(arr, mid + 1, end)
        newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
        return newRoot

    newRoot = buildBalancedAVL(values, 0, len(values) - 1)
    print("Tree rebalanced successfully.")
    return newRoot


def menu():
    print("\n===== AVL TREE MENU =====")
    print("1. Insert Node")
    print("2. Delete Node")
    print("3. Search Node")
    print("4. PreOrder Traversal")
    print("5. InOrder Traversal")
    print("6. PostOrder Traversal")
    print("7. LevelOrder Traversal")
    print("8. Delete Entire Tree")
    print("9. Check and Rebalance AVL Tree (if needed)")
    print("10. Exit")


root = None

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        val = int(input("Enter value to insert: "))
        root = insertNode(root, val)
        printTree(root)  
    elif choice == '2':
        val = int(input("Enter value to delete: "))
        root = deleteNode(root, val)
        printTree(root)  
    elif choice == '3':
        val = int(input("Enter value to search: "))
        searchNode(root, val)
        printTree(root)  
    elif choice == '4':
        print("PreOrder: ", end='')
        preOrderTraversal(root)
        print()
    elif choice == '5':
        print("InOrder: ", end='')
        inOrderTraversal(root)
        print()
    elif choice == '6':
        print("PostOrder: ", end='')
        postOrderTraversal(root)
        print()
    elif choice == '7':
        print("LevelOrder: ", end='')
        levelOrderTraversal(root)
        print()
    elif choice == '8':
        deleteAVL(root)
        root = None
        print("Tree deleted.")
    elif choice == '9':
        root = checkAndRebalanceAVL(root)
        print("\nCurrent AVL Tree:")
        printTree(root)

    elif choice == '10':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Try again.")


#############   Time & Space Complexity Table: AVL Tree using Queue  ############


# | Operation              | Time Complexity            | Space Complexity          | Notes                                                   |
# | ---------------------- | ---------------------------| --------------------------| --------------------------------------------------------|
# | insert_node()          | O(log n) avg / O(n) worst  | O(log n) avg / O(n) worst | Goes down one path from root to leaf (height of tree)   |
# | search_node()          | O(log n) avg / O(n) worst  | O(log n) avg / O(n) worst | Same as insert — path from root to node                 |
# | delete_node()          | O(log n) avg / O(n) worst  | O(log n) avg / O(n) worst | One recursive pass to locate and fix tree               |
# | min_value_node()       | O(log n) avg / O(n) worst  | O(1)                      | Follows left children only                              |
# | pre_order()            | O(n)                       | O(n) worst                | Recursive; space used by call stack                     |
# | in_order()             | O(n)                       | O(n) worst                | Same as above                                           |
# | post_order()           | O(n)                       | O(n) worst                | Same as above                                           |
# | level_order()          | O(n)                       | O(n)                      | Uses a queue storing up to all nodes at one level       |
# | print_tree()           | O(n)                       | O(log n) avg / O(n) worst | Recursive sideways printing, depth controls indentation |
# | delete_entire_tree()   | O(1)                       | O(1)                      | Just sets root to `None`                                |
# | check_and_rebalance()  | O(n)                       | O(n)                      | In-order traversal + rebuild from sorted array          |
