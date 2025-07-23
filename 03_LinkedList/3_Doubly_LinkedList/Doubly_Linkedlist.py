class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '<->'
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
    
    def reverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            
    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
    
    def get_node(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        elif idx < self.length // 2:
            current_node = self.head
            for _ in range(idx):
                current_node = current_node.next
        else:
           current_node = self.tail
           for _ in range(self.length - 1, idx, -1):
               current_node = current_node.prev
        return current_node
    
    def set_value(self, idx, value):
        node = self.get_node(idx)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self, idx, value):
        if idx < 0 or idx > self.length:
            return "Index out of Range"
        
        if idx == 0:
            self.prepend(value)
            return True
        elif idx == self.length:
            self.append(value)
            return True

        new_node = Node(value)
        next_node = self.get_node(idx)
        prev_node = next_node.prev

        new_node.next = next_node
        new_node.prev = prev_node
        prev_node.next = new_node
        next_node.prev = new_node

        self.length += 1
        return True

    
    def pop_first(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if not self.head:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return "Index Out of range"
        
        if idx == 0:
            return self.pop_first()

        if idx == self.length -1:
            return self.pop()
 
        popped_node = self.get_node(idx)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

if __name__ == "__main__":
    
    new_linked_list = DLL()

    while True:
        print("\n--- MENU ---")
        print("1. Append")
        print("2. Prepend")
        print("3. Insert at Index")
        print("4. Search")
        print("5. Traverse (Forward)")
        print("6. Get by Index")
        print("7. Set by Index")
        print("8. Pop First")
        print("9. Pop Last")
        print("10. Remove by Index")
        print("11. Reverse Traverse")
        print("12. Length")
        print("13. Print List")
        print("14. Delete All")
        print("15. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = input("Enter value to append: ")
            new_linked_list.append(val)
            print("After append:", new_linked_list)

        elif choice == 2:
            val = input("Enter value to prepend: ")
            new_linked_list.prepend(val)
            print("After prepend:", new_linked_list)

        elif choice == 3:
            idx = int(input("Enter index to insert at: "))
            val = input("Enter value to insert: ")
            result = new_linked_list.insert(idx, val)
            print("Inserted" if result else "Invalid Index")
            print("After insert:", new_linked_list)

        elif choice == 4:
            val = input("Enter value to search: ")
            found = new_linked_list.search(val)
            print("Found" if found else "Not Found")

        elif choice == 5:
            print("Linked List (forward):")
            new_linked_list.traverse()

        elif choice == 6:
            idx = int(input("Enter index to get value: "))
            node = new_linked_list.get_node(idx)
            print("Value:", node.value if node else "Invalid Index")

        elif choice == 7:
            idx = int(input("Enter index to set value: "))
            val = input("Enter new value: ")
            updated = new_linked_list.set_value(idx, val)
            print("Updated" if updated else "Invalid Index")
            print("After set:", new_linked_list)

        elif choice == 8:
            node = new_linked_list.pop_first()
            print("Popped First:", node.value if node else "Nothing to pop")
            print("After pop_first:", new_linked_list)

        elif choice == 9:
            node = new_linked_list.pop()
            print("Popped Last:", node.value if node else "Nothing to pop")
            print("After pop:", new_linked_list)

        elif choice == 10:
            idx = int(input("Enter index to remove: "))
            node = new_linked_list.remove(idx)
            print("Removed:", node.value if node else "Invalid Index")
            print("After remove:", new_linked_list)

        elif choice == 11:
            print("Linked List (reverse):")
            new_linked_list.reverse()

        elif choice == 12:
            print(f"Length of Linked List is {new_linked_list.length}")

        elif choice == 13:
            print("Current List:", new_linked_list)

        elif choice == 14:
            new_linked_list.delete_all()
            print("All nodes deleted.")
            print("After delete all:", new_linked_list)

        elif choice == 15:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")



#############   Time & Space Complexity Table: Doubly Linked List  ############

# | Method             | Time Complexity | Space Complexity | Notes                                           |
# | ------------------ | --------------- | ---------------- | ----------------------------------------------- |
# |  append()          | O(1)            | O(1)             | Direct insertion at the tail                    |
# |  prepend()         | O(1)            | O(1)             | Direct insertion at the head                    |
# |  insert(index)     | O(n)            | O(1)             | O(n) traversal for arbitrary index              |
# |  search(value)     | O(n)            | O(1)             | May need to traverse entire list                |
# |  traverse()        | O(n)            | O(1)             | Prints elements forward                         |
# |  reverse()         | O(n)            | O(1)             | Prints elements in reverse order                |
# |  get_node(index)   | O(n)            | O(1)             | Bidirectional traversal based on index location |
# |  set_value(index)  | O(n)            | O(1)             | Depends on `get_node(index)`                    |
# |  pop_first()       | O(1)            | O(1)             | Removes the head node                           |
# |  pop()             | O(1)            | O(1)             | Removes the tail node                           |
# |  remove(index)     | O(n)            | O(1)             | O(n) for arbitrary index, O(1) for ends         |
# |  delete_all()      | O(1)            | O(1)             | Dereferences head and tail; GC clears memory    |
# |  __str__()         | O(n)            | O(n)             | Builds and returns a string representation      |

