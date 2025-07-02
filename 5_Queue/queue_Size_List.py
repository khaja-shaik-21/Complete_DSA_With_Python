# Queue Using Python List Without Size Limit

class Queue:
    def __init__(self, maxSize):
        self.list = [None] * maxSize
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        if self.isEmpty():
            return "Queue is Empty"
        values = []
        i = self.start
        while True:
            values.append(str(self.list[i]))
            if i == self.top:
                break
            i = (i + 1) % self.maxSize
        return ' <- '.join(values)

    def isFull(self):
        return (self.top + 1) % self.maxSize == self.start

    def isEmpty(self):
        return self.start == -1

    def enqueue(self, value):
        if self.isFull():
            return "Queue is Full"
        if self.isEmpty():
            self.start = 0
            self.top = 0
        else:
            self.top = (self.top + 1) % self.maxSize
        self.list[self.top] = value
        return "Enqueued"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        value = self.list[self.start]
        if self.start == self.top:
            self.start = -1
            self.top = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        return f"Dequeued: {value}"

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return f"Front Element: {self.list[self.start]}"
    
    def delete_all(self):
        self.list = [None] * self.maxSize
        self.start = -1
        self.top = -1
        return "🗑️ Queue Cleared"

def menu():
    q = Queue(5)
    while True:
        print("\n====== Circular Queue Menu ======")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check if Empty")
        print("5. Check if Full")
        print("6. Delete All")
        print("7. Exit")

        choice = input("Enter your choice (1–8): ")

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
            print("🗑️ Current Queue")
            print(q)
            
        elif choice == '4':
            print("Queue is Empty" if q.isEmpty() else "Queue is NOT Empty")
            print("🗑️ Current Queue")
            print(q)
            
        elif choice == '5':
            print("Queue is Full" if q.isFull() else "Queue is NOT Full")
            print("🗑️ Current Queue")
            print(q)
            
        elif choice == '6':
            print(q.delete_all())
            
        elif choice == '7':
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice. Please enter between 1–8.")

# Run the menu
if __name__ == '__main__':
    menu()


#############   Time & Space Complexity Table: Queue Using Python List With Size Limit  ############

# | Method         | Time Complexity | Space Complexity | Notes                                            |
# | -------------- | --------------- | ---------------- | ------------------------------------------------ |
# |  enqueue()     | O(1)            | O(1)             | Circular insert using modulo                     |
# |  dequeue()     | O(1)            | O(1)             | Circular removal from front                      |
# |  peek()        | O(1)            | O(1)             | Accesses the front element                       |
# |  isEmpty()     | O(1)            | O(1)             | Checks if queue is empty                         |
# |  isFull()      | O(1)            | O(1)             | Checks if next slot is the start                 |
# |  __str__()     | O(n)            | O(n)             | Iterates from start to top (handles wrap-around) |
# |  delete_all()  | O(1)            | O(n)             | Reinitializes the list                           |
