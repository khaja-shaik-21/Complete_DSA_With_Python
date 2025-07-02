class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        if self.isEmpty():
            return "Queue is Empty"
        return ' <- '.join([str(node.value) for node in self.linkedlist])

    def isEmpty(self):
        return self.linkedlist.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.linkedlist.head = self.linkedlist.tail = new_node
        else:
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node
        return "Enqueued"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        removed = self.linkedlist.head
        if self.linkedlist.head == self.linkedlist.tail:
            self.linkedlist.head = self.linkedlist.tail = None
        else:
            self.linkedlist.head = self.linkedlist.head.next
        return f"Dequeued: {removed.value}"

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return f"Front Element: {self.linkedlist.head.value}"

    def delete_all(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None
        return "🗑️ Queue Cleared"


def menu():
    q = Queue()
    while True:
        print("\n====== Linked List Queue Menu ======")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check if Empty")
        print("5. Delete All")
        print("6. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == '1':
            val = input("Enter value to enqueue: ")
            print(q.enqueue(val))
            print("🗑️ Current Queue")
            print(q)
            
        elif choice == '2':
            print(q.dequeue())
            print("🗑️ Current Queue")
            print(q)
            
        elif choice == '3':
            print(q.peek())
            
        elif choice == '4':
            print("Queue is Empty" if q.isEmpty() else "Queue is NOT Empty")
            print("🗑️ Current Queue")
            print(q)
            
        elif choice == '5':
            print(q.delete_all())
            
        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice. Please enter between 1–7.")

# Run the menu
if __name__ == '__main__':
    menu()


#############   Time & Space Complexity Table: Queue Using Linked List  ############


# | Method         | Time Complexity | Space Complexity | Notes                             |
# | -------------- | --------------- | ---------------- | --------------------------------- |
# |  enqueue()     | O(1)            | O(1)             | Add at tail                       |
# |  dequeue()     | O(1)            | O(1)             | Remove from head                  |            
# |  peek()        | O(1)            | O(1)             | Access front                      |
# |  isEmpty()     | O(1)            | O(1)             | Just check if head is None        |
# |  __str__()     | O(n)            | O(n)             | Traverse and join all node values |
# |  delete_all()  | O(1)            | O(1)             | Clear head and tail references    |
