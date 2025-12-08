"""
Design your implementation of the linked list. 
- int get(int index) Get the value of the indexth node in the linked list. 
    If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of the linked list. 
    After the insertion, the new node will be the first node of the linked list.
- void addAtTail(int val) Append a node of value val as the last element of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. 
    If index equals the length of the linked list, the node will be appended to the end of the linked list. 
    If index is greater than the length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
"""

class Node:
    def __init__(self,val):
        self.val=val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        curr = self.head
        count = 0
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp

    def addAtTail(self, val: int) -> None:
        temp = Node(val)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        temp = Node(val)
        count = 0
        curr = self.head
        while curr and count < index - 1:
            curr = curr.next
            count += 1
        if curr is None:
            return

        temp.next = curr.next
        curr.next = temp

        if temp.next is None:
            self.tail = temp
                    

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        
        curr = self.head
        count = 0
        
        while curr.next and count < index - 1:
            curr = curr.next
            count += 1
        
        if curr.next is None:
            return
        
        if curr.next == self.tail:
            self.tail = curr
        
        curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

val = int(input("Enter the Value to add at Head of SLL:"))
obj.addAtHead(val)

val = int(input("Enter the Value to add at Tail of SLL:"))
obj.addAtTail(val)


index = int(input("Enter the index to get the value: "))
param_1 = obj.get(index)
print(param_1)


obj.addAtIndex(index,val)

index = int(input("Enter the index to delete the value: "))
obj.deleteAtIndex(index)