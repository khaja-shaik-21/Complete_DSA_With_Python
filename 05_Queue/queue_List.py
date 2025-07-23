# Queue Using Python List Without Size Limit

class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' <- '.join(values)

    def isEmpty(self):
        return len(self.list) == 0

    def enqueue(self, value):
        self.list.append(value)
        return "Enqueued Successfully"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return f"Dequeued: {self.list.pop(0)}"  # FIFO

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return f"Front Element: {self.list[0]}"

    def delete_all(self):
        self.list = []
        return "🗑️ Queue Cleared"

def menu():
    q = Queue()
    while True:
        print("\n====== Queue Menu ======")
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
            print("🗑️ Current Queue")
            print(q)
        elif choice == '4':
            print("Queue is Empty" if q.isEmpty() else "Queue is NOT Empty")
            print("🗑️ Current Queue")
            print(q)
        elif choice == '5':
            print(q.delete_all())
            print("🗑️ Current Queue")
            print(q)
        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice. Please enter between 1–7.")

# Run the menu
if __name__ == '__main__':
    menu()


#############   Time & Space Complexity Table: Queue Using Python List Without Size Limit  ############

# | Method         | Time Complexity | Space Complexity | Notes                                        |
# | -------------- | --------------- | ---------------- | -------------------------------------------- |
# |  enqueue()     | O(1)            | O(1)             | Append at end of list                        |
# |  dequeue()     | O(n)            | O(1)             | Pops from start (inefficient for large size) |
# |  peek()        | O(1)            | O(1)             | Access front element                         |
# |  isEmpty()     | O(1)            | O(1)             | Length check                                 |
# |  __str__()     | O(n)            | O(n)             | Builds string from all elements              |
# |  delete_all()  | O(1)            | O(1)             | Clears the list                              |
