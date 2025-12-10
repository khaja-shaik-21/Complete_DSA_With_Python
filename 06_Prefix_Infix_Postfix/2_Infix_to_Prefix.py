"""
Reverse input

Swap ( and )

Convert to postfix

Reverse result → prefix
"""
def infix_to_postfix(exp):
    prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []
    output = ""

    for ch in exp:
        if ch.isalnum():
            output += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and prec.get(ch,0) <= prec.get(stack[-1],0):
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output

def infix_to_prefix(exp):
    exp = exp[::-1]
    exp = exp.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    postfix = infix_to_postfix(exp)
    return postfix[::-1]
