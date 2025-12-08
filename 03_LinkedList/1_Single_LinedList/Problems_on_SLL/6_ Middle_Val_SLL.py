"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

def middleNode(self, head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = head.next
        fast =fast.next.next
    
    return slow
    