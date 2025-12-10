"""
Scan left → right

If operand → push to stack

If operator → pop two operands:
    Combine as (op1 operator op2)
    Push back
"""

def postfix_to_infix(exp):
    stack = []
    for ch in exp:
        if ch.isalnum():
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({b}{ch}{a})")
    return stack[-1]
