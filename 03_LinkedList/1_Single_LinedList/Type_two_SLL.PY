class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        
    def traverse(self):
        if self.head is None:
            print("SLL is Empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next
            print()

    def insert(self, idx, value):
        new_node = Node(value)

        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return

        count = 0
        curr = self.head
        prev = None

        while curr is not None and count < idx:
            prev = curr
            curr = curr.next
            count += 1

        if prev is None:
            raise IndexError("Index out of range")

        prev.next = new_node
        new_node.next = curr

    def delete_node(self, value):
        temp = self.head
        if temp.next is not None:
            if temp.val == value:
                self.head = temp.next
                temp.next = None
                return
            else:
                prev = None
                found = False
                while temp is not None:
                    if temp.val == value:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next = temp.next
                    temp.next = None
                    return
                else:
                    print("Node is not found.")
    
    def delete_all(self):
        self.head = None
