"""
Given a doubly linked list of n nodes sorted by values, 
the task is to remove duplicate nodes present in the linked list.
"""
####### Method 1: most common approach #######
def removeDuplicates(self, head):
    cur = head
    while cur and cur.next:
        if cur.data == cur.next.data:
            duplicate = cur.next
            cur.next = duplicate.next
            if duplicate.next:
                duplicate.next.prev = cur
        else:
            cur = cur.next
    return head


####### Method 2: #######
class Solution:
    def removeDuplicates(self, head):
        cur = head  # Current node pointer for traversal
        
        while cur:
            # Check if current node is duplicate of previous node
            if cur.prev and cur.prev.data == cur.data:
                # Handle case where previous node is the head
                if cur.prev == head:
                    cur.prev = None        # Remove backward link
                    head = cur            # Update head to current node
                else:
                    # Remove the previous duplicate node by updating links
                    cur.prev.prev.next = cur     # Connect prev's prev to current
                    cur.prev = cur.prev.prev     # Connect current to prev's prev
            
            cur = cur.next  # Move to next node
        
        return head