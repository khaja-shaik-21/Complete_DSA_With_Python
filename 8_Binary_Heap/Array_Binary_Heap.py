class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekofHeap(rootNode):
    if not rootNode or rootNode.heapSize == 0:
        return None
    return rootNode.customList[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return 0
    return rootNode.heapSize

def preorderTraversal(heap, index=1):
    if index > heap.heapSize or heap.customList[index] is None:
        return
    print(heap.customList[index], end=' ')
    preorderTraversal(heap, 2 * index)       
    preorderTraversal(heap, 2 * index + 1)   

def inorderTraversal(heap, index=1):
    if index > heap.heapSize or heap.customList[index] is None:
        return
    inorderTraversal(heap, 2 * index)        
    print(heap.customList[index], end=' ')
    inorderTraversal(heap, 2 * index + 1)    

def postorderTraversal(heap, index=1):
    if index > heap.heapSize or heap.customList[index] is None:
        return
    postorderTraversal(heap, 2 * index)      
    postorderTraversal(heap, 2 * index + 1)  
    print(heap.customList[index], end=' ')

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i], end=' ')
    print()

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = index // 2
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]
            heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]
            heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.heapSize += 1
    rootNode.customList[rootNode.heapSize] = nodeValue
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = 2 * index
    rightIndex = 2 * index + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if (heapType == "Min" and rootNode.customList[index] > rootNode.customList[leftIndex]) or \
           (heapType == "Max" and rootNode.customList[index] < rootNode.customList[leftIndex]):
            rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]
        return

    if heapType == "Min":
        swapChild = leftIndex if rootNode.customList[leftIndex] < rootNode.customList[rightIndex] else rightIndex
        if rootNode.customList[index] > rootNode.customList[swapChild]:
            rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]
            heapifyTreeExtract(rootNode, swapChild, heapType)
    else:
        swapChild = leftIndex if rootNode.customList[leftIndex] > rootNode.customList[rightIndex] else rightIndex
        if rootNode.customList[index] < rootNode.customList[swapChild]:
            rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]
            heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return "Heap is empty"
    extractedNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractedNode

def deleteEntireBP(rootNode):
    rootNode.customList = [None] * rootNode.maxSize
    rootNode.heapSize = 0
    return "Heap cleared successfully"


def menu():
    print("Binary Heap Menu")
    print("1. Insert")
    print("2. Extract Root")
    print("3. Peek")
    print("4. Size of Heap")
    print("5. Level Order Traversal")
    print("6. Preorder Traversal")
    print("7. Inorder Traversal")
    print("8. Postorder Traversal")
    print("9. Delete Entire Heap")
    print("10. Show Heap (Internal List)")
    print("11. Exit")


if __name__ == "__main__":
    size = int(input("Enter the size of heap: "))
    while True:
        heapType = input("Enter heap type (Min/Max): ").strip().capitalize()
        if heapType in ["Min", "Max"]:
            print(f"You selected a {heapType} Heap.")
            break
        else:
            print("Invalid input. Please enter 'Min' or 'Max'.")

    heap = Heap(size)

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            val = int(input("Enter value to insert: "))
            print(insertNode(heap, val, heapType))
            print("Heap (Array View):", heap.customList[1:heap.heapSize + 1])
        elif choice == '2':
            print("Extracted:", extractNode(heap, heapType))
        elif choice == '3':
            print("Peek:", peekofHeap(heap))
        elif choice == '4':
            print("Current Size:", sizeofHeap(heap))
        elif choice == '5':
            if heap.heapSize == 0:
                print("Heap is empty.")
            else:
                print("Heap Elements:")
                levelOrderTraversal(heap)
        elif choice == '6':
            if heap.heapSize == 0:
                print("Heap is empty.")
            else:
                print("Preorder Traversal:")
                preorderTraversal(heap)
                print()
        elif choice == '7':
            if heap.heapSize == 0:
                print("Heap is empty.")
            else:
                print("Inorder Traversal:")
                inorderTraversal(heap)
                print()
        elif choice == '8':
            if heap.heapSize == 0:
                print("Heap is empty.")
            else:
                print("Postorder Traversal:")
                postorderTraversal(heap)
                print()
        elif choice == '9':
            print(deleteEntireBP(heap))
        elif choice == '10':
            if heap.heapSize == 0:
                print("Heap is empty.")
            else:
                print("Heap (Array View):", heap.customList[1:heap.heapSize + 1])
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
        print("-" * 40)



#############   Time & Space Complexity Table: Binary Heap Tree using using Array  ############


# | Operation              | Time Complexity            | Space Complexity           | Notes                                                     |
# |------------------------|----------------------------|----------------------------|------------------------------------------------------------|
# | insertNode()           | O(log n)                   | O(1)                       | Heapify-up from inserted node to root                     |
# | extractNode()          | O(log n)                   | O(1)                       | Replaces root and heapifies down to maintain structure    |
# | peekofHeap()           | O(1)                       | O(1)                       | Returns the root node                                     |
# | sizeofHeap()           | O(1)                       | O(1)                       | Just returns heapSize                                     |
# | levelOrderTraversal()  | O(n)                       | O(1)                       | Linear scan from index 1 to heapSize                      |
# | preorderTraversal()    | O(n)                       | O(h) = O(log n)            | Recursive, space used by call stack                      |
# | inorderTraversal()     | O(n)                       | O(h) = O(log n)            | Recursive, same as preorder                               |
# | postorderTraversal()   | O(n)                       | O(h) = O(log n)            | Recursive, same as preorder                               |
# | printHeapTree()        | O(n)                       | O(h) = O(log n)            | Recursively prints tree structure                         |
# | deleteEntireBP()       | O(1)                       | O(n)                       | Resets array to [None] * size; memory reused              |
