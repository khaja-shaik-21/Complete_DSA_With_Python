"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

class Solution:
    def removeNthFromEnd(self, head, n):        
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        
        if fast == None:
            return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head
            
        
        