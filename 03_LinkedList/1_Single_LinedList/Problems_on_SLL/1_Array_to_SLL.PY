class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def constructLL(arr):
    if not arr:
        return None

    head = Node(arr[0])
    curr = head
    
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next

    temp = head
    while temp.next is not None:
        print(temp.data, end="->")
        temp = temp.next


arr = [1, 2, 3, 4, 5]
constructLL(arr)