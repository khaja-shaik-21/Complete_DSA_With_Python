"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
"""
####### Method1: Using Only Stack #######
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if ((bracket == ')' and last == "(") or 
                    (bracket == "]"  and last == "[") or 
                    (bracket == "}"  and last == "{")):
                    continue
                else:
                    return False
        return len(stack) == 0 



####### Method1: Using Stack along with dict to match #######
class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', ']': '[', '}': '{'}
        close = [')', ']', '}']
        stack = []
        for c in s:
            if c in close:
                if len(stack) > 0 and stack[-1] == matching[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
    
    
    
# TC and SC for Both Codes Same
# Time Complexity : O(N)
# Space Complexity : O(N)