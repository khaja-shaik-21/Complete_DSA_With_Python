"""
You are given the head_ref of a doubly Linked List and a Key. 
Your task is to delete all occurrences of the given key if it is present and return the new DLL.
"""

class Solution:
    def deleteAllOccurOfX(self, head, x):
        curr = head

        while curr:
            if curr.data == x:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev

            curr = curr.next

        return head

