class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CircularSinglyLinkedList:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def __str__(self):
        if self.head is None:
            return "Empty List"
        result = ''
        current = self.head
        while True:
            result += str(current.value)
            current = current.next
            if current == self.head:
                break
            result += '->'
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
        return True
        
    def traverse(self):
        if self.head is None:
            return []
        result = []
        current = self.head
        while True:
            result.append(current.value)
            current = current.next
            if current == self.head:
                break
        return result

    def search(self, target):
        if self.head is None:
            return False
        current = self.head
        while True:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        popped_node.next = None
        self.length -= 1
        return popped_node.value

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
        popped_node.next = None
        self.length -= 1
        return popped_node.value

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        removed_node = temp.next
        temp.next = removed_node.next
        removed_node.next = None
        self.length -= 1
        return removed_node.value
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get_length(self):
        return f"Length of Linked List is {self.length}"

if __name__ == "__main__":
    
    new_linked_list = CircularSinglyLinkedList()

    while True:
        print("\n--- MENU ---")
        print("1.Append() \n2.Prepend() \n3.Insert() \n4.Search() \n5.Traverse()")
        print("6.Get() \n7.Set_value() \n8.Pop_first() \n9.Pop() \n10.Remove()")
        print("11.Delete All \n12.Length() \n13.Exit")

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
            print("Current list:", new_linked_list)
        elif choice == 5:
            print("Linked List:")
            print(new_linked_list.traverse())
        elif choice == 6:
            idx = int(input("Enter index to get value: "))
            result = new_linked_list.get(idx)
            print("Value:", result.value if result else "Invalid Index")
            print("Current list:", new_linked_list)
        elif choice == 7:
            idx = int(input("Enter index to set value: "))
            val = input("Enter new value: ")
            updated = new_linked_list.set_value(idx, val)
            print("Updated" if updated else "Invalid Index")
            print("After set:", new_linked_list)
        elif choice == 8:
            val = new_linked_list.pop_first()
            print("Popped First:", val)
            print("After pop_first:", new_linked_list)
        elif choice == 9:
            val = new_linked_list.pop()
            print("Popped Last:", val)
            print("After pop:", new_linked_list)
        elif choice == 10:
            idx = int(input("Enter index to remove: "))
            val = new_linked_list.remove(idx)
            print("Removed:", val if val is not None else "Invalid Index")
            print("After remove:", new_linked_list)
        elif choice == 11:
            new_linked_list.delete_all()
            print("Deleted entire list.")
            print("After delete_all:", new_linked_list)
        elif choice == 12:
            print(new_linked_list.get_length())
        elif choice == 13:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")



#############   Time & Space Complexity Table: Circular Singly Linked List  ############
   
# | Method            | Time Complexity | Space Complexity | Notes                                    |
# | ----------------- | --------------- | ---------------- | ---------------------------------------- |
# |  append()         | O(1)            | O(1)             | Direct insertion at tail                 |
# |  prepend()        | O(1)            | O(1)             | Direct insertion at head                 |
# |  insert(index)    | O(n)            | O(1)             | O(n) traversal for arbitrary index       |
# |  search(value)    | O(n)            | O(1)             | May need to traverse entire list         |
# |  traverse()       | O(n)            | O(n)             | Stores all values in a list              |
# |  get(index)       | O(n)            | O(1)             | Sequential traversal to index            |
# |  set(index, val)  | O(n)            | O(1)             | Depends on `get(index)`                  |
# |  pop_first()      | O(1)            | O(1)             | Remove head                              |
# |  pop()            | O(n)            | O(1)             | Must traverse to find node before tail   |
# |  remove(index)    | O(n)            | O(1)             | O(1) for 0 or last index, O(n) otherwise |
# |  delete()         | O(1)            | O(1)             | Just dereferences head and tail          |
# |  __str__()        | O(n)            | O(n)             | Builds a string representing the list    |
