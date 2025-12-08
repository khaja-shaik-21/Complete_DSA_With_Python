"""
Given the head of a linked list, determine whether the list contains a loop. 
If a loop is present, return the number of nodes in the loop, otherwise return 0.
"""


####### Method 1: Bruit Force #######

class Solution:
    def lengthOfLoop(self, head):
        temp = head
        my_dict = {}
        travel = 0
        
        while temp:
            if temp in my_dict:
                return travel - my_dict[temp]
            
            my_dict[temp] = travel
            travel += 1
            temp = temp.next
        return 0
    

####### Method 2: #######
class Solution:
    def lengthOfLoop(self, head):
        if not head or not head.next:
            return 0
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                count = 1
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0