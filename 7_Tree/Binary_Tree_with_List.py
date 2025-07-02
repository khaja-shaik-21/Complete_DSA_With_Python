# Binary Tree Creation using Python List

class BinaryTree:
    def __init__(self, size):
        self.customList = [None] * size  # Index 0 is unused
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 >= self.maxSize:
            return 'The Binary Tree is Full'
        self.lastUsedIndex += 1
        self.customList[self.lastUsedIndex] = value
        return 'The value has been successfully inserted.'

    def searchNode(self, value):
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                return f'Found at index {i}'
        return 'Not Found'

    def preOrder(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index], end=" ")
        self.preOrder(index * 2)
        self.preOrder(index * 2 + 1)

    def inOrder(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrder(index * 2)
        print(self.customList[index], end=" ")
        self.inOrder(index * 2 + 1)

    def postOrder(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrder(index * 2)
        self.postOrder(index * 2 + 1)
        print(self.customList[index], end=" ")

    def levelOrder(self):
        for i in range(1, self.lastUsedIndex + 1):
            print(self.customList[i], end=" ")
        print()

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "Binary Tree is empty"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return 'The node has been successfully deleted.'
        return "Node not found."

    def deleteTree(self):
        self.customList = None
        self.lastUsedIndex = 0
        return "Successfully deleted the entire binary tree."

    def displayTree(self):
        print("\nCurrent Binary Tree (Index : Value):")
        if self.lastUsedIndex == 0:
            print("Tree is empty.")
            return
        for i in range(1, self.lastUsedIndex + 1):
            print(f"[{i}] : {self.customList[i]}")
        print()


# ---------- Menu-Driven Program ----------
def main():
    size = int(input("Enter the maximum size of the binary tree: "))
    bt = BinaryTree(size + 1)  # +1 because index 0 is unused

    while True:
        print("\n--- Binary Tree Menu ---")
        print("1. Insert Node")
        print("2. Search Node")
        print("3. Delete Node")
        print("4. Preorder Traversal")
        print("5. Inorder Traversal")
        print("6. Postorder Traversal")
        print("7. Level Order Traversal")
        print("8. Delete Entire Tree")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            val = input("Enter value to insert: ")
            print(bt.insertNode(val))
            bt.displayTree()
        elif choice == '2':
            val = input("Enter value to search: ")
            print(bt.searchNode(val))
            bt.displayTree()
        elif choice == '3':
            val = input("Enter value to delete: ")
            print(bt.deleteNode(val))
            bt.displayTree()
        elif choice == '4':
            print("Preorder Traversal:")
            bt.preOrder(1)
            print()
            bt.displayTree()
        elif choice == '5':
            print("Inorder Traversal:")
            bt.inOrder(1)
            print()
            bt.displayTree()
        elif choice == '6':
            print("Postorder Traversal:")
            bt.postOrder(1)
            print()
            bt.displayTree()
        elif choice == '7':
            print("Level Order Traversal:")
            bt.levelOrder()
            bt.displayTree()
        elif choice == '8':
            print(bt.deleteTree())
            bt.displayTree()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



#############   Time & Space Complexity Table: Binary Tree using List (Array)  ############

# | Operation           | Time Complexity | Space Complexity  | Notes                                                      |
# | ------------------- | --------------- | ----------------- | ---------------------------------------------------------- |
# |  insertNode()       | O(1)            | O(1)              | Inserts at the next available index                        |
# |  searchNode()       | O(n)            | O(1)              | Linear search through the array                            |
# |  preOrder()         | O(n)            | O(h) = O(n) worst | Recursive traversal; space for call stack (height of tree) |
# |  inOrder()          | O(n)            | O(h) = O(n) worst | Same as above                                              |
# |  postOrder()        | O(n)            | O(h) = O(n) worst | Same as above                                              |
# |  levelOrder()       | O(n)            | O(1)              | Iterative print of all used nodes                          |
# |  deleteNode()       | O(n)            | O(1)              | Linear search, then overwrite last used node               |
# |  deleteTree()       | O(1)            | O(1)              | Sets list to `None`; Python GC handles the rest            |
# |  displayTree()      | O(n)            | O(1)              | Prints index and value of all used nodes                   |
