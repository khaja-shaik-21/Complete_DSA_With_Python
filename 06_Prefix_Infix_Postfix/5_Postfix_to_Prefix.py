"""
If operand → push to stack

If operator → pop 2 operands
    op2 = pop()
    op1 = pop()

Create: operator + op1 + op2
Push back to stack
"""
def postfix_to_prefix(expression):
    stack = []
    
    for ch in expression:
        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = ch + op1 + op2
            stack.append(new_expr)
    
    return stack[-1]

exp = "AB+CD-*"
print(postfix_to_prefix(exp))   # -*+ABCD