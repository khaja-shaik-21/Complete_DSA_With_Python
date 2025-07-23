# Using Python List Without Size Limit.

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, value):
        self.list.append(value)
        return 'Value Pushed'

    def pop(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return f'Popped: {self.list.pop()}'

    def peek(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return f'Top Element: {self.list[-1]}'

    def delete_all(self):
        self.list = []
        return 'Stack Cleared'


# Menu Interface
if __name__ == '__main__':
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

        # psuh
        if choice == '1':
            val = input("Enter value to push: ")
            print(s.push(val))
            print('Current Stack:')
            print(s)
        
        # pop
        elif choice == '2':
            print(s.pop())
            print('Current Stack:')
            print(s)
        
        # peek
        elif choice == '3':
            print(s.peek())
            print('Current Stack:')
            print(s)
        
        # isEmpty
        elif choice == '4':
            print("Stack is Empty" if s.isEmpty() else "Stack is NOT Empty")
            print('Current Stack:')
            print(s)
        
        # Print Stack
        elif choice == '5':
            print("Current Stack:\n" + str(s) if not s.isEmpty() else "Stack is Empty")
        
        # Delete All
        elif choice == '6':
            print(s.delete_all())
        
        # Exit
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print(" Invalid choice. Please enter between 1–7.")




#############   Time & Space Complexity Table: Stack Using Python List Without Size Limit  ############

# | Method         | Time Complexity | Space Complexity | Notes                                         |
# | -------------- | --------------- | ---------------- | --------------------------------------------- |
# |  push()        | O(1)            | O(1)             | Appending at the end of list is constant time |
# |  pop()         | O(1)            | O(1)             | Removing last item from list                  |
# |  peek()        | O(1)            | O(1)             | Accessing last item in list                   |
# |  isEmpty()     | O(1)            | O(1)             | Simple length check                           |
# |  __str__()     | O(n)            | O(n)             | Reverses and joins the list for display       |
# |  delete_all()  | O(1)            | O(1)             | Resets list reference                         |
