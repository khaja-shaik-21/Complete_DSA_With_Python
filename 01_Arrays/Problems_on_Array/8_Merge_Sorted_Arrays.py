"""
Merge two sorted arrays without duplicated
"""

######### Method 1: #########
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

Set = set()
if len(a) == len(b):
    for i in range(len(a)):
        Set.add(a[i])
        Set.add(b[i])
print(list(Set))

# Time Complexity : O(N)
# Space Complexity : O(N)


######### Method 2: #########
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

a_len = len(a)
b_len = len(b)

i = 0
j = 0
result = []

while i < a_len and j < b_len:
    if a[i] <= b[j]:
        if len(result) == 0 or result[-1] != a[i]:
            result.append(a[i])
        i += 1
    else:
        if len(result) == 0 or result[-1] != b[j]:
            result.append(b[j])
        j += 1

while i < a_len:
    if len(result) == 0 or result[-1] != a[i]:
            result.append(a[i])
    i += 1

while j < b_len:
    if len(result) == 0 or result[-1] != b[j]:
            result.append(b[j])
    j += 1

print(result)

# Time Complexity : O(n + m)
# Space Complexity (including output) : O(n + m)
# Space Complexity (excluding output) : O(1)

