class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating a linked list with none value.
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Print the Linkedlist
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    # append method to the linked list. It adds nodes to the end
    def append(self,value):
        new_node = Node(value)
        # if the Linkedlist is Empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if the Linkedlist is Not Empty
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    # prepend method to the linked list. It adds nodes to the first
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # insert method to the linked list. It adds nodes to the particular index
    def insert(self, index, value):
        new_node = Node(value)
        if index <0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1
        return True

    # Traversing the Linkedlist
    def traverse(self):
        current = self.head
        while current is not None: # or while current
            print(current.value)
            current = current.next

    # Search for a value
    def search(self, target):
        current = self.head
        # index = 0
        while current:
            if current.value == target:
                return True    # or return index
            current = current.next
            # index += 1
        return False    # or return -1

    # Get value using index
    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current

    # Update the value at the index using set function
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # delete the first node
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            return popped_node.value
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value

    # remove the last node
    def pop(self):
        # List is empty
        if self.head is None:
            return None

        temp = self.head
        prev = self.head

        # If there's only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value

        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None
        self.tail = prev
        self.length -= 1
        return temp.value


    # remove node at particular index
    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length -1 or index == -1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node.value

    # Delete all the nodes
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    
        
    def get_length(self):
        return f"Length of Linked List is {self.length}"

if __name__ == "__main__":
    
    new_linked_list = LinkedList()

    while True:
        print("\n--- MENU ---")
        print("1.Append() \n2.Prepend() \n3.Insert() \n4.Search() \n5.Traverse()")
        print("6.Get() \n7.Set() \n8.Pop_first() \n9.Pop() \n10.Remove()")
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
            new_linked_list.traverse()
        elif choice == 6:
            idx = int(input("Enter index to get value: "))
            result = new_linked_list.get(idx)
            print("Value:", result.value if result is not None else "Invalid Index")
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
            if val is not None:
                print("Popped Last:", val)
                print("After pop:", new_linked_list)
            else:
                print("Empty Linkedlist con't Popped")
        elif choice == 10:
            idx = int(input("Enter index to remove: "))
            val = new_linked_list.remove(idx)
            if val is not None:
                print("Removed:", val)
            else:
                print("Invalid Index")
            print("After remove:", new_linked_list)
        elif choice == 11:
            new_linked_list.delete_all()
            print("Deleted entire list.")
        elif choice == 12:
            print(new_linked_list.get_length())
        elif choice == 13:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

        

#############   Time & Space Complexity Table: Singly Linked List  ############

# | Method          | Time Complexity | Space Complexity | Notes                                            |
# | --------------- | --------------- | ---------------- | ------------------------------------------------ |
# |  append()       | O(1)            | O(1)             | Uses `tail` pointer for efficient tail insertion |
# |  prepend()      | O(1)            | O(1)             | Directly modifies `head` pointer                 |
# |  insert(index)  | O(n)            | O(1)             | Traverses up to index                            |
# |  search(value)  | O(n)            | O(1)             | Full traversal in worst case                     |
# |  travers()      | O(n)            | O(1)             | Iterates over entire list                        |
# |  get(index)     | O(n)            | O(1)             | Traverses from `head` up to index                |
# |  set_value()    | O(n)            | O(1)             | Relies on `get()` internally                     |
# |  pop_first()    | O(1)            | O(1)             | Removes `head`, updates pointer                  |
# |  pop()          | O(n)            | O(1)             | Traverses to second-last node to update `tail`   |
# |  remove(index)  | O(n)            | O(1)             | O(1) for `0`, O(n) otherwise                     |
# |  delete_all()   | O(1)            | O(1)             | Dereferences `head` and `tail`                   |
# |  __str__()      | O(n)            | O(n)             | Builds a printable string of the list            |