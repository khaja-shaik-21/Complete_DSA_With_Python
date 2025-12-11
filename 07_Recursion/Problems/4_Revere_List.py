"""
Reverse the List Using the Recursion
"""
def reverse(List, left, right):
    if left == right or left > right:
        return
    List[left], List[right] = List[right], List[left]
    reverse(List, left + 1, right - 1)
List = [1, 2, 3, 4]
left = 0
right = len(List) - 1
reverse(List, left, right)
print(List)