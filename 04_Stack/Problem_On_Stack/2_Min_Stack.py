"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""

class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if len(self.items) == 0:
            self.items.append([val, val])
        else:
            mini = min(self.items[-1][1], val)
            self.items.append([val, mini])

    def pop(self) -> None:
        if len(self.items) == 0:
            return False
        else:
            return self.items.pop()

    def top(self) -> int:
        if len(self.items) == 0:
            return False
        else:
            return self.items[-1][0]

    def getMin(self) -> int:
        if len(self.items) == 0:
            return False
        else:
            return self.items[-1][1]

#############   Time & Space Complexity Table: Min Stack   #############

# | Operation | Time | Space |
# | --------- | ---- | ----- |
# | push()    | O(1) | O(1)  |
# | pop()     | O(1) | O(1)  |
# | top()     | O(1) | O(1)  |
# | getMin()  | O(1) | O(1)  |
