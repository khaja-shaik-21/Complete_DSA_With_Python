"""
You are given the head of a doubly linked list. 
You have to reverse the doubly linked list and return its head.
"""
class Solution:
    def reverse(self, head):
        if head.next is None:
            return head
        
        prev = None
        curr = head
        while curr:
            front = curr.next
            curr.next = prev
            curr.prev = front
            prev = curr
            curr = front
            
        return prev