"""
If operand → push to stack

If operator → pop 2 operands
    op1 = pop()
    op2 = pop()

Create: op1 + op2 + operator
Push back to stack
"""
def prefix_to_postfix(expression):
    stack = []

    for ch in reversed(expression):
        if ch.isalnum():
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = op1 + op2 + ch
            stack.append(new_expr)
    
    return stack[-1]

exp = "*+AB-CD"
print(prefix_to_postfix(exp))   # AB+CD-*