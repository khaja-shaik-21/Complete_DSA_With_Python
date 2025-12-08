"""
Given head of a singly linked list. The task is to find the length of the linked list, 
where length is defined as the number of nodes in the linked list.
"""

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
class Solution:
    def getCount(self, head):
        if head == None:
            return 0
        
        count = 1
        curr = head
        
        while curr.next is not None:
            curr = curr.next
            count += 1
        
        return count