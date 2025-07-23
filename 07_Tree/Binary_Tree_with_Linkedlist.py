# Binary tree is implemented using linked list, and the queue is just a helper for processing nodes level-by-level.

from collections import deque

# Binary Tree Node class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Traversals
def pre_order(root):
    if root:
        print(root.data, end=" ")
        pre_order(root.left)
        pre_order(root.right)

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=" ")

def level_order(root):
    if not root:
        print("Tree is empty.")
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Search
def search_node(root, key):
    if not root:
        return False
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.data == key:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False

# Insert
def insert_node(root, key):
    new_node = TreeNode(key)
    if not root:
        return new_node
    queue = deque([root])
    while queue:
        temp = queue.popleft()
        if not temp.left:
            temp.left = new_node
            return root
        else:
            queue.append(temp.left)
        if not temp.right:
            temp.right = new_node
            return root
        else:
            queue.append(temp.right)

# Get deepest node
def get_deepest_node(root):
    if not root:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return node

# Delete deepest node
def delete_deepest_node(root):
    if not root:
        return None, None

    deepest = get_deepest_node(root)
    if not deepest:
        return root, None

    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            if node.left == deepest:
                deleted = node.left.data
                node.left = None
                return root, deleted
            else:
                queue.append(node.left)
        if node.right:
            if node.right == deepest:
                deleted = node.right.data
                node.right = None
                return root, deleted
            else:
                queue.append(node.right)

    # If the deepest node is the root itself and it's a single-node tree
    if root == deepest:
        deleted = root.data
        return None, deleted

    return root, None


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print('    ' * level + '->', node.data)
        print_tree(node.left, level + 1)

def delete_entire_tree():
    global newBT
    newBT = None
    print("Binary tree has been deleted successfully.")

# Menu display
def menu():
    print("\n=== Binary Tree Menu ===")
    print("1. Insert a Node")
    print("2. Preorder Traversal")
    print("3. Inorder Traversal")
    print("4. Postorder Traversal")
    print("5. Level Order Traversal")
    print("6. Search a Node")
    print("7. Get Deepest Node")
    print("8. Delete Deepest Node")
    print("9. Print the Tree")
    print("10. Delete Entire Tree")
    print("11. Exit")


def main():
    global newBT
    newBT = None
    while True:
        menu()
        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            key = input("Enter value to insert: ")
            newBT = insert_node(newBT, key)
            print("Inserted successfully.")

        elif choice == '2':
            print("Preorder Traversal:")
            if newBT: pre_order(newBT)
            else: print("Tree is empty.")

        elif choice == '3':
            print("Inorder Traversal:")
            if newBT: in_order(newBT)
            else: print("Tree is empty.")

        elif choice == '4':
            print("Postorder Traversal:")
            if newBT: post_order(newBT)
            else: print("Tree is empty.")

        elif choice == '5':
            print("Level Order Traversal:")
            level_order(newBT)

        elif choice == '6':
            key = input("Enter value to search: ")
            found = search_node(newBT, key)
            print("Found!" if found else "Not found.")

        elif choice == '7':
            node = get_deepest_node(newBT)
            print("Deepest Node:", node.data if node else "Tree is empty.")

        elif choice == '8':
            newBT, deleted = delete_deepest_node(newBT)
            print("Deleted Node:", deleted if deleted else "Nothing deleted.")

        elif choice == '9':
            print("Tree Structure:")
            print_tree(newBT)

        elif choice == '10':
            delete_entire_tree()

        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

        print("\n" + "-" * 40)

if __name__ == '__main__':
    main()


#############   Time & Space Complexity Table: Binary Tree using Linkedlist with help of Queue  ############

# |   Operation             |   Time Complexity   |   Space Complexity   |   Notes                                             |
# | ----------------------- | ------------------- | -------------------- | --------------------------------------------------- |
# |  insert_node()          | O(n)                | O(n)                 | Uses level-order (queue) to find first empty spot   |
# |  search_node()          | O(n)                | O(n)                 | Level-order search; worst case all nodes scanned    |
# |  pre_order()            | O(n)                | O(h) = O(n) worst    | Recursive, space is for call stack (height of tree) |
# |  in_order()             | O(n)                | O(h) = O(n) worst    | Same as above                                       |
# |  post_order()           | O(n)                | O(h) = O(n) worst    | Same as above                                       |
# |  level_order()          | O(n)                | O(n)                 | Queue stores all nodes at the deepest level         |
# |  get_deepest_node()     | O(n)                | O(n)                 | Level-order traversal to find last node             |
# |  delete_deepest_node()  | O(n)                | O(n)                 | Finds deepest node, searches again to delete it     |
# |  print_tree()           | O(n)                | O(h)                 | Prints tree sideways recursively                    |
# |  delete_entire_tree()   | O(1)                | O(1)                 | Sets root to None; Python GC handles node deletion  |
