"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""

def hasCycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False