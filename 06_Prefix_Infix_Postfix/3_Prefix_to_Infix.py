"""
Scan right → left

If operand → push

If operator → pop two operands:
    Combine as (op1 operator op2)
"""
def prefix_to_infix(exp):
    stack = []
    for ch in reversed(exp):
        if ch.isalnum():
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({a}{ch}{b})")
    return stack[-1]
