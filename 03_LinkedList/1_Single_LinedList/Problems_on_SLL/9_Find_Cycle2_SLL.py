"""
Given the head of a linked list, 
return the node where the cycle begins. If there is no cycle, return null.
"""

def detetCycle(self, head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            slow = head
            
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
