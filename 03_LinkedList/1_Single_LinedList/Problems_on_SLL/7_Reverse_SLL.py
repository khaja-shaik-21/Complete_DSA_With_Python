"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev