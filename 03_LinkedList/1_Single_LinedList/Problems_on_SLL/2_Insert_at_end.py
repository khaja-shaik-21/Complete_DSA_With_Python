"""
You are given the head of a Singly Linked List and a value x, 
insert that value x at the end of the LinkedList and return the head of the modified Linked List.
"""

 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insertAtEnd(self, head, x):
        if head == None:
            head = Node(x)
            return head
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(x)
        
        return head