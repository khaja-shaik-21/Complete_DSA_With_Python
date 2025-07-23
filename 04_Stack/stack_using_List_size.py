# Using Python List With Size Limit.

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    def isEmpty(self):
        return len(self.list) == 0

    def isFull(self):
        return len(self.list) == self.maxSize

    def push(self, value):
        if self.isFull():
            return 'Stack is Full'
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
def menu():
    s = Stack(5)  # You can change the size here
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
        elif choice == '2':
            print(s.pop())
        elif choice == '3':
            print(s.peek())
        elif choice == '4':
            print("Stack is Empty" if s.isEmpty() else "Stack is NOT Empty")
        elif choice == '5':
            print("Stack:\n" + str(s) if not s.isEmpty() else "Stack is Empty")
        elif choice == '6':
            print(s.delete_all())
        elif choice == '7':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Please enter between 1–7.")

# Run the menu
if __name__ == '__main__':
    menu()



#############   Time & Space Complexity Table: Stack Using Python List With Size Limit  ############

# | Method         | Time Complexity | Space Complexity | Notes                             |
# | -------------- | --------------- | ---------------- | --------------------------------- |
# |  push()        | O(1)            | O(1)             | Checks for size before appending  |
# |  pop()         | O(1)            | O(1)             | Removes the last element          |
# |  peek()        | O(1)            | O(1)             | Direct access to the last element |
# |  isEmpty()     | O(1)            | O(1)             | Checks list length                |
# |  isFull()      | O(1)            | O(1)             | Compares list length with maxSize |
# |  __str__()     | O(n)            | O(n)             | Reverses and joins list elements  |
# |  delete_all()  | O(1)            | O(1)             | Resets list to empty              |
