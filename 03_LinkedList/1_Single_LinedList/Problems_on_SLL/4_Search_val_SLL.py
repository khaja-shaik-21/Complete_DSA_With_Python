"""
Given a linked list with the head node and a key, 
the task is to check if the key is present in the linked list or not. 
Return true if key is present, else return false.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def searchKey(self, head, key):
        if head == None:
            return False

        curr = head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False