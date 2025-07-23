# Using LinkedList

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        values = []
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return '\n'.join(reversed(values))

class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def isEmpty(self):
        return self.linkedList.head is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.linkedList.head
        self.linkedList.head = new_node
        return 'Value Pushed'

    def pop(self):
        if self.isEmpty():
            return 'Stack is Empty'
        value = self.linkedList.head.value
        self.linkedList.head = self.linkedList.head.next
        return f'Popped: {value}'

    def peek(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return f'Top Element: {self.linkedList.head.value}'

    def delete_all(self):
        self.linkedList.head = None
        return 'Stack Cleared'

    def __str__(self):
        return str(self.linkedList)



def menu():
    s = Stack()
    while True:
        print("\n====== Stack Menu ======")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if Empty")
        print("5. Display Stack")
        print("6. Delete All")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            val = input("Enter value to push: ")
            print(s.push(val))
            print('🗑️ Current Stack:')
            print(s)
        elif choice == '2':
            print(s.pop())
            print('🗑️ Current Stack:')
            print(s)
        elif choice == '3':
            print(s.peek())
            print('🗑️ Current Stack:')
            print(s)
        elif choice == '4':
            print("Stack is Empty" if s.isEmpty() else "Stack is NOT Empty")
            print('🗑️ Current Stack:')
            print(s)
        elif choice == '5':
            print("🗑️ Current Stack:\n" + str(s) if not s.isEmpty() else "Stack is Empty")
        elif choice == '6':
            print(s.delete_all())
        elif choice == '7':
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice. Please enter between 1–7.")

if __name__ == '__main__':
    menu()


#############   Time & Space Complexity Table: Stack Using Python LinkedList  ############

# | Method         | Time Complexity | Space Complexity | Notes                                           |
# | -------------- | --------------- | ---------------- | ----------------------------------------------- |
# |  push()        | O(1)            | O(1)             | Inserts at the head of linked list              |
# |  pop()         | O(1)            | O(1)             | Removes head node                               |
# |  peek()        | O(1)            | O(1)             | Accesses head node                              |
# |  isEmpty()     | O(1)            | O(1)             | Checks head node                                |
# |  __str__()     | O(n)            | O(n)             | Traverses all nodes to print                    |
# |  delete_all()  | O(1)            | O(1)             | Sets head to None (GC clears memory eventually) |
